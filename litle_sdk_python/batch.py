# -*- coding: utf-8 -*-l
# Copyright (c) 2017 Vantiv eCommerce
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
from __future__ import print_function

import datetime
import os

import paramiko
import six

import litle_xml_fields
import utils

# Key: transaction name
# Value: array of batchRequest attributes according to transactions
_supported_transaction_types = {
    'activate': ['numActivates', 'activateAmount'],
    'auth': ['numAuths', 'authAmount'],
    'authReversal': ['numAuthReversals', 'authReversalAmount'],
    'balanceInquiry': ['numBalanceInquirys', ''],
    'cancelSubscription': ['numCancelSubscriptions', ''],
    'capture': ['numCaptures', 'captureAmount'],
    'captureGivenAuth': ['numCaptureGivenAuths', 'captureGivenAuthAmount'],
    'createPlan': ['numCreatePlans', ''],
    'credit': ['numCredits', 'creditAmount'],
    'deactivate': ['numDeactivates', ''],
    'echeckCredit': ['numEcheckCredit', 'echeckCreditAmount'],
    'echeckPreNoteSale': ['numEcheckPreNoteSale', ''],
    'echeckRedeposit': ['numEcheckRedeposit', ''],
    'echeckSale': ['numEcheckSales', 'echeckSalesAmount'],
    'echeckVerification': ['numEcheckVerification', 'echeckVerificationAmount'],
    'forceCapture': ['numForceCaptures', 'forceCaptureAmount'],
    'load': ['numLoads', 'loadAmount'],
    'registerTokenRequest': ['numTokenRegistrations', ''],
    'sale': ['numSales', 'saleAmount'],
    'unload': ['numUnloads', 'unloadAmount'],
    'updateCardValidationNumOnToken': ['numUpdateCardValidationNumOnTokens', ''],
    'updatePlan': ['numUpdatePlans', ''],
    'updateSubscription': ['numUpdateSubscriptions', ''],
    'payFacCredit': ['numPayFacCredit', 'payFacCreditAmount'],
    'payFacDebit': ['numPayFacDebit', 'payFacDebitAmount'],
    'reserveCredit': ['numReserveCredit', 'reserveCreditAmount'],
    'reserveDebit': ['numReserveDebit', 'reserveDebitAmount'],
    'submerchantCredit': ['numSubmerchantCredit', 'submerchantCreditAmount'],
    'submerchantDebit': ['numSubmerchantDebit', 'submerchantDebitAmount'],
    'vendorCredit': ['numVendorCredit', 'vendorCreditAmount'],
    'vendorDebit': ['numVendorDebit', 'vendorDebitAmount'],
    'echeckPreNoteCredit': ['numEcheckPreNoteCredit', ''],
    'accountUpdate': ['numAccountUpdates', ''],
    # '': ['numExtCaptures', 'extCaptureAmount'],
    'physicalCheckDebit': ['numPhysicalCheckDebit', 'physicalCheckDebitAmount'],
    'physicalCheckCredit': ['numPhysicalCheckCredit', 'physicalCheckCreditAmount'],
}


def submit(transactions, conf, filename='', timeout=60):
    """Submitting a Session File for Processing to server via sFTP

    1. Generate litleRequest xml.
    2. Save xml at local file system.
    3. Send xml file to server.

    Args:
        transactions: an instance of batch.Transactions.
        conf: An instance of utils.Configuration.
        filename: String. File name for generated xml file. If the file exist, a timestamp string will be added.
        timeout: Positive int. Timeout in second for ssh connection for sftp.

    Returns:
        filename of file in inbound folder at remote server with '.asc' as extension.

    Raises:
        Exception depends on when get it.
    """
    if not isinstance(transactions, Transactions):
        raise TypeError('transactions must be an instance of batch.Transactions')

    if transactions.num_transactions < 1:
        raise ValueError('transactions must have at least 1 transaction')

    if not isinstance(conf, utils.Configuration):
        raise TypeError('conf must be an instance of utils.Configuration')

    if not isinstance(filename, six.string_types):
        raise TypeError('filename must be a string')

    if not isinstance(timeout, six.integer_types) or timeout < 0:
        raise ValueError('timeout must be an positive int')

    # 1. Generate litleRequest xml.
    xml_str = _create_batch_xml(transactions, conf)

    # 2. Save xml at local file system.
    file_path = _save_str_file(xml_str, conf.batch_requests_path, filename)

    # 3. Send xml file to server.
    remote_filename = _put_file_to_sftp(file_path, conf, timeout)
    return remote_filename


