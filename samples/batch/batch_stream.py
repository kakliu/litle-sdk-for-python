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
from __future__ import print_function

from litle_sdk_python import *

# Initial Configuration object. If you have saved configuration in '.vantiv_python_sdk.conf' at system environment
# variable: VANTIV_SDK_CONFIG or user home directory, the saved configuration will be automatically load.
conf = utils.Configuration()

# Configuration has following attributes:
# attributes = default value
# self.user = ''
# self.password = ''
# self.merchantId = ''
# self.reportGroup = 'Default Report Group'
# self.url = 'https://www.testlitle.com/sandbox/communicator/online'
# self.proxy = ''
# self.sftp_username = ''
# self.sftp_password = ''
# self.sftp_url = ''
# self.batch_requests_path = tempdir + '/vantiv_sdk_batch_request'
# self.batch_response_path = tempdir + '/vantiv_sdk_batch_response'
# self.fast_url = ''
# self.fast_ssl = True
# self.fast_port = ''
# self.print_xml = False
# self.id = ''

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
# Add transaction to container
transactions.add(authorization)

# Initial authorization
sale = fields.sale()
sale.orderId = '1'
sale.amount = 10010
sale.reportGroup = 'Planets'
sale.orderSource = 'ecommerce'
sale.card = card
sale.billtoaddress = billtoaddress
# Add transaction to container
transactions.add(sale)

# stream to Vaitiv eCommerce and get object as response
response = batch.stream(transactions, conf)

# Return as xml string
# response = batch.stream(transactions, conf, 'xml')

for batchresponse in response.batchResponse:
    for txn in batchresponse.transactionResponse:
        print('Message: %s' % txn.message)
        print('LitleTransaction ID: %s' % txn.litleTxnId)

# In your sample, you can ignore this
if response.message != 'Valid Format':
    raise Exception('the example does not give the right response')

# Example for RFRRequest
RFRRequest = fields.RFRRequest()
RFRRequest.litleSessionId = response.litleSessionId

# Initial Transactions container, because RFRRequest and batchRequest cannot be in same session file
transactions = batch.Transactions()
transactions.add(RFRRequest)

# stream to Vaitiv eCommerce and get object as response
response = batch.stream(transactions, conf)

for batchresponse in response.batchResponse:
    for txn in batchresponse.transactionResponse:
        print('Message: %s' % txn.message)
        print('LitleTransaction ID: %s' % txn.litleTxnId)

# In your sample, you can ignore this
if response.message != 'Valid Format':
    raise Exception('the example does not give the right response')