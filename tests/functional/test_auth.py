# -*- coding: utf-8 -*-
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

import unittest
from litle_sdk_python import *

conf = utils.Configuration()

class TestAuth(unittest.TestCase):
    def test_simple_auth_with_card(self):
        authorization = litle_xml_fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'

        card = litle_xml_fields.cardType()
        card.number = "4100000000000000"
        card.expDate = "1210"
        card.type = 'VI'

        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals("000", response.transactionResponse.response)


    def test_simple_auth_with_android_pay(self):
        authorization = litle_xml_fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'androidpay'

        card = litle_xml_fields.cardType()
        card.number = "4100000000000000"
        card.expDate = "1210"
        card.type = 'VI'

        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals("000", response.transactionResponse.response)
        self.assertEquals("aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ0K",
                          response.transactionResponse.androidpayResponse.cryptogram);


if __name__ == '__main__':
    unittest.main()