def download(filename, conf, timeout=60):
    """Download Processed Session File from server via sFTP

    Get xml file from server and save to local file system

    Args:
        filename: filename of file in outbound folder at remote server with '.asc' as extension.
        conf:  An instance of utils.Configuration.
        timeout: Timeout in second for ssh connection for sftp.

    Returns:
        path for file that saved in local file system.

    Raises:
        Exception depends on when get it.
    """
    if not isinstance(conf, utils.Configuration):
        raise TypeError('conf must be an instance of utils.Configuration')

    if not isinstance(filename, six.string_types) or len(filename) < 4:
        raise TypeError('filename must be a string, and at least 4 chars')

    if not isinstance(timeout, six.integer_types) or timeout < 0:
        raise ValueError('timeout must be an positive int')

    return _get_file_from_sftp(filename, conf, timeout)


def retrieve(filename, conf, return_format='object', save_to_local=False, timeout=60):
    """Retrieving Processed Session File from server via sFTP

    1. Get xml file string from server and return object
    2. If save_to_local, save to local file system

    Args:
        filename: filename of file in outbound folder at remote server with '.asc' as extension.
        conf:  An instance of utils.Configuration.
        return_format: Return format. The default is 'object'. Could be either 'object' or 'xml'.
        save_to_local: whether save file to local. default is false.
        timeout: Timeout in second for ssh connection for sftp.

    Returns:
        response XML in desired format.

    Raises:
        Exception depends on when get it.
    """
    if not isinstance(conf, utils.Configuration):
        raise TypeError('conf must be an instance of utils.Configuration')

    if not isinstance(filename, six.string_types) or len(filename) < 4:
        raise TypeError('filename must be a string, and at least 4 chars')

    if not isinstance(timeout, six.integer_types) or timeout < 0:
        raise ValueError('timeout must be an positive int')

    xml_str = _get_file_str_from_sftp(filename, conf, timeout)
    if save_to_local:
        _save_str_file(xml_str, conf.batch_response_path, filename)

    if return_format.lower() == 'xml':
        return xml_str
    else:
        return litle_xml_fields.CreateFromDocument(xml_str)


def stream(transactions, conf, return_format='object', timeout_send=60, timeout_rev=1):
    """stream batch request to IBC (inbound batch communicator) via socket and get return object

    Args:
        transactions: an instance of batch.Transactions.
        conf: An instance of utils.Configuration.
        return_format: Return format. The default is 'object'. Could be either 'object' or 'xml'.
        timeout_send: Positive int. Timeout in second for socket connection when sending.
        timeout_rev: Positive int. Timeout in second for socket connection when receiving.

    Returns:
        response XML in desired format.

    """
    if not isinstance(transactions, Transactions):
        raise TypeError('transactions must be an instance of batch.Transactions')

    if transactions.num_transactions < 1:
        raise ValueError('transactions must have at least 1 transaction')

    if not isinstance(conf, utils.Configuration):
        raise TypeError('conf must be an instance of utils.Configuration')

    if not isinstance(timeout_send, six.integer_types) or timeout_send < 0:
        raise ValueError('timeout_send must be an positive int')

    if not isinstance(timeout_rev, six.integer_types) or timeout_rev < 0:
        raise ValueError('timeout_rev must be an positive int')

    xml_str = _create_batch_xml(transactions, conf)
    response_xml = _stream_socket(xml_str, conf, timeout_send, timeout_rev)

    if return_format.lower() == 'xml':
        return response_xml
    else:
        return litle_xml_fields.CreateFromDocument(response_xml)


def _stream_socket(xml_str, conf, timeout_send, timeout_rev):
    """Send and receive xml string via socket connection

    Args:
        xml_str: Batch request xml string
        conf: An instance of utils.Configuration.
        timeout_send: Positive int. Timeout in second for socket connection when sending.
        timeout_rev: Positive int. Timeout in second for socket connection when receiving.

    Returns:
        Response xml string
    """
    import socket
    import ssl
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    s.settimeout(timeout_send)

    if conf.fast_ssl:
        s = ssl.wrap_socket(s)

    try:
        s.connect((conf.fast_url, int(conf.fast_port)))
    except:
        # TODO customized exceptions
        raise Exception("Exception connect to vantiv")

    s.sendall(xml_str)

    s.settimeout(0.0)
    str_array = []
    import time
    start = time.time()
    timeout_rev_double = timeout_rev * 2
    while True:
        if str_array and time.time() - start > timeout_rev:
            break
        if time.time() - start > timeout_rev_double:
            break
        # noinspection PyBroadException
        try:
            data = s.recv(512)
            if data:
                str_array.append(data)
                start = time.time()
            else:
                time.sleep(0.1)
        except:
            pass

    s.close()

    return_str = ''.join(str_array)

    if conf.print_xml:
        print('Batch stream response XML: \n', return_str)

    return return_str


