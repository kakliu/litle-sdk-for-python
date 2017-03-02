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


class TestEcheckSale(unittest.TestCase):
    def test_simple_echeck_sale(self):
        transaction = fields.echeckSale()
        transaction.litleTxnId = 123456789101112
        transaction.amount = 12
        transaction.id = 'ThisIsID'

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)

    def test_echeck_sale_with_echeck(self):
        transaction = fields.echeckSale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        echeck = fields.echeck()
        echeck.accNum = '12345657890'
        echeck.routingNum = '123456789'
        echeck.checkNum = '123455'
        echeck.accType = 'Checking'
        transaction.echeckOrEcheckToken = echeck

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress
        transaction.shipToAddress = billtoaddress

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)

    def test_echeck_sale_with_token(self):
        transaction = fields.echeckSale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.id = 'ThisIsID'

        token = fields.echeckToken()
        token.litleToken = '1234565789012'
        token.routingNum = '123456789'
        token.accType = 'Checking'
        transaction.echeckOrEcheckToken = token

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)

    def test_echeck_sale_with_secoundary_amount_and_ccd(self):
        transaction = fields.echeckSale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.secondaryAmount = 50
        transaction.id = 'ThisIsID'

        echeck = fields.echeck()
        echeck.accNum = '12345657890'
        echeck.routingNum = '123456789'
        echeck.checkNum = '123455'
        echeck.accType = 'Checking'
        echeck.ccdPaymentInformation = '12345678901234567890123456789012345678901234567890123456789012345678901234567890'
        transaction.echeckOrEcheckToken = echeck

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)


    def test_echeck_sale_with_secoundary_amount_and_ccd_longer_80(self):
        transaction = fields.echeckSale()
        transaction.reportGroup = 'Planets'
        transaction.orderId = '12344'
        transaction.amount = 106
        transaction.orderSource = 'ecommerce'
        transaction.secondaryAmount = 50
        transaction.id = 'ThisIsID'

        echeck = fields.echeck()
        echeck.accNum = '12345657890'
        echeck.routingNum = '123456789'
        echeck.checkNum = '123455'
        echeck.accType = 'Checking'
        echeck.ccdPaymentInformation = '123456789012345678901234567890123456789012345678901234567890123456789012345678901'
        transaction.echeckOrEcheckToken = echeck

        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        self.assertRaises(Exception, online.request, transaction, conf)

if __name__ == '__main__':
    unittest.main()
