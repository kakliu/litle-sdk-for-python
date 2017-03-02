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

import pyxb

from litle_sdk_python import *

conf = utils.Configuration()


class TestAuth(unittest.TestCase):
    def test_simple_auth_with_card(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.id = 'thisisid'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response.transactionResponse.response)

    def test_simple_auth_with_android_pay(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'androidpay'
        authorization.id = 'thisisid'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ0K',
                          response.transactionResponse.androidpayResponse.cryptogram)

    def test_simple_auth_with_paypal(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.id = 'thisisid'

        paypal = fields.payPal()
        paypal.payerId = '1234'
        paypal.token = '1234'
        paypal.transactionId = '1234'
        authorization.paypal = paypal

        response = online.request(authorization, conf)
        self.assertEquals('000', response.transactionResponse.response)

    def test_simple_auth_with_applepay_and_secondary_amount(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.secondaryAmount = 50
        authorization.orderSource = 'ecommerce'
        authorization.id = 'thisisid'

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
        authorization.applepay = applepay

        response = online.request(authorization, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals(106, response.transactionResponse.applepayResponse.transactionAmount)

    def test_pos_without_capability_entrymod(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'

        pos = fields.pos()
        pos.cardholderId = 'pin'
        authorization.pos = pos

        card = fields.cardType()
        card.number = '4100000000000002'
        card.expDate = '1210'
        card.type = 'VI'
        card.pin = '2222'
        authorization.card = card

        self.assertRaises(utils.VantivException, online.request, authorization, conf)

    def test_account_update(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.id = 'thisisid'

        card = fields.cardType()
        card.number = '4100100000000000'
        card.expDate = '1210'
        card.type = 'VI'
        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('4100100000000000', response.transactionResponse.accountUpdater.originalCardInfo.number)

    def test_track_data(self):
        authorization = fields.authorization()
        authorization.id = 'AX54321678'
        authorization.reportGroup = 'RG27'
        authorization.orderId = '12z58743y1'
        authorization.amount = 12522
        authorization.orderSource = 'retail'

        billToAddress = fields.contact()
        billToAddress.zip = '95032'
        authorization.billToAddress = billToAddress

        card = fields.cardType()
        card.track = '%B40000001^Doe/JohnP^06041...?;40001=0604101064200?'
        authorization.card = card

        pos = fields.pos()
        pos.cardholderId = 'signature'
        pos.capability = 'magstripe'
        pos.entryMode = 'completeread'
        authorization.pos = pos

        response = online.request(authorization, conf)
        self.assertEquals('000', response.transactionResponse.response)

    def test_list_of_tax_amount(self):
        authorization = fields.authorization()
        authorization.id = '12345'
        authorization.reportGroup = 'Default'
        authorization.orderId = '67890'
        authorization.amount = 10000
        authorization.orderSource = 'ecommerce'

        detailTax = fields.detailTax()
        detailTax.taxAmount = 100
        detailTax2 = fields.detailTax()
        detailTax2.taxAmount = 200
        # pyxb cannot bind multi occurs item, have to use pyxb.BIND
        enhancedData = pyxb.BIND(detailTax, detailTax2)
        authorization.enhancedData = enhancedData

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response.transactionResponse.response)

    def test_auth_with_processing_type(self):
        authorization = fields.authorization()
        authorization.id = '12345'
        authorization.reportGroup = 'Default'
        authorization.orderId = '67890'
        authorization.amount = 10000
        authorization.orderSource = 'ecommerce'
        authorization.processingType = 'initialInstallment'
        authorization.originalNetworkTransactionId = '9876543210'
        authorization.originalTransactionAmount = 53698

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response.transactionResponse.response)

    def test_auth_with_wallet(self):
        authorization = fields.authorization()
        authorization.id = '12345'
        authorization.reportGroup = 'Default'
        authorization.orderId = '67890'
        authorization.amount = 10000
        authorization.orderSource = 'ecommerce'
        authorization.processingType = 'initialInstallment'
        authorization.originalNetworkTransactionId = '9876543210'
        authorization.originalTransactionAmount = 53698

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'
        authorization.card = card

        wallet = fields.wallet()
        wallet.walletSourceTypeId = '1'
        wallet.walletSourceType = 'VisaCheckout'
        authorization.wallet = wallet

        response = online.request(authorization, conf)
        self.assertEquals('63225578415568556365452427825', response.transactionResponse.networkTransactionId)

    def test_auth_with_wallet_and_card_suffix_response(self):
        authorization = fields.authorization()
        authorization.id = '12345'
        authorization.reportGroup = 'Default'
        authorization.orderId = '67890'
        authorization.amount = 10000
        authorization.orderSource = 'ecommerce'
        authorization.processingType = 'initialInstallment'
        authorization.originalNetworkTransactionId = '9876543210'
        authorization.originalTransactionAmount = 53698

        card = fields.cardType()
        card.number = '5400700000000000'
        card.expDate = '1215'
        card.type = 'MC'
        authorization.card = card

        wallet = fields.wallet()
        wallet.walletSourceTypeId = '1'
        wallet.walletSourceType = 'MasterPass'
        authorization.wallet = wallet

        response = online.request(authorization, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertIsNone(response.transactionResponse.networkTransactionId)


if __name__ == '__main__':
    unittest.main()
