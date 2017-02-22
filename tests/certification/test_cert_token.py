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

class TestCertToken(unittest.TestCase):
    def test_table_2_8_50(self):
        # orderId *
        transaction = litle_xml_fields.registerTokenRequest()
        transaction.orderId = '50'
        transaction.accountNumber = '4457119922390123'

        response = online.request(transaction, conf)
        self.assertEquals('0123', response.transactionResponse.litleToken[-4:])
        self.assertEquals('445711', response.transactionResponse.bin)
        self.assertEquals('VI', response.transactionResponse.type)
        self.assertEquals('801', response.transactionResponse.response)
        self.assertEquals('Account number was successfully registered', response.transactionResponse.message)

    def test_table_2_8_51(self):
        # orderId *
        transaction = litle_xml_fields.registerTokenRequest()
        transaction.orderId = '51'
        transaction.accountNumber = '4457119999999999'

        response = online.request(transaction, conf)
        self.assertRaises(response.transactionResponse.litleToken)
        self.assertEquals('820', response.transactionResponse.response)
        self.assertEquals('Credit card number was invalid', response.transactionResponse.message)


    def test_table_2_8_52(self):
        # orderId *
        transaction = litle_xml_fields.registerTokenRequest()
        transaction.orderId = '52'
        transaction.accountNumber = '4457119922390123'

        response = online.request(transaction, conf)
        self.assertEquals('0123', response.transactionResponse.litleToken[-4:])
        self.assertEquals('445711', response.transactionResponse.bin)
        self.assertEquals('VI', response.transactionResponse.type)
        self.assertEquals('802', response.transactionResponse.response)
        self.assertEquals('Account number was previously registered', response.transactionResponse.message)


    def test_table_2_8_53(self):
        # orderId *
        transaction = litle_xml_fields.registerTokenRequest()
        transaction.orderId = '53'

        echeckForToken = litle_xml_fields.echeckForTokenType()
        echeckForToken.accNum = "1099999998"
        echeckForToken.routingNum = "011100012"
        transaction.echeckForToken = echeckForToken

        response = online.request(transaction, conf)
        self.assertEquals('0123', response.transactionResponse.litleToken[-4:])
        self.assertEquals('EC', response.transactionResponse.type)
        self.assertEquals('998', response.transactionResponse.eCheckAccountSuffix)
        self.assertEquals('801', response.transactionResponse.response)
        self.assertEquals('Account number was previously registered', response.transactionResponse.message)


    def test_table_2_8_54(self):
        # orderId *
        transaction = litle_xml_fields.registerTokenRequest()
        transaction.orderId = '54'

        echeckForToken = litle_xml_fields.echeckForTokenType()
        echeckForToken.accNum = "1022222102"
        echeckForToken.routingNum = "1145_7895"
        transaction.echeckForToken = echeckForToken

        response = online.request(transaction, conf)
        self.assertEquals('900', response.transactionResponse.response)
        self.assertEquals('Invalid Bank Routing Number', response.transactionResponse.message)

    def test_table_2_9_55(self):
        # orderId *
        transaction = litle_xml_fields.authorization()
        transaction.orderId = '55'
        transaction.amount = 15000
        transaction.orderSource = 'ecommerce'

        card = litle_xml_fields.cardType()
        card.type = 'MC'
        card.number = '5435101234510196'
        card.expDate = '1121'
        card.cardValidationNum = '987'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)
        self.assertEquals('0196', response.transactionResponse.tokenResponse.litleToken[-4:])
        self.assertEquals('801', response.transactionResponse.tokenResponse.tokenResponseCode)
        self.assertEquals('Account number was previously registered',
                          response.transactionResponse.tokenResponse.tokenMessage)
        self.assertEquals('MC', response.transactionResponse.tokenResponse.type)
        self.assertEquals('543510', response.transactionResponse.tokenResponse.bin)

    def test_table_2_9_56(self):
        # orderId *
        transaction = litle_xml_fields.authorization()
        transaction.orderId = '56'
        transaction.amount = 15000
        transaction.orderSource = 'ecommerce'

        card = litle_xml_fields.cardType()
        card.type = 'MC'
        card.number = '5435109999999999'
        card.expDate = '1121'
        card.cardValidationNum = '987'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('301', response.transactionResponse.response)
        self.assertEquals('Invalid account number', response.transactionResponse.message)

    def test_table_2_9_57_58(self):
        # orderId 57
        transaction = litle_xml_fields.authorization()
        transaction.orderId = '57'
        transaction.amount = 15000
        transaction.orderSource = 'ecommerce'

        card = litle_xml_fields.cardType()
        card.type = 'MC'
        card.number = '5435101234510196'
        card.expDate = '1121'
        card.cardValidationNum = '987'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)
        self.assertEquals('0196', response.transactionResponse.tokenResponse.litleToken[-4:])
        self.assertEquals('802', response.transactionResponse.tokenResponse.tokenResponseCode)
        self.assertEquals('Account number was previously registered',
                          response.transactionResponse.tokenResponse.tokenMessage)
        self.assertEquals('MC', response.transactionResponse.tokenResponse.type)
        self.assertEquals('543510', response.transactionResponse.tokenResponse.bin)

        # orderId 58
        transaction = litle_xml_fields.authorization()
        transaction.orderId = '58'
        transaction.amount = 15000
        transaction.orderSource = 'ecommerce'

        token = litle_xml_fields.cardTokenType()
        token.litleToken = response.transactionResponse.tokenResponse.litleToken
        token.expDate = '1121'
        token.cardValidationNum = '987'
        transaction.token = token

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)

    def test_table_2_9_59(self):
        # orderId *
        transaction = litle_xml_fields.authorization()
        transaction.orderId = '59'
        transaction.amount = 15000
        transaction.orderSource = 'ecommerce'

        token = litle_xml_fields.cardTokenType()
        token.litleToken = '1111000100092332'
        token.expDate = '1121'
        transaction.token = token

        response = online.request(transaction, conf)
        self.assertEquals('822', response.transactionResponse.response)
        self.assertEquals('Token was not found', response.transactionResponse.message)

    def test_table_2_9_60(self):
        # orderId *
        transaction = litle_xml_fields.authorization()
        transaction.orderId = '60'
        transaction.amount = 15000
        transaction.orderSource = 'ecommerce'

        token = litle_xml_fields.cardTokenType()
        token.litleToken = '1112000100000085'
        token.expDate = '1121'
        transaction.token = token

        response = online.request(transaction, conf)
        self.assertEquals('823', response.transactionResponse.response)
        self.assertEquals('Token was invalid', response.transactionResponse.message)


    def test_table_2_9_61(self):
        # orderId *
        transaction = litle_xml_fields.echeckSale()
        transaction.orderId = '61'
        transaction.amount = 15000
        transaction.orderSource = 'ecommerce'

        billtoaddress = litle_xml_fields.contact()
        billtoaddress.firstName = 'Tom'
        billtoaddress.lastName = 'Black'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = litle_xml_fields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '1099999003'
        echeck.routingNum = '011100012'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertIsNotNone(response.transactionResponse.tokenResponse.litleToken)
        self.assertEquals('801', response.transactionResponse.tokenResponse.tokenResponseCode)
        self.assertEquals('Account number was successfully registered',
                          response.transactionResponse.tokenResponse.tokenMessage)
        self.assertEquals('EC', response.transactionResponse.tokenResponse.type)
        self.assertEquals('003', response.transactionResponse.tokenResponse.eCheckAccountSuffix)


    def test_table_2_9_62(self):
        # orderId *
        transaction = litle_xml_fields.echeckSale()
        transaction.orderId = '62'
        transaction.amount = 15000
        transaction.orderSource = 'ecommerce'

        billtoaddress = litle_xml_fields.contact()
        billtoaddress.firstName = 'Tom'
        billtoaddress.lastName = 'Black'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = litle_xml_fields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '1099999999'
        echeck.routingNum = '011100012'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertIsNotNone(response.transactionResponse.tokenResponse.litleToken)
        self.assertEquals('801', response.transactionResponse.tokenResponse.tokenResponseCode)
        self.assertEquals('Account number was successfully registered',
                          response.transactionResponse.tokenResponse.tokenMessage)
        self.assertEquals('EC', response.transactionResponse.tokenResponse.type)
        self.assertEquals('999', response.transactionResponse.tokenResponse.eCheckAccountSuffix)

    def test_table_2_9_63(self):
        # orderId *
        transaction = litle_xml_fields.echeckCredit()
        transaction.orderId = '63'
        transaction.amount = 15000
        transaction.orderSource = 'ecommerce'

        billtoaddress = litle_xml_fields.contact()
        billtoaddress.firstName = 'Tom'
        billtoaddress.lastName = 'Black'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = litle_xml_fields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '1099999999'
        echeck.routingNum = '011100012'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertIsNotNone(response.transactionResponse.tokenResponse.litleToken)
        self.assertEquals('801', response.transactionResponse.tokenResponse.tokenResponseCode)
        self.assertEquals('Account number was successfully registered',
                          response.transactionResponse.tokenResponse.tokenMessage)
        self.assertEquals('EC', response.transactionResponse.tokenResponse.type)
        self.assertEquals('999', response.transactionResponse.tokenResponse.eCheckAccountSuffix)


    def test_table_2_9_64(self):
        # orderId *
        transaction = litle_xml_fields.echeckSale()
        transaction.orderId = '64'
        transaction.amount = 15000
        transaction.orderSource = 'ecommerce'

        billtoaddress = litle_xml_fields.contact()
        billtoaddress.firstName = 'Tom'
        billtoaddress.lastName = 'Black'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = litle_xml_fields.echeck()
        echeck.accType = 'Corporate'
        echeck.accNum = '6099999993'
        echeck.routingNum = '211370545'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)

        self.assertEquals('Checking', response.transactionResponse.accountUpdater.originalTokenInfo.accType)
        self.assertEquals('11190000001003001', response.transactionResponse.accountUpdater.originalTokenInfo.litleToken)
        self.assertEquals('211370545', response.transactionResponse.accountUpdater.originalTokenInfo.routingNum)

        self.assertEquals('Checking', response.transactionResponse.accountUpdater.newTokenInfo.accType)
        self.assertEquals('11190000001003001', response.transactionResponse.accountUpdater.newTokenInfo.litleToken)
        self.assertEquals('211370545', response.transactionResponse.accountUpdater.newTokenInfo.routingNum)

        self.assertIsNotNone(response.transactionResponse.accountUpdater.newTokenInfo.litleToken)
        self.assertEquals('801', response.transactionResponse.accountUpdater.newTokenInfo.tokenResponseCode)
        self.assertEquals('Account number was successfully registered',
                          response.transactionResponse.accountUpdater.newTokenInfo.tokenMessage)
        self.assertEquals('EC', response.transactionResponse.accountUpdater.newTokenInfo.type)
        self.assertEquals('999', response.transactionResponse.accountUpdater.newTokenInfo.eCheckAccountSuffix)