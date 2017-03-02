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

import requests

import fields
import utils

import re


def request(transaction, conf, return_format='object', timeout=30):
    """Send request to server.

    Args:
        transaction: An instance of transaction class
        conf: An instance of utils.Configuration
        return_format: Return format. The default is 'object'. Could be either 'object' or 'xml'.
        timeout: timeout for the request in seconds. timeout is not a time limit on the entire response.
        It's the time that server has not issued a response.

    Returns:
        response XML in desired format.

    Raises:
        Vantiv Exceptions.
    """
    if not (isinstance(transaction, fields.recurringTransactionType)
            or isinstance(transaction, fields.transactionType)):
        raise TypeError('transaction must be either litle_xml_fields.recurringTransactionType or transactionType')

    if not isinstance(conf, utils.Configuration):
        raise TypeError('conf must be an instance of utils.Configuration')

    request_xml = _create_request_xml(transaction, conf)
    response_xml = _http_post(request_xml, conf, timeout)
    response_code = utils.get_response_code(response_xml, 'litleOnlineResponse')

    if response_code == '0':
        if return_format.lower() == 'xml':
            return response_xml
        else:
            return fields.CreateFromDocument(response_xml)
    else:
        # Using pyxb to get
        msg = fields.CreateFromDocument(response_xml).message
        raise utils.VantivException(msg)


def _create_request_xml(transaction, conf):
    """Create xml string from transaction object

    Args:
        transaction: an instance of object, could be either recurringTransaction or transaction
        conf: an instance of utils.Configuration

    Returns:
        XML string
    """
    request_obj = _create_request_obj(transaction, conf)
    request_xml = utils.obj_to_xml(request_obj)

    if conf.print_xml:
        print('Request XML:\n', request_xml)

    return request_xml


def _create_request_obj(transaction, conf):
    """ Create <xs:element name="litleOnlineRequest">

    <xs:complexType name="baseRequest">
        <xs:sequence>
            <xs:element ref="xp:authentication" />
            <xs:choice>
                <xs:element ref="xp:transaction" />
                <xs:element ref="xp:recurringTransaction" />
            </xs:choice>
        </xs:sequence>
        <xs:attribute name="version" type="xp:versionType" use="required" />
    </xs:complexType>

    <xs:element name="litleOnlineRequest">
        <xs:complexType>
            <xs:complexContent>
                <xs:extension base="xp:baseRequest">
                    <xs:attribute name="merchantId" type="xp:merchantIdentificationType" use="required" />
                    <xs:attribute name="merchantSdk" type="xs:string" use="optional" />
                    <xs:attribute name="loggedInUser" type="xs:string" use="optional"/>
                </xs:extension>
            </xs:complexContent>
        </xs:complexType>
    </xs:element>

    Args:
        transaction: an instance of object, could be either recurringTransaction or transaction
        conf: an instance of utils.Configuration

    Returns:
        an instance of litleOnlineRequest object
    """
    request_obj = fields.litleOnlineRequest()
    request_obj.merchantId = conf.merchantId
    request_obj.version = conf.VERSION
    request_obj.merchantSdk = conf.MERCHANTSDK
    authentication = fields.authentication()
    authentication.user = conf.user
    authentication.password = conf.password
    request_obj.authentication = authentication
    if not transaction.reportGroup:
        transaction.reportGroup = conf.reportGroup
    # determine option for choice.
    # <xs:choice>
    #     <xs:element ref="xp:transaction" />
    #     <xs:element ref="xp:recurringTransaction" />
    # </xs:choice>
    if isinstance(transaction, fields.recurringTransactionType):
        request_obj.recurringTransaction = transaction
    else:
        request_obj.transaction = transaction
    return request_obj


def _http_post(post_data, conf, timeout):
    """Post xml to server via https using requests

    Args:
        timeout:
        post_data: Request XML String
        conf: Instances of Configuration

    Returns:
        XML string for server response.

    Raise:
        When can't communicate with server, Error with Https Request, Please Check Proxy and Url configuration
        When the server response code is not 200, Error with Https Response, Status code: xxx
    """
    headers = {'Content-type': 'application/xml'}
    proxies = {'https': conf.proxy} if (conf.proxy is not None and conf.proxy != '') else None
    try:
        response = requests.post(conf.url, data=post_data, headers=headers, proxies=proxies, timeout=timeout)
    except Exception as e:
        # TODO Change to custom Vantiv Exception.
        raise Exception("Error with Https Request, Please Check Proxy and Url configuration", e.message)
    if response.status_code != 200:
        # TODO Change to custom Vantiv Exception.
        raise Exception("Error with Https Response, Status code: ", response.status_code)

    if conf.print_xml:
        print('Response XML:\n', response.text, '\n')

    return response.text
