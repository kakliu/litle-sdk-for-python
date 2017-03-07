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
from __future__ import absolute_import, division, print_function

import datetime
import os

import paramiko
import six
import xmltodict

from . import (fields, utils)

# Key: transaction name
# Value: array of batchRequest attributes according to transactions
_supported_transaction_types = {
    # '': ['numExtCaptures', 'extCaptureAmount'],
    'accountUpdate': ['numAccountUpdates', ''],
    'activate': ['numActivates', 'activateAmount'],
    'authorization': ['numAuths', 'authAmount'],
    'authReversal': ['numAuthReversals', 'authReversalAmount'],
    'balanceInquiry': ['numBalanceInquirys', ''],
    'cancelSubscription': ['numCancelSubscriptions', ''],
    'capture': ['numCaptures', 'captureAmount'],
    'captureGivenAuth': ['numCaptureGivenAuths', 'captureGivenAuthAmount'],
    'createPlan': ['numCreatePlans', ''],
    'credit': ['numCredits', 'creditAmount'],
    'deactivate': ['numDeactivates', ''],
    'echeckCredit': ['numEcheckCredit', 'echeckCreditAmount'],
    'echeckPreNoteCredit': ['numEcheckPreNoteCredit', ''],
    'echeckPreNoteSale': ['numEcheckPreNoteSale', ''],
    'echeckRedeposit': ['numEcheckRedeposit', ''],
    'echeckSale': ['numEcheckSales', 'echeckSalesAmount'],
    'echeckVerification': ['numEcheckVerification', 'echeckVerificationAmount'],
    'forceCapture': ['numForceCaptures', 'forceCaptureAmount'],
    'fundingInstructionVoid': ['numFundingInstructionVoid', ''],
    'load': ['numLoads', 'loadAmount'],
    'payFacCredit': ['numPayFacCredit', 'payFacCreditAmount'],
    'payFacDebit': ['numPayFacDebit', 'payFacDebitAmount'],
    'physicalCheckCredit': ['numPhysicalCheckCredit', 'physicalCheckCreditAmount'],
    'physicalCheckDebit': ['numPhysicalCheckDebit', 'physicalCheckDebitAmount'],
    'registerTokenRequest': ['numTokenRegistrations', ''],
    'reserveCredit': ['numReserveCredit', 'reserveCreditAmount'],
    'reserveDebit': ['numReserveDebit', 'reserveDebitAmount'],
    'sale': ['numSales', 'saleAmount'],
    'submerchantCredit': ['numSubmerchantCredit', 'submerchantCreditAmount'],
    'submerchantDebit': ['numSubmerchantDebit', 'submerchantDebitAmount'],
    'unload': ['numUnloads', 'unloadAmount'],
    'updateCardValidationNumOnToken': ['numUpdateCardValidationNumOnTokens', ''],
    'updatePlan': ['numUpdatePlans', ''],
    'updateSubscription': ['numUpdateSubscriptions', ''],
    'vendorCredit': ['numVendorCredit', 'vendorCreditAmount'],
    'vendorDebit': ['numVendorDebit', 'vendorDebitAmount'],
}

_batch_attributes_num_dict = dict()
_batch_attributes_amount_dict = dict()
for key in _supported_transaction_types:
    if _supported_transaction_types[key][0]:
        _batch_attributes_num_dict[_supported_transaction_types[key][0]] = 0
    if _supported_transaction_types[key][1]:
        _batch_attributes_amount_dict[_supported_transaction_types[key][1]] = 0

_class_transaction_dict = dict()
for key in _supported_transaction_types:
    obj = getattr(fields, key)()
    typename = type(obj).__name__
    _class_transaction_dict[typename] = _supported_transaction_types[key]


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
        raise utils.VantivException('transactions must be an instance of batch.Transactions')

    if len(transactions.transactions) < 1:
        raise utils.VantivException('transactions must have at least 1 transaction')

    if not isinstance(conf, utils.Configuration):
        raise utils.VantivException('conf must be an instance of utils.Configuration')

    if not isinstance(filename, six.string_types):
        raise utils.VantivException('filename must be a string')

    if not isinstance(timeout, six.integer_types) or timeout < 0:
        raise utils.VantivException('timeout must be an positive int')

    # 1. Generate litleRequest xml.
    xml_str = _create_batch_xml(transactions, conf)

    # 2. Save xml at local file system.
    file_path = _save_str_file(xml_str, conf.batch_requests_path, filename)

    # 3. Send xml file to server.
    remote_filename = _put_file_to_sftp(file_path, conf, timeout)
    return remote_filename


