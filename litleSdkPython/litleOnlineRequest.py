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

import pyxb

import litleXmlFields
from Communications import *
from Configuration import *


class litleOnlineRequest:
    def __init__(self, conf=Configuration()):
        self.conf = conf

    def sendRequest(self, transaction):
        request_obj = self._create_txn_obj(transaction)
        request_xml = request_obj.toxml('utf-8')
        request_xml = request_xml.replace('ns1:', '').replace(':ns1', '')

        response_xml = Communications.http_post(request_xml, self.conf)

        if self.conf.printXml:
            print('\nRequest:\n', request_xml)
            print('\nResponse:\n', response_xml)

        response = litleXmlFields.CreateFromDocument(response_xml)
        if response.response == '0':
            return response.transactionResponse
        else:
            raise Exception(response.message)

    def _create_txn_obj(self, transaction):
        request_obj = litleXmlFields.litleOnlineRequest()
        request_obj.merchantId = self.conf.merchantId
        request_obj.version = self.conf.version
        request_obj.merchantSdk = self.conf.merchantSdk
        authentication = litleXmlFields.authentication()
        authentication.user = self.conf.user
        authentication.password = self.conf.password
        request_obj.authentication = authentication
        transaction.reportGroup = self.conf.reportGroup
        if isinstance(transaction, litleXmlFields.recurringTransactionType):
            request_obj.recurringTransaction = transaction
        else:
            request_obj.transaction = transaction
        return request_obj