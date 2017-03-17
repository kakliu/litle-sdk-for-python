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

import os
import sys
import unittest

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

from vantivsdk import *

import datetime

conf = utils.Configuration()


class TestBatch(unittest.TestCase):
    def test_batch_submit(self):
        # Initial Transactions container
        transactions = batch.Transactions()

        # Card
        card = fields.cardType()
        card.number = '4457010000000009'
        card.expDate = '0121'
        card.cardValidationNum = '349'
        card.type = 'VI'

        # eCheck
        echeck = fields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '4099999992'
        echeck.routingNum = '011075150'

        # billtoaddress
        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Mike'
        billtoaddress.middleInitial = 'J'
        billtoaddress.lastName = 'Hammer'
        billtoaddress.phone = '999-999-9999'

        # Initial authorization
        authorization = fields.authorization()
        authorization.orderId = '1'
        authorization.amount = 10010
        authorization.reportGroup = 'Planets'
        authorization.orderSource = 'ecommerce'
        authorization.card = card
        authorization.billtoaddress = billtoaddress
        authorization.id = 'thisisid'
        # Add transaction to container
        transactions.add(authorization)

        # Initial authorization
        authorization2 = fields.authorization()
        authorization2.orderId = '2'
        authorization2.amount = 1001
        authorization2.reportGroup = 'Planets'
        authorization2.orderSource = 'ecommerce'
        authorization2.card = card
        authorization2.billtoaddress = billtoaddress
        authorization2.id = 'thisisid'
        # Add transaction to container
        transactions.add(authorization2)

        # Initial authorization
        sale = fields.sale()
        sale.orderId = '1'
        sale.amount = 10010
        sale.reportGroup = 'Planets'
        sale.orderSource = 'ecommerce'
        sale.card = card
        sale.billtoaddress = billtoaddress
        sale.id = 'thisisid'
        # Add transaction to container
        transactions.add(sale)

        filename = 'batch_test_%s' % datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")

        # stream to Vaitiv eCommerce and get object as response
        response = batch.submit(transactions, conf, filename)

        with open(os.path.join(conf.batch_requests_path, '%s.xml' % filename), 'r') as xml_file:
            obj = fields.CreateFromDocument(xml_file.read())
            self.assertEquals(1, obj.numBatchRequests)
            self.assertEquals(11011, obj.batchRequest[0].authAmount)

        self.assertEquals('%s.xml.asc' % filename, response)

    def test_batch_stream_and_rfr(self):
        # Initial Transactions container
        transactions = batch.Transactions()

        # Card
        card = fields.cardType()
        card.number = '4457010000000009'
        card.expDate = '0121'
        card.cardValidationNum = '349'
        card.type = 'VI'

        # eCheck
        echeck = fields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '4099999992'
        echeck.routingNum = '011075150'

        # billtoaddress
        billtoaddress = fields.contact()
        billtoaddress.firstName = 'Mike'
        billtoaddress.middleInitial = 'J'
        billtoaddress.lastName = 'Hammer'
        billtoaddress.phone = '999-999-9999'

        # Initial authorization
        authorization = fields.authorization()
        authorization.orderId = '1'
        authorization.amount = 10010
        authorization.reportGroup = u'русский中文'
        authorization.orderSource = 'ecommerce'
        authorization.card = card
        authorization.billtoaddress = billtoaddress
        authorization.id = 'thisisid'
        # Add transaction to container
        transactions.add(authorization)

        # Initial authorization
        authorization2 = fields.authorization()
        authorization2.orderId = '2'
        authorization2.amount = 1001
        authorization2.reportGroup = 'Planets'
        authorization2.orderSource = 'ecommerce'
        authorization2.card = card
        authorization2.billtoaddress = billtoaddress
        authorization2.id = 'thisisid'
        # Add transaction to container
        transactions.add(authorization2)

        # Initial authorization
        sale = fields.sale()
        sale.orderId = '1'
        sale.amount = 10010
        sale.reportGroup = 'Planets'
        sale.orderSource = 'ecommerce'
        sale.card = card
        sale.billtoaddress = billtoaddress
        sale.id = 'thisisid'
        # Add transaction to container
        transactions.add(sale)

        # stream to Vaitiv eCommerce and get object as response
        response = batch.stream(transactions, conf)

        self.assertIn('batchResponse', response)

        # Example for RFRRequest
        RFRRequest = fields.RFRRequest()
        RFRRequest.litleSessionId = response['@litleSessionId']

        transactions = batch.Transactions()
        transactions.add(RFRRequest)

        # stream to Vaitiv eCommerce and get object as response
        response_rfr = batch.stream(transactions, conf)

        self.assertIn('batchResponse', response_rfr)
        self.assertEquals(response_rfr['batchResponse']['authorizationResponse'][0]['litleTxnId'],
                          response['batchResponse']['authorizationResponse'][0]['litleTxnId'])


if __name__ == '__main__':
    unittest.main()
