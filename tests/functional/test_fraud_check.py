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


class TestFraudCheck(unittest.TestCase):
    def test_force_capture_with_card(self):
        transaction = fields.fraudCheck()
        transaction.id = 'ThisIsID'
        advancedFraudChecks = fields.advancedFraudChecksType()
        advancedFraudChecks.threatMetrixSessionId = '123'
        transaction.advancedFraudChecks = advancedFraudChecks

        response = online.request(transaction, conf)
        self.assertEquals('pass', response.transactionResponse.advancedFraudResults.deviceReviewStatus)
        self.assertEquals(42, response.transactionResponse.advancedFraudResults.deviceReputationScore)


if __name__ == '__main__':
    unittest.main()