def _put_file_to_sftp(file_path, conf, timeout):
    """Upload file to server via sftp.

    Args:
        file_path: local file path
        conf: An instance of utils.Configuration.
        timeout: Timeout in second for ssh connection for sftp.

    Returns:
        filename of file in inbound folder at remote server with '.asc' as extension.
    """
    basename = os.path.basename(file_path)
    remote_path_prg = 'inbound/%s.prg' % basename
    remote_path_asc = 'inbound/%s.asc' % basename

    transport = ''
    try:
        # noinspection PyTypeChecker
        transport = paramiko.Transport((conf.sftp_url, 22))
        transport.connect(username=conf.sftp_username, password=conf.sftp_password)
        channel = transport.open_session()
        channel.settimeout(timeout)
        sftp = paramiko.SFTPClient.from_transport(transport)
        while __check_file_exist_in_sftp(sftp, remote_path_prg) or __check_file_exist_in_sftp(sftp, remote_path_asc):
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            remote_path_prg = 'inbound/%s_%s.prg' % (basename, timestamp)
            remote_path_asc = 'inbound/%s_%s.asc' % (basename, timestamp)
        sftp.put(file_path, remote_path_prg)
        sftp.rename(remote_path_prg, remote_path_asc)
        transport.close()
    except Exception as e:
        # noinspection PyBroadException
        try:
            transport.close()
        except:
            pass
        # TODO customized exceptions
        raise Exception('fail to send', e.message)

    return os.path.basename(remote_path_asc)


def _get_file_from_sftp(filename, conf, timeout):
    """Download file from server via sftp

    Args:
        filename: filename in outbound folder
        conf: An instance of utils.Configuration.
        timeout: Timeout in second for ssh connection for sftp.

    Returns:
        path for file that saved in local file system.
    """
    if not os.path.exists(conf.batch_response_path):
        os.makedirs(conf.batch_response_path)
    local_path = os.path.join(conf.batch_response_path, filename)

    remote_path_asc = 'outbound/' + filename

    transport = ''
    try:
        # noinspection PyTypeChecker
        transport = paramiko.Transport((conf.sftp_url, 22))
        transport.connect(username=conf.sftp_username, password=conf.sftp_password)
        channel = transport.open_session()
        channel.settimeout(timeout)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.get(remote_path_asc, local_path)
        transport.close()
    except Exception as e:
        # noinspection PyBroadException
        try:
            transport.close()
        except:
            pass
        # TODO customized exceptions

        raise Exception('fail to get %s' % e.message)
    return local_path


def _get_file_str_from_sftp(filename, conf, timeout):
    """read file from server via sftp

    Args:
        filename: filename in outbound folder
        conf: An instance of utils.Configuration.
        timeout: Timeout in second for ssh connection for sftp.

    Returns:
        xml string
    """
    remote_path_asc = 'outbound/' + filename
    transport = ''
    try:
        # noinspection PyTypeChecker
        transport = paramiko.Transport((conf.sftp_url, 22))
        transport.connect(username=conf.sftp_username, password=conf.sftp_password)
        channel = transport.open_session()
        channel.settimeout(timeout)
        sftp = paramiko.SFTPClient.from_transport(transport)
        remote_file = sftp.open(remote_path_asc)
        return_str = remote_file.read()
        transport.close()
    except Exception as e:
        # noinspection PyBroadException
        try:
            transport.close()
        except:
            pass
        # TODO customized exceptions
        raise Exception('fail to get', e.message)

    if conf.print_xml:
        print('Batch response file content: \n', return_str)

    return return_str


def __check_file_exist_in_sftp(sftp, path):
    """ Check if path exist in server via sftp

    Args:
        sftp: An instance of sftp connection
        path: file path on server

    Returns:
        boolean
    """
    try:
        sftp.stat(path)
        return True
    except IOError:
        return False


def _save_str_file(xml_str, path, filename):
    """Save string to local system

    Args:
        xml_str: String
        path: path for file to save
        filename: filename

    Returns:
        file path that saved
    """
    if not filename:
        filename = 'Vantiv_Batch_XML_%s' % datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    file_path = os.path.join(path, '%s.xml' % filename)
    if not os.path.exists(path):
        os.makedirs(path)
    while os.path.exists(file_path):
        file_path = os.path.join(path, '%s_%s.xml' % (filename, datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")))
    with open(file_path, 'w') as request_xml_file:
        request_xml_file.write(xml_str)
    return file_path


def _create_batch_xml(transactions, conf):
    """Create litleRequest xml string

    Args:
        transactions: an instance of batch.Transactions.
        conf: An instance of utils.Configuration.

    Returns:
        litleRequest xml string
    """
    xml_str = '<?xml version="1.0" encoding="utf-8"?>'
    xml_str += '<litleRequest version="%s" xmlns="http://www.litle.com/schema" id="%s" numBatchRequests="%d">' \
               % (conf.VERSION, conf.id, transactions.num_transactions)

    authentication = litle_xml_fields.authentication()
    authentication.user = conf.user
    authentication.password = conf.password

    xml_str += _obj_to_xml_element(authentication)

    if transactions.is_rfr_request:
        xml_str += _obj_to_xml_element(transactions.transactions.pop())
    else:
        attributes_dict = transactions.attributes_dict
        attributes_str = ''
        for key in attributes_dict.keys():
            if attributes_dict[key]:
                attributes_str += ' %s ="%d"' % (key, attributes_dict[key])
        xml_str += '<batchRequest merchantId="%s"%s>' % (conf.merchantId, attributes_str)
        trans_set = transactions.transactions
        while trans_set:
            xml_str += _obj_to_xml_element(trans_set.pop())
        xml_str += '</batchRequest>'
    xml_str += '</litleRequest>'

    if conf.print_xml:
        print('Batch request XML:\n', xml_str)

    return xml_str


def _obj_to_xml_element(obj):
    """Convert obj to xml

    Args:
        obj: Object

    Returns:
        xml string
    """
    xml = utils.obj_to_xml(obj)
    xml = xml.replace('<?xml version="1.0" encoding="utf-8"?>', '')
    xml = xml.replace(' xmlns="http://www.litle.com/schema"', '')
    return xml


class Transactions(object):
    """Container class for all transactions for batch

    """
    _RFRRequest = False
    _transactions = set()
    _cls_attribute = {}

    @property
    def is_rfr_request(self):
        return self._RFRRequest

    @property
    def transactions(self):
        # The purpose to do this is to avoid giving directly access to _transactions
        return self._transactions.copy()

    @property
    def num_transactions(self):
        num = 0 if self._RFRRequest else len(self._transactions)
        return num

    @property
    def attributes_dict(self):
        attributes_dict = vars(self)
        attributes_dict.pop('_RFRRequest_cls_name', None)
        return attributes_dict

    def __init__(self):
        for key in _supported_transaction_types.keys():
            obj = getattr(litle_xml_fields, key)()
            typename = type(obj).__name__
            self._cls_attribute[typename] = _supported_transaction_types[key]
            for attr_name in _supported_transaction_types[key]:
                if attr_name != '':
                    self.__setattr__(attr_name, 0)
        obj = getattr(litle_xml_fields, 'RFRRequest')()
        self._RFRRequest_cls_name = type(obj).__name__

    def add(self, transaction):
        """Add transaction to the container class.

        Args:
            transaction: an instance of Transactions which could process by Batch.

        Returns:
            None
        """
        typename = type(transaction).__name__

        # A Batch should not exceed 20,000 transactions.
        if len(self._transactions) > 20000:
            raise Exception('A Batch should not exceed 20,000 transactions.')

        if self._RFRRequest_cls_name == typename:
            if self._RFRRequest:
                raise Exception('only can add one RFRRequest')
            else:
                if not self._transactions:
                    self._transactions.add(transaction)
                    self._RFRRequest = True
                else:
                    raise Exception('cannot mix transactions and RFRRequest')
        else:
            if typename in self._cls_attribute.keys() and not self._RFRRequest:
                if transaction not in self._transactions:
                    # Add transaction
                    self._transactions.add(transaction)
                    # increase num attribute if has
                    num_attr_name = self._cls_attribute[typename][0]
                    if num_attr_name:
                        setattr(self, num_attr_name, getattr(self, num_attr_name) + 1)
                    # increase amount attribute if has
                    amount_attr_name = self._cls_attribute[typename][1]
                    if amount_attr_name and hasattr(transaction, 'amount'):
                        setattr(self, amount_attr_name,
                                # getattr(self, amount_attr_name) + int(getattr(transaction, 'amount')) * 100)
                                getattr(self, amount_attr_name) + int(getattr(transaction, 'amount')))
                else:
                    raise Exception('duplicate transaction cannot be added to a batch')
            else:
                raise Exception('transaction cannot be added to a batch')
