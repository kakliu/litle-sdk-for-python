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
from __future__ import print_function

import os
import sys
import unittest

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

import certification_test_conf
from litle_sdk_python import *

conf = certification_test_conf.conf

if __name__ == '__main__':
    unittest.main()


class TestCertAuths(unittest.TestCase):
    def test_table_2_1_1_auth(self):
        # orderId 1
        transaction = fields.authorization()
        transaction.orderId = '1'
        transaction.amount = 10010
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        contact = fields.contact()
        contact.name = 'John & Mary Smith'
        contact.addressLine1 = '1 Main St.'
        contact.city = 'Burlington'
        contact.state = 'MA'
        contact.zip = '01803-3747'
        contact.country = 'USA'
        transaction.billToAddress = contact

        card = fields.cardType()
        card.number = '4457010000000009'
        card.expDate = '0121'
        card.cardValidationNum = '349'
        card.type = 'VI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)
        # TODO response.transactionResponse.authCode include extra space
        self.assertEquals('11111 ', response.transactionResponse.authCode)
        self.assertEquals('01', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('M', response.transactionResponse.fraudResult.cardValidationResult)

        # orderId 1A
        capture = fields.capture()
        capture.litleTxnId = response.transactionResponse.litleTxnId
        capture.id = 'ThisIsID'
        captureresponse = online.request(capture, conf)
        self.assertEquals('000', captureresponse.transactionResponse.response)
        self.assertEquals('Approved', captureresponse.transactionResponse.message)

        # orderId 1B
        credit = fields.credit()
        credit.id = 'ThisIsID'
        credit.litleTxnId = captureresponse.transactionResponse.litleTxnId
        creditresponse = online.request(credit, conf)
        self.assertEquals('000', creditresponse.transactionResponse.response)
        self.assertEquals('Approved', creditresponse.transactionResponse.message)

        # orderId 1C
        void = fields.void()
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = online.request(void, conf)
        self.assertEquals('000', voidresponse.transactionResponse.response)
        self.assertEquals('Approved', voidresponse.transactionResponse.message)

    def test_table_2_1_1_avs(self):

        # orderId 1
        transaction = fields.authorization()
        transaction.orderId = '1'
        transaction.amount = 000
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        contact = fields.contact()
        contact.name = 'John & Mary Smith'
        contact.addressLine1 = '1 Main St.'
        contact.city = 'Burlington'
        contact.state = 'MA'
        contact.zip = '01803-3747'
        contact.country = 'USA'
        transaction.billToAddress = contact

        card = fields.cardType()
        card.number = '4457010000000009'
        card.expDate = '0121'
        card.cardValidationNum = '349'
        card.type = 'VI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)
        self.assertEquals('11111 ', response.transactionResponse.authCode)
        self.assertEquals('01', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('M', response.transactionResponse.fraudResult.cardValidationResult)

    def test_table_2_1_1_sale(self):
        # orderId 1
        transaction = fields.sale()
        transaction.orderId = '1'
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
        card.number = '4457010000000009'
        card.expDate = '0121'
        card.cardValidationNum = '349'
        card.type = 'VI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)
        self.assertEquals('11111 ', response.transactionResponse.authCode)
        self.assertEquals('01', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('M', response.transactionResponse.fraudResult.cardValidationResult)

        # orderId 1B
        credit = fields.credit()
        credit.id = 'thisisid'
        credit.litleTxnId = response.transactionResponse.litleTxnId
        creditresponse = online.request(credit, conf)
        self.assertEquals('000', creditresponse.transactionResponse.response)
        self.assertEquals('Approved', creditresponse.transactionResponse.message)

        # orderId 1C
        void = fields.void()
        void.id = 'thisisid'
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = online.request(void, conf)
        self.assertEquals('000', voidresponse.transactionResponse.response)
        self.assertEquals('Approved', voidresponse.transactionResponse.message)

    def test_table_2_1_2_auth(self):
        # orderId 2
        transaction = fields.authorization()
        transaction.orderId = '2'
        transaction.amount = 10100
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
        card.number = '5112010000000003'
        card.expDate = '0221'
        card.cardValidationNum = '261'
        card.type = 'MC'
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

        # orderId 2A
        capture = fields.capture()
        capture.id = 'thisisid'
        capture.litleTxnId = response.transactionResponse.litleTxnId
        captureresponse = online.request(capture, conf)
        self.assertEquals('000', captureresponse.transactionResponse.response)
        self.assertEquals('Approved', captureresponse.transactionResponse.message)

        # orderId 2B
        credit = fields.credit()
        credit.id = 'thisisid'
        credit.litleTxnId = captureresponse.transactionResponse.litleTxnId
        creditresponse = online.request(credit, conf)
        self.assertEquals('000', creditresponse.transactionResponse.response)
        self.assertEquals('Approved', creditresponse.transactionResponse.message)

        # orderId 2C
        void = fields.void()
        void.id = 'thisisid'
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = online.request(void, conf)
        self.assertEquals('000', voidresponse.transactionResponse.response)
        self.assertEquals('Approved', voidresponse.transactionResponse.message)

    def test_table_2_1_2_avs(self):
        # orderId 2
        transaction = fields.authorization()
        transaction.orderId = '2'
        transaction.amount = 000
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
        card.number = '5112010000000003'
        card.expDate = '0221'
        card.cardValidationNum = '261'
        card.type = 'MC'
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

    def test_table_2_1_2_sale(self):
        # orderId 2
        transaction = fields.sale()
        transaction.orderId = '2'
        transaction.amount = 10100
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
        card.number = '5112010000000003'
        card.expDate = '0221'
        card.cardValidationNum = '261'
        card.type = 'MC'
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
        # capture = fields.capture()
        # capture.litleTxnId = response.transactionResponse.litleTxnId
        # captureresponse = online.request(capture, conf)
        # self.assertEquals('000', captureresponse.transactionResponse.response)
        # self.assertEquals('Approved', captureresponse.transactionResponse.message)

        # orderId *B
        credit = fields.credit()
        credit.id = 'thisisid'
        credit.litleTxnId = response.transactionResponse.litleTxnId
        creditresponse = online.request(credit, conf)
        self.assertEquals('000', creditresponse.transactionResponse.response)
        self.assertEquals('Approved', creditresponse.transactionResponse.message)

        # orderId *C
        void = fields.void()
        credit.id = 'thisisid'
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = online.request(void, conf)
        self.assertEquals('000', voidresponse.transactionResponse.response)
        self.assertEquals('Approved', voidresponse.transactionResponse.message)

    def test_table_2_1_3_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '3'
        transaction.amount = 10010
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
        capture = fields.capture()
        capture.id = 'thisisid'
        capture.litleTxnId = response.transactionResponse.litleTxnId
        captureresponse = online.request(capture, conf)
        self.assertEquals('000', captureresponse.transactionResponse.response)
        self.assertEquals('Approved', captureresponse.transactionResponse.message)

        # orderId *B
        credit = fields.credit()
        credit.id = 'thisisid'
        credit.litleTxnId = captureresponse.transactionResponse.litleTxnId
        creditresponse = online.request(credit, conf)
        self.assertEquals('000', creditresponse.transactionResponse.response)
        self.assertEquals('Approved', creditresponse.transactionResponse.message)

        # orderId *C
        void = fields.void()
        void.id = 'thisisid'
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = online.request(void, conf)
        self.assertEquals('000', voidresponse.transactionResponse.response)
        self.assertEquals('Approved', voidresponse.transactionResponse.message)

    def test_table_2_1_3_avs(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '3'
        transaction.amount = 000
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

    def test_table_2_1_3_sale(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '3'
        transaction.amount = 10010
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
        capture = fields.capture()
        capture.id = 'thisisid'
        capture.litleTxnId = response.transactionResponse.litleTxnId
        captureresponse = online.request(capture, conf)
        self.assertEquals('000', captureresponse.transactionResponse.response)
        self.assertEquals('Approved', captureresponse.transactionResponse.message)

        # orderId *B
        credit = fields.credit()
        credit.id = 'thisisid'
        credit.litleTxnId = captureresponse.transactionResponse.litleTxnId
        creditresponse = online.request(credit, conf)
        self.assertEquals('000', creditresponse.transactionResponse.response)
        self.assertEquals('Approved', creditresponse.transactionResponse.message)

        # orderId *C
        void = fields.void()
        void.id = 'thisisid'
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = online.request(void, conf)
        self.assertEquals('000', voidresponse.transactionResponse.response)
        self.assertEquals('Approved', voidresponse.transactionResponse.message)

    def test_table_2_1_4_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '4'
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
        captureresponse = online.request(capture, conf)
        self.assertEquals('000', captureresponse.transactionResponse.response)
        self.assertEquals('Approved', captureresponse.transactionResponse.message)

        # orderId *B
        credit = fields.credit()
        credit.id = 'thisisid'
        credit.litleTxnId = captureresponse.transactionResponse.litleTxnId
        creditresponse = online.request(credit, conf)
        self.assertEquals('000', creditresponse.transactionResponse.response)
        self.assertEquals('Approved', creditresponse.transactionResponse.message)

        # orderId *C
        void = fields.void()
        void.id = 'thisisid'
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = online.request(void, conf)
        self.assertEquals('000', voidresponse.transactionResponse.response)
        self.assertEquals('Approved', voidresponse.transactionResponse.message)

    def test_table_2_1_4_avs(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '4'
        transaction.amount = 000
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
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)
        self.assertEquals('44444 ', response.transactionResponse.authCode)
        self.assertEquals('13', response.transactionResponse.fraudResult.avsResult)

    def test_table_2_1_4_sale(self):
        # orderId *
        transaction = fields.sale()
        transaction.orderId = '4'
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
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)
        self.assertEquals('44444 ', response.transactionResponse.authCode)
        self.assertEquals('13', response.transactionResponse.fraudResult.avsResult)

        # orderId *A
        capture = fields.capture()
        capture.id = 'thisisid'
        capture.litleTxnId = response.transactionResponse.litleTxnId
        captureresponse = online.request(capture, conf)
        self.assertEquals('000', captureresponse.transactionResponse.response)
        self.assertEquals('Approved', captureresponse.transactionResponse.message)

        # orderId *B
        credit = fields.credit()
        credit.id = 'thisisid'
        credit.litleTxnId = captureresponse.transactionResponse.litleTxnId
        creditresponse = online.request(credit, conf)
        self.assertEquals('000', creditresponse.transactionResponse.response)
        self.assertEquals('Approved', creditresponse.transactionResponse.message)

    def test_table_2_1_5_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '5'
        transaction.amount = 10010
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.number = '4100200300011001'
        card.expDate = '0521'
        card.type = 'VI'
        card.cardValidationNum = '463'
        transaction.card = card

        cardholderauthentication = fields.fraudCheckType()
        cardholderauthentication.authenticationValue = 'BwABBJQ1AgAAAAAgJDUCAAAAAAA='
        # TODO <message>3-D Secure transaction not supported by merchant</message>
        # transaction.cardholderAuthentication = cardholderauthentication

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)
        self.assertEquals('55555 ', response.transactionResponse.authCode)
        self.assertEquals('32', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('M', response.transactionResponse.fraudResult.cardValidationResult)

        # orderId *A
        capture = fields.capture()
        capture.id = 'thisisid'
        capture.litleTxnId = response.transactionResponse.litleTxnId
        captureresponse = online.request(capture, conf)
        self.assertEquals('000', captureresponse.transactionResponse.response)
        self.assertEquals('Approved', captureresponse.transactionResponse.message)

        # orderId *B
        credit = fields.credit()
        credit.id = 'thisisid'
        credit.litleTxnId = captureresponse.transactionResponse.litleTxnId
        creditresponse = online.request(credit, conf)
        self.assertEquals('000', creditresponse.transactionResponse.response)
        self.assertEquals('Approved', creditresponse.transactionResponse.message)

        # orderId *C
        void = fields.void()
        void.id = 'thisisid'
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = online.request(void, conf)
        self.assertEquals('000', voidresponse.transactionResponse.response)
        self.assertEquals('Approved', voidresponse.transactionResponse.message)

    def test_table_2_1_5_avs(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '5'
        transaction.amount = 000
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.number = '4100200300011001'
        card.expDate = '0521'
        card.type = 'VI'
        card.cardValidationNum = '463'
        transaction.card = card

        cardholderauthentication = fields.fraudCheckType()
        cardholderauthentication.authenticationValue = 'BwABBJQ1AgAAAAAgJDUCAAAAAAA='
        # TODO <message>3-D Secure transaction not supported by merchant</message>
        # transaction.cardholderAuthentication = cardholderauthentication

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)
        self.assertEquals('55555 ', response.transactionResponse.authCode)
        self.assertEquals('32', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('M', response.transactionResponse.fraudResult.cardValidationResult)

    def test_table_2_1_5_sale(self):
        # orderId *
        transaction = fields.sale()
        transaction.orderId = '5'
        transaction.amount = 10010
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.number = '4100200300011001'
        card.expDate = '0521'
        card.type = 'VI'
        card.cardValidationNum = '463'
        transaction.card = card

        cardholderauthentication = fields.fraudCheckType()
        cardholderauthentication.authenticationValue = 'BwABBJQ1AgAAAAAgJDUCAAAAAAA='
        # TODO <message>3-D Secure transaction not supported by merchant</message>
        # transaction.cardholderAuthentication = cardholderauthentication

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)
        self.assertEquals('55555 ', response.transactionResponse.authCode)
        self.assertEquals('32', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('M', response.transactionResponse.fraudResult.cardValidationResult)

        # orderId *B
        credit = fields.credit()
        credit.id = 'thisisid'
        credit.litleTxnId = response.transactionResponse.litleTxnId
        creditresponse = online.request(credit, conf)
        self.assertEquals('000', creditresponse.transactionResponse.response)
        self.assertEquals('Approved', creditresponse.transactionResponse.message)

        # orderId *C
        void = fields.void()
        void.id = 'thisisid'
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = online.request(void, conf)
        self.assertEquals('000', voidresponse.transactionResponse.response)
        self.assertEquals('Approved', voidresponse.transactionResponse.message)

    def test_table_2_1_6_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '6'
        transaction.amount = 10010
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        contact = fields.contact()
        contact.name = 'Joe Green'
        contact.addressLine1 = '6 Main St.'
        contact.city = 'Derry'
        contact.state = 'NH'
        contact.zip = '03038'
        contact.country = 'US'
        transaction.billToAddress = contact

        card = fields.cardType()
        card.number = '4457010100000008'
        card.expDate = '0621'
        card.cardValidationNum = '992'
        card.type = 'VI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('110', response.transactionResponse.response)
        self.assertEquals('Insufficient Funds', response.transactionResponse.message)
        self.assertEquals('34', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('P', response.transactionResponse.fraudResult.cardValidationResult)

    def test_table_2_1_6_sale(self):
        # orderId *
        transaction = fields.sale()
        transaction.orderId = '6'
        transaction.amount = 10010
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        contact = fields.contact()
        contact.name = 'Joe Green'
        contact.addressLine1 = '6 Main St.'
        contact.city = 'Derry'
        contact.state = 'NH'
        contact.zip = '03038'
        contact.country = 'US'
        transaction.billToAddress = contact

        card = fields.cardType()
        card.number = '4457010100000008'
        card.expDate = '0621'
        card.cardValidationNum = '992'
        card.type = 'VI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('110', response.transactionResponse.response)
        self.assertEquals('Insufficient Funds', response.transactionResponse.message)
        self.assertEquals('34', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('P', response.transactionResponse.fraudResult.cardValidationResult)

        # orderId *A
        void = fields.void()
        void.id = 'thisisid'
        void.litleTxnId = response.transactionResponse.litleTxnId
        voidresponse = online.request(void, conf)
        self.assertEquals('360', voidresponse.transactionResponse.response)
        self.assertEquals('No transaction found with specified litleTxnId', voidresponse.transactionResponse.message)

    def test_table_2_1_7_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '7'
        transaction.amount = 10010
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        contact = fields.contact()
        contact.name = 'Jane Murray'
        contact.addressLine1 = '7 Main St.'
        contact.city = 'Amesbury'
        contact.state = 'MA'
        contact.zip = '01913'
        contact.country = 'US'
        transaction.billToAddress = contact

        card = fields.cardType()
        card.number = '5112010100000002'
        card.expDate = '0721'
        card.cardValidationNum = '251'
        card.type = 'MC'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('301', response.transactionResponse.response)
        self.assertEquals('Invalid Account Number', response.transactionResponse.message)
        self.assertEquals('34', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('N', response.transactionResponse.fraudResult.cardValidationResult)

    def test_table_2_1_7_avs(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '7'
        transaction.amount = 000
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        contact = fields.contact()
        contact.name = 'Jane Murray'
        contact.addressLine1 = '7 Main St.'
        contact.city = 'Amesbury'
        contact.state = 'MA'
        contact.zip = '01913'
        contact.country = 'US'
        transaction.billToAddress = contact

        card = fields.cardType()
        card.number = '5112010100000002'
        card.expDate = '0721'
        card.cardValidationNum = '251'
        card.type = 'MC'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('301', response.transactionResponse.response)
        self.assertEquals('Invalid Account Number', response.transactionResponse.message)
        self.assertEquals('34', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('N', response.transactionResponse.fraudResult.cardValidationResult)

    def test_table_2_1_7_sale(self):
        # orderId *
        transaction = fields.sale()
        transaction.orderId = '7'
        transaction.amount = 10010
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        contact = fields.contact()
        contact.name = 'Jane Murray'
        contact.addressLine1 = '7 Main St.'
        contact.city = 'Amesbury'
        contact.state = 'MA'
        contact.zip = '01913'
        contact.country = 'US'
        transaction.billToAddress = contact

        card = fields.cardType()
        card.number = '5112010100000002'
        card.expDate = '0721'
        card.cardValidationNum = '251'
        card.type = 'MC'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('301', response.transactionResponse.response)
        self.assertEquals('Invalid Account Number', response.transactionResponse.message)
        self.assertEquals('34', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('N', response.transactionResponse.fraudResult.cardValidationResult)

    def test_table_2_1_8_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '8'
        transaction.amount = 10010
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        contact = fields.contact()
        contact.name = 'Mark Johnson'
        contact.addressLine1 = '8 Main St.'
        contact.city = 'Manchester'
        contact.state = 'NH'
        contact.zip = '03101'
        contact.country = 'US'
        transaction.billToAddress = contact

        card = fields.cardType()
        card.number = '6011010100000002'
        card.expDate = '0821'
        card.cardValidationNum = '184'
        card.type = 'DI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('123', response.transactionResponse.response)
        self.assertEquals('Call Discover', response.transactionResponse.message)
        self.assertEquals('34', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('P', response.transactionResponse.fraudResult.cardValidationResult)

    def test_table_2_1_8_avs(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '8'
        transaction.amount = 000
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        contact = fields.contact()
        contact.name = 'Mark Johnson'
        contact.addressLine1 = '8 Main St.'
        contact.city = 'Manchester'
        contact.state = 'NH'
        contact.zip = '03101'
        contact.country = 'US'
        transaction.billToAddress = contact

        card = fields.cardType()
        card.number = '6011010100000002'
        card.expDate = '0821'
        card.cardValidationNum = '184'
        card.type = 'DI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('123', response.transactionResponse.response)
        self.assertEquals('Call Discover', response.transactionResponse.message)
        self.assertEquals('34', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('P', response.transactionResponse.fraudResult.cardValidationResult)

    def test_table_2_1_8_sale(self):
        # orderId *
        transaction = fields.sale()
        transaction.orderId = '8'
        transaction.amount = 10010
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        contact = fields.contact()
        contact.name = 'Mark Johnson'
        contact.addressLine1 = '8 Main St.'
        contact.city = 'Manchester'
        contact.state = 'NH'
        contact.zip = '03101'
        contact.country = 'US'
        transaction.billToAddress = contact

        card = fields.cardType()
        card.number = '6011010100000002'
        card.expDate = '0821'
        card.cardValidationNum = '184'
        card.type = 'DI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('123', response.transactionResponse.response)
        self.assertEquals('Call Discover', response.transactionResponse.message)
        self.assertEquals('34', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('P', response.transactionResponse.fraudResult.cardValidationResult)

    def test_table_2_1_9_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '9'
        transaction.amount = 10010
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        contact = fields.contact()
        contact.name = 'James Miller'
        contact.addressLine1 = '9 Main St.'
        contact.city = 'Boston'
        contact.state = 'MA'
        contact.zip = '02134'
        contact.country = 'US'
        transaction.billToAddress = contact

        card = fields.cardType()
        card.number = '375001010000003'
        card.expDate = '0921'
        card.cardValidationNum = '0421'
        card.type = 'AX'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('303', response.transactionResponse.response)
        self.assertEquals('Pick Up Card', response.transactionResponse.message)
        self.assertEquals('34', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('P', response.transactionResponse.fraudResult.cardValidationResult)

    def test_table_2_1_9_avs(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '9'
        transaction.amount = 000
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        contact = fields.contact()
        contact.name = 'James Miller'
        contact.addressLine1 = '9 Main St.'
        contact.city = 'Boston'
        contact.state = 'MA'
        contact.zip = '02134'
        contact.country = 'US'
        transaction.billToAddress = contact

        card = fields.cardType()
        card.number = '375001010000003'
        card.expDate = '0921'
        card.cardValidationNum = '0421'
        card.type = 'AX'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('303', response.transactionResponse.response)
        self.assertEquals('Pick Up Card', response.transactionResponse.message)
        self.assertEquals('34', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('P', response.transactionResponse.fraudResult.cardValidationResult)

    def test_table_2_1_9_sale(self):
        # orderId *
        transaction = fields.sale()
        transaction.orderId = '9'
        transaction.amount = 10010
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        contact = fields.contact()
        contact.name = 'James Miller'
        contact.addressLine1 = '9 Main St.'
        contact.city = 'Boston'
        contact.state = 'MA'
        contact.zip = '02134'
        contact.country = 'US'
        transaction.billToAddress = contact

        card = fields.cardType()
        card.number = '375001010000003'
        card.expDate = '0921'
        card.cardValidationNum = '0421'
        card.type = 'AX'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('303', response.transactionResponse.response)
        self.assertEquals('Pick Up Card', response.transactionResponse.message)
        self.assertEquals('34', response.transactionResponse.fraudResult.avsResult)
        self.assertEquals('P', response.transactionResponse.fraudResult.cardValidationResult)

    def test_table_2_1_10_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '10'
        transaction.amount = 40000
        transaction.orderSource = 'ecommerce'

        card = fields.cardType()
        card.number = '4457010140000141'
        card.expDate = '0921'
        card.type = 'VI'
        transaction.card = card

        transaction.allowPartialAuth = True

        response = online.request(transaction, conf)
        self.assertEquals('010', response.transactionResponse.response)
        self.assertEquals('Partially Approved', response.transactionResponse.message)
        self.assertEquals(32000, response.transactionResponse.approvedAmount)

    def test_table_2_1_11_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '11'
        transaction.amount = 60000
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.number = '5112010140000004'
        card.expDate = '1121'
        card.type = 'MC'
        transaction.card = card

        transaction.allowPartialAuth = True

        response = online.request(transaction, conf)
        self.assertEquals('010', response.transactionResponse.response)
        self.assertEquals('Partially Approved', response.transactionResponse.message)
        self.assertEquals(48000, response.transactionResponse.approvedAmount)

    def test_table_2_1_12_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '12'
        transaction.amount = 50000
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.number = '375001014000009'
        card.expDate = '0421'
        card.type = 'AX'
        transaction.card = card

        transaction.allowPartialAuth = True

        response = online.request(transaction, conf)
        #self.assertEquals('010', response.transactionResponse.response)
        self.assertEquals('Partially Approved', response.transactionResponse.message)
        self.assertEquals(40000, response.transactionResponse.approvedAmount)

    def test_table_2_1_13_auth(self):
        # orderId *
        transaction = fields.authorization()
        transaction.orderId = '13'
        transaction.amount = 15000
        transaction.orderSource = 'ecommerce'
        transaction.id = 'thisisid'

        card = fields.cardType()
        card.number = '6011010140000004'
        card.expDate = '0821'
        card.type = 'DI'
        transaction.card = card

        transaction.allowPartialAuth = True

        response = online.request(transaction, conf)
        self.assertEquals('010', response.transactionResponse.response)
        self.assertEquals('Partially Approved', response.transactionResponse.message)
        self.assertEquals(12000, response.transactionResponse.approvedAmount)
