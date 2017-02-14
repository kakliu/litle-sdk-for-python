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

import litle_xml_fields
from utils import http_post


def request(transaction, conf):
    """Send request to server.

    Args:
        transaction: An instance of transaction class
        conf: An instance of utils.Configuration

    Returns:
        An object for return xml.

    Raises:
        Vantiv Exceptions.
    """
    request_obj = _create_request_obj(transaction, conf)
    # TODO convert object to xml without default namespace gracefully.
    request_xml = request_obj.toxml('utf-8')
    request_xml = request_xml.replace('ns1:', '').replace(':ns1', '')

    response_xml = http_post(request_xml, conf)

    if conf.print_xml:
        print('\nRequest:\n', request_xml)
        print('\nResponse:\n', response_xml)

    response = litle_xml_fields.CreateFromDocument(response_xml)
    if response.response == '0':
        return response.transactionResponse
    else:
        # TODO Change to custom Vantiv Exception.
        raise Exception(response.message)


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
    request_obj = litle_xml_fields.litleOnlineRequest()
    request_obj.merchantId = conf.merchantId
    request_obj.version = conf._VERSION
    request_obj.merchantSdk = conf._MERCHANTSDK
    authentication = litle_xml_fields.authentication()
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
    if isinstance(transaction, litle_xml_fields.recurringTransactionType):
        request_obj.recurringTransaction = transaction
    else:
        request_obj.transaction = transaction
    return request_obj
