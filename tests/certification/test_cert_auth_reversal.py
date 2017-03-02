# -*- coding: utf-8 -*-
# Copyright (c) 2017 Vantiv eCommerce
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the 'Software'), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import unittest
from litle_sdk_python import *
import certification_test_conf

conf = certification_test_conf.conf

if __name__ == '__main__':
    unittest.main()

class TestCertEcheck(unittest.TestCase):
    def test_table_2_4_32(self):
        # orderId 32
        transaction = fields.authorization()
        transaction.orderId = '32'
        transaction.amount = 10010
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        contact = fields.contact()
        contact.name = 'John Smith'
        contact.addressLine1 = '1 Main St.'
        contact.city = 'Burlington'
        contact.state = 'MA'
        contact.zip = '01803-3747'
        contact.country = 'USA'
        transaction.billToAddress = contact

        card = fields.cardType()
        card.type = 'VI'
        card.number = '4457010000000009'
        card.expDate = '0121'
        card.cardValidationNum = '349'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)
        self.assertEquals('11111 ', response.transactionResponse.authCode)
        self.assertEquals('01', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('M', response.transactionResponse.fraudResult.cardValidationResult)

        # orderId *A
        capture = fields.capture()
        capture.id = 'thisisid'
        capture.amount = 5050
        capture.litleTxnId = response.transactionResponse.litleTxnId
        captureresponse = online.request(capture, conf)
        self.assertEquals('000', captureresponse.transactionResponse.response)
        self.assertEquals('Approved', captureresponse.transactionResponse.message)

        # orderId *B
        # <litleOnlineResponse version="9.10" xmlns="http://www.litle.com/fields.
        #     response="0" message="Valid Format">
        #     <authReversalResponse reportGroup="Default Report Group">
        #         <litleTxnId>82919994641942281</litleTxnId>
        #         <orderId>32</orderId>
        #         <response>000</response>
        #         <responseTime>2017-02-21T17:53:54</responseTime>
        #         <postDate>2017-02-22</postDate>
        #         <message>Approved</message>
        #     </authReversalResponse>
        # </litleOnlineResponse>
        authreversal = fields.authReversal()
        authreversal.id = 'thisisid'
        authreversal.litleTxnId = response.transactionResponse.litleTxnId
        authreversalresponse = online.request(authreversal, conf)
        self.assertEquals('111', authreversalresponse.transactionResponse.response)
        self.assertEquals('Authorization amount has already been depleted',
                          authreversalresponse.transactionResponse.message)


    def test_table_2_3_33(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '33'
        transaction.amount = 20020
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        contact = fields.contact()
        contact.name = 'Mike J. Hammer'
        contact.addressLine1 = '2 Main St.'
        contact.addressLine2 = 'Apt. 222'
        contact.city = 'Riverside'
        contact.state = 'RI'
        contact.zip = '02915'
        contact.country = 'US'
        transaction.billToAddress = contact

        card = fields.cardType()
        card.type = 'MC'
        card.number = '5112010000000003'
        card.expDate = '0221'
        card.cardValidationNum = '261'
        transaction.card = card

        cardholderauthentication = fields.fraudCheckType()
        cardholderauthentication.authenticationValue = 'BwABBJQ1AgAAAAAgJDUCAAAAAAA='
        # TODO <message>3-D Secure transaction not supported by merchant</message>
        # transaction.cardholderAuthentication = cardholderauthentication

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)
        self.assertEquals('22222 ', response.transactionResponse.authCode)
        self.assertEquals('10', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('M', response.transactionResponse.fraudResult.cardValidationResult)
        self.assertRaises(response.transactionResponse.fraudResult.authenticationResult)

        # orderId *A
        authreversal = fields.authReversal()
        authreversal.id = 'thisisid'
        authreversal.litleTxnId = response.transactionResponse.litleTxnId
        authreversalresponse = online.request(authreversal, conf)
        self.assertEquals('000', authreversalresponse.transactionResponse.response)
        self.assertEquals('Approved', authreversalresponse.transactionResponse.message)


    def test_table_2_3_34(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '34'
        transaction.amount = 30030
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        contact = fields.contact()
        contact.name = 'Eileen Jones'
        contact.addressLine1 = '3 Main St.'
        contact.city = 'Bloomfield'
        contact.state = 'CT'
        contact.zip = '06002'
        contact.country = 'US'
        transaction.billToAddress = contact

        card = fields.cardType()
        card.number = '6011010000000003'
        card.expDate = '0321'
        card.cardValidationNum = '758'
        card.type = 'DI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)
        self.assertEquals('33333 ', response.transactionResponse.authCode)
        self.assertEquals('10', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('M', response.transactionResponse.fraudResult.cardValidationResult)

        # orderId *A
        authreversal = fields.authReversal()
        authreversal.id = 'thisisid'
        authreversal.litleTxnId = response.transactionResponse.litleTxnId
        authreversalresponse = online.request(authreversal, conf)
        self.assertEquals('000', authreversalresponse.transactionResponse.response)
        self.assertEquals('Approved', authreversalresponse.transactionResponse.message)


    def test_table_2_3_35(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '35'
        transaction.amount = 10010
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        contact = fields.contact()
        contact.name = 'Bob Black'
        contact.addressLine1 = '4 Main St.'
        contact.city = 'Laurel'
        contact.state = 'MD'
        contact.zip = '20708'
        contact.country = 'US'
        transaction.billToAddress = contact

        card = fields.cardType()
        card.number = '375001000000005'
        card.expDate = '0421'
        card.type = 'AX'
        transaction.card = card

        response = online.request(transaction, conf)
        # TODO <response>100</response><message>Processing Network Unavailable</message>
        # self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)
        self.assertEquals('44444 ', response.transactionResponse.authCode)
        self.assertEquals('13', response.transactionResponse.fraudResult.avsResult)

        # orderId *A
        capture = fields.capture()
        capture.id = 'thisisid'
        capture.litleTxnId = response.transactionResponse.litleTxnId
        capture.amount = 5050
        captureresponse = online.request(capture, conf)
        self.assertEquals('000', captureresponse.transactionResponse.response)
        self.assertEquals('Approved', captureresponse.transactionResponse.message)

        # orderId *B
        authreversal = fields.authReversal()
        authreversal.id = 'thisisid'
        authreversal.litleTxnId = response.transactionResponse.litleTxnId
        authreversal.amount = 5050
        authreversalresponse = online.request(authreversal, conf)
        self.assertEquals('336', authreversalresponse.transactionResponse.response)
        self.assertEquals('Reversal amount does not match Authorization amount',
                          authreversalresponse.transactionResponse.message)


    def test_table_2_3_36(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '36'
        transaction.amount = 20500
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.number = '375000026600004'
        card.expDate = '0521'
        card.type = 'AX'
        transaction.card = card

        response = online.request(transaction, conf)
        # TODO <response>100</response><message>Processing Network Unavailable</message>
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)

        # orderId *A
        authreversal = fields.authReversal()
        authreversal.id = 'thisisid'
        authreversal.litleTxnId = response.transactionResponse.litleTxnId
        authreversal.amount = 10000
        authreversalresponse = online.request(authreversal, conf)
        self.assertEquals('336', authreversalresponse.transactionResponse.response)
        self.assertEquals('Reversal amount does not match Authorization amount',
                          authreversalresponse.transactionResponse.message)