def download(filename, conf, delete_remote=False, timeout=60):
    """Download Processed Session File from server via sFTP

    Get xml file from server and save to local file system

    Args:
        filename: filename of file in outbound folder at remote server with '.asc' as extension.
        conf:  An instance of utils.Configuration.
        delete_remote: If delete the remote file after download. The default is False
        timeout: Timeout in second for ssh connection for sftp.

    Returns:
        path for file that saved in local file system.

    Raises:
        Exception depends on when get it.
    """
    if not isinstance(conf, utils.Configuration):
        raise utils.VantivException('conf must be an instance of utils.Configuration')

    if not isinstance(filename, six.string_types) or len(filename) < 4:
        raise utils.VantivException('filename must be a string, and at least 4 chars')

    if not isinstance(timeout, six.integer_types) or timeout < 0:
        raise utils.VantivException('timeout must be an positive int')

    return _get_file_from_sftp(filename, conf, delete_remote, timeout)


def retrieve(filename, conf, return_format='dict', save_to_local=False, delete_remote=False, timeout=60):
    """Retrieving Processed Session File from server via sFTP

    1. Get xml file string from server and return object
    2. If save_to_local, save to local file system

    Args:
        filename: filename of file in outbound folder at remote server with '.asc' as extension.
        conf:  An instance of utils.Configuration.
        return_format: Return format. The default is ‘dict’. Could be one of ‘dict’, ‘object’ or ‘xml’.
        save_to_local: whether save file to local. default is false.
        delete_remote: If delete the remote file after download. The default is False
        timeout: Timeout in second for ssh connection for sftp.

    Returns:
        response XML in desired format.

    Raises:
        Exception depends on when get it.
    """
    if not isinstance(conf, utils.Configuration):
        raise utils.VantivException('conf must be an instance of utils.Configuration')

    if not isinstance(filename, six.string_types) or len(filename) < 4:
        raise utils.VantivException('filename must be a string, and at least 4 chars')

    if not isinstance(timeout, six.integer_types) or timeout < 0:
        raise utils.VantivException('timeout must be an positive int')

    response_xml = _get_file_str_from_sftp(filename, conf, delete_remote, timeout)

    if save_to_local:
        _save_str_file(response_xml, conf.batch_response_path, filename)

    return _generate_response(response_xml, return_format, conf)


def stream(transactions, conf, return_format='dict', timeout_send=60, timeout_rev=2):
    """stream batch request to IBC (inbound batch communicator) via socket and get return object

    Args:
        transactions: an instance of batch.Transactions.
        conf: An instance of utils.Configuration.
        return_format: Return format. The default is ‘dict’. Could be one of ‘dict’, ‘object’ or ‘xml’.
        timeout_send: Positive int. Timeout in second for socket connection when sending.
        timeout_rev: Positive int. Timeout in second for socket connection when receiving.

    Returns:
        response XML in desired format.

    """
    if not isinstance(transactions, Transactions):
        raise utils.VantivException('transactions must be an instance of batch.Transactions')

    if len(transactions.transactions) < 1:
        raise utils.VantivException('transactions must have at least 1 transaction')

    if not isinstance(conf, utils.Configuration):
        raise utils.VantivException('conf must be an instance of utils.Configuration')

    if not isinstance(timeout_send, six.integer_types) or timeout_send < 0:
        raise utils.VantivException('timeout_send must be an positive int')

    if not isinstance(timeout_rev, six.integer_types) or timeout_rev < 0:
        raise utils.VantivException('timeout_rev must be an positive int')

    xml_str = _create_batch_xml(transactions, conf)
    response_xml = _stream_socket(xml_str, conf, timeout_send, timeout_rev)

    if not response_xml.strip():
        raise utils.VantivException('Cannot get response from vantiv, please tray again later.')

    return _generate_response(response_xml, return_format, conf)


