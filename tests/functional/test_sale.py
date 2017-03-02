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

conf = utils.Configuration()


class TestSale(unittest.TestCase):
    def test_simple_sale_with_card(self):
        transaction = fields.sale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)

    def test_simple_sale_with_paypal(self):
        transaction = fields.sale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        paypal = fields.payPal()
        paypal.payerId = '1234'
        paypal.token = '1234'
        paypal.transactionId = '123456'
        transaction.paypal = paypal

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)

    def test_simple_sale_with_applepay_and_secondary_amount(self):
        transaction = fields.sale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.secondaryAmount = 50
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        applepayHeaderType = fields.applepayHeaderType()
        applepayHeaderType.applicationData = '454657413164'
        applepayHeaderType.ephemeralPublicKey = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        applepayHeaderType.publicKeyHash = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        applepayHeaderType.transactionId = '1234'
        applepay = fields.applepayType()
        applepay.header = applepayHeaderType
        applepay.data = 'user'
        applepay.signature = 'sign'
        applepay.version = '12345'
        transaction.applepay = applepay

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals(106, response.transactionResponse.applepayResponse.transactionAmount)

    def test_simple_sale_with_android_pay(self):
        transaction = fields.sale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'androidpay'
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ0K',
                          response.transactionResponse.androidpayResponse.cryptogram)


    def test_simple_sale_with_token(self):
        transaction = fields.sale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        token = fields.cardTokenType()
        token.litleToken = '1111222233334000'
        token.expDate = '1210'
        token.cardValidationNum = '555'
        token.type = 'VI'
        transaction.token = token

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)


    def test_simple_sale_with_token(self):
        transaction = fields.sale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        token = fields.cardTokenType()
        token.litleToken = '1111222233334000'
        token.expDate = '1210'
        token.cardValidationNum = '555'
        token.type = 'VI'
        transaction.token = token

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        
    def test_sale_with_wallet(self):
        transaction = fields.sale()
        transaction.id = '12345'
        transaction.reportGroup = 'Default'
        transaction.orderId = '67890'
        transaction.amount = 10000
        transaction.orderSource = 'ecommerce'
        transaction.processingType = 'initialInstallment'
        transaction.originalNetworkTransactionId = '9876543210'
        transaction.originalTransactionAmount = 53698
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card

        wallet = fields.wallet()
        wallet.walletSourceTypeId = '1'
        wallet.walletSourceType = 'VisaCheckout'
        transaction.wallet = wallet

        response = online.request(transaction, conf)
        self.assertEquals('63225578415568556365452427825', response.transactionResponse.networkTransactionId)

    def test_sale_with_wallet_and_card_suffix_response(self):
        transaction = fields.sale()
        transaction.id = '12345'
        transaction.reportGroup = 'Default'
        transaction.orderId = '67890'
        transaction.amount = 10000
        transaction.orderSource = 'ecommerce'
        transaction.processingType = 'initialInstallment'
        transaction.originalNetworkTransactionId = '9876543210'
        transaction.originalTransactionAmount = 53698
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '5400700000000000'
        card.expDate = '1215'
        card.type = 'MC'
        transaction.card = card

        wallet = fields.wallet()
        wallet.walletSourceTypeId = '1'
        wallet.walletSourceType = 'MasterPass'
        transaction.wallet = wallet

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertIsNone(response.transactionResponse.networkTransactionId)

    def test_sale_with_processing_type(self):
        transaction = fields.sale()
        transaction.id = '12345'
        transaction.reportGroup = 'Default'
        transaction.orderId = '67890'
        transaction.amount = 10000
        transaction.orderSource = 'ecommerce'
        transaction.processingType = 'initialInstallment'
        transaction.originalNetworkTransactionId = '9876543210'
        transaction.originalTransactionAmount = 53698
        transaction.id = 'ThisIsID'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        transaction.card = card

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)


if __name__ == '__main__':
    unittest.main()