def _generate_response(_response_xml, _return_format, conf):
    response_dict = xmltodict.parse(_response_xml)['litleResponse']
    if response_dict['@response'] == '0':
        return_f_l = _return_format.lower()
        if return_f_l == 'xml':
            return _response_xml
        elif return_f_l == 'object':
            return fields.CreateFromDocument(_response_xml)
        else:
            if conf.print_xml:
                import json
                print('Response Dict:\n', json.dumps(response_dict, indent=4), '\n\n')
            return response_dict
    else:
        raise utils.VantivException(response_dict['@message'])


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
        raise utils.VantivException("Cannot connect to vantiv")

    s.sendall(xml_str.encode())

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
            data = s.recv(4096)
            if data:
                str_array.append(data)
                # break when got litleResponse close tag
                if b'</litleResponse>' in data:
                    break
                start = time.time()
            else:
                time.sleep(0.1)
        except:
            pass

    s.close()

    return_str = b''.join(str_array)
    return_str = return_str.decode('utf-8')

    if conf.print_xml:
        print('Batch stream response XML: \n', return_str, '\n')

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
    except Exception:
        try:
            transport.close()
        except:
            pass
        raise utils.VantivException('Fail to send "%s" to Vantiv server.' % file_path)

    return os.path.basename(remote_path_asc)


def _get_file_from_sftp(filename, conf, delete_remote, timeout):
    """Download file from server via sftp

    Args:
        filename: filename in outbound folder
        conf: An instance of utils.Configuration.
        delete_remote: If delete the remote file after download.
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
        transport = paramiko.Transport((conf.sftp_url, 22))
        transport.connect(username=conf.sftp_username, password=conf.sftp_password)
        channel = transport.open_session()
        channel.settimeout(timeout)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.get(remote_path_asc, local_path)
        if delete_remote:
            sftp.remove(remote_path_asc)
        transport.close()
    except FileNotFoundError:
        try:
            transport.close()
        except:
            pass
        raise utils.VantivException('Cannot find file "%s" on Vantiv server.' % filename)
    return local_path


def _get_file_str_from_sftp(filename, conf, delete_remote, timeout):
    """read file from server via sftp

    Args:
        filename: filename in outbound folder
        conf: An instance of utils.Configuration.
        delete_remote: If delete the remote file after download.
        timeout: Timeout in second for ssh connection for sftp.

    Returns:
        xml string
    """
    remote_path_asc = 'outbound/' + filename
    transport = ''
    try:
        transport = paramiko.Transport((conf.sftp_url, 22))
        transport.connect(username=conf.sftp_username, password=conf.sftp_password)
        channel = transport.open_session()
        channel.settimeout(timeout)
        sftp = paramiko.SFTPClient.from_transport(transport)
        remote_file = sftp.open(remote_path_asc)
        return_str = remote_file.read()
        return_str = return_str.decode('utf-8')
        if delete_remote:
            sftp.remove(remote_path_asc)
        transport.close()
    except FileNotFoundError:
        try:
            transport.close()
        except:
            pass
        raise utils.VantivException('Cannot find file "%s" on Vantiv server.' % filename)

    if conf.print_xml:
        print('Batch response file content: \n', return_str, '\n')

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

    authentication = fields.authentication()
    authentication.user = conf.user
    authentication.password = conf.password

    txns = transactions.transactions

    request_str = ''
    num_batch_requests = 0
    if transactions.is_rfr_request:
        request_str += _obj_to_xml_element(txns[0])
    else:
        attributes_num_dict = _batch_attributes_num_dict.copy()
        attributes_amount_dict = _batch_attributes_amount_dict.copy()
        txn_count = 0
        txns_str = ''
        for txn in txns:
            # Add default reportGroup to txn
            if not txn.reportGroup:
                txn.reportGroup = conf.reportGroup
            txn_count += 1
            type_name = type(txn).__name__
            attributes_num_dict[_class_transaction_dict[type_name][0]] += 1
            if hasattr(txn, 'amount') and _class_transaction_dict[type_name][1]:
                attributes_amount_dict[_class_transaction_dict[type_name][1]] += int(getattr(txn, 'amount'))
            txns_str += _obj_to_xml_element(txn)
            if txn_count == 20000:
                attributes_str = ''
                for k in attributes_num_dict:
                    if attributes_num_dict[k]:
                        attributes_str += ' %s ="%d"' % (k, attributes_num_dict[k])
                for k in attributes_amount_dict:
                    if attributes_amount_dict[k]:
                        attributes_str += ' %s ="%d"' % (k, attributes_amount_dict[k])
                batch_request_str = '<batchRequest merchantId="%s"%s>' % (conf.merchantId, attributes_str)
                batch_request_str += txns_str
                batch_request_str += '</batchRequest>'
                request_str += batch_request_str
                num_batch_requests += 1
                txn_count = 0
                txns_str = ''
                attributes_num_dict = _batch_attributes_num_dict.copy()
                attributes_amount_dict = _batch_attributes_amount_dict.copy()
        if txn_count:
            attributes_str = ''
            for k in attributes_num_dict:
                if attributes_num_dict[k]:
                    attributes_str += ' %s ="%d"' % (k, attributes_num_dict[k])
            for k in attributes_amount_dict:
                if attributes_amount_dict[k]:
                    attributes_str += ' %s ="%d"' % (k, attributes_amount_dict[k])
            batch_request_str = '<batchRequest merchantId="%s"%s>' % (conf.merchantId, attributes_str)
            batch_request_str += txns_str
            batch_request_str += '</batchRequest>'
            request_str += batch_request_str
            num_batch_requests += 1

    xml_str = '<?xml version="1.0" encoding="utf-8"?>'
    xml_str += '<litleRequest version="%s" xmlns="http://www.litle.com/schema" id="%s" numBatchRequests="%d">' \
               % (conf.VERSION, conf.id, num_batch_requests)
    xml_str += _obj_to_xml_element(authentication)
    xml_str += request_str
    xml_str += '</litleRequest>'

    if conf.print_xml:
        print('Batch request XML:\n', xml_str, '\n')

    return xml_str


def _obj_to_xml_element(_obj):
    """Convert obj to xml

    Args:
        _obj: Object

    Returns:
        xml string
    """
    xml = utils.obj_to_xml(_obj)
    xml = xml.replace('<?xml version="1.0" encoding="utf-8"?>', '')
    xml = xml.replace(' xmlns="http://www.litle.com/schema"', '')
    return xml


class Transactions(object):
    """Container of transactions for batch request

    Then transactions could be RFRRequest and any batch request supported transactions and recurringTransaction.
    RFRRequest cannot exist in the same instance with any other transactions.

    A instance cannot contain more than 1,000,000 transactions.

    """

    @property
    def is_rfr_request(self):
        """A property, whether current instanc include a RFRRequest

        Returns:
            Boolean
        """
        return self._RFRRequest

    @property
    def transactions(self):
        """A property, return a new list of transactions.

        Returns:
            list of transactions
        """
        # The purpose to do this is to avoid giving directly access to _transactions
        return list(self._transactions)

    def __init__(self):
        self._RFRRequest = False
        self._transactions = set()
        obje = getattr(fields, 'RFRRequest')()
        self._RFRRequest_cls_name = type(obje).__name__

    def add(self, transaction):
        """Add transaction to the container class.

        Args:
            transaction: an instance of Transactions or RFRRequest which could process by Batch.

        Returns:
            None

        Raises:
            Exceptions.
        """

        # A Batch should not exceed 1,000,000 transactions.
        if len(self._transactions) > 1000000:
            raise utils.VantivException('A session should not exceed 1,000,000 transactions.')

        type_name = type(transaction).__name__
        if self._RFRRequest_cls_name == type_name:
            if self._RFRRequest:
                raise utils.VantivException('only can add one RFRRequest')
            else:
                if not self._transactions:
                    self._transactions.add(transaction)
                    self._RFRRequest = True
                else:
                    raise utils.VantivException('cannot mix transactions and RFRRequest')
        else:
            if self._RFRRequest:
                raise utils.VantivException('cannot mix transactions and RFRRequest')
            if typename in _class_transaction_dict:
                if transaction not in self._transactions:
                    # Add transaction
                    self._transactions.add(transaction)
                else:
                    raise utils.VantivException('duplicate transaction cannot be added to a batch')
            else:
                raise utils.VantivException('transaction not support by batch')
