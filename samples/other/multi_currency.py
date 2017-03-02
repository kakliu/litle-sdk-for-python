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

# Initial Transaction.
transaction = fields.authorization()
transaction.orderId = '12344'
transaction.amount = 106
transaction.reportGroup = 'Planets'
transaction.orderSource = 'ecommerce'
transaction.id = 'ThisIsRequiredby11'

# Create cardType object
card = fields.cardType()
card.number = '375001010000003'
card.expDate = '0112'
card.cardValidationNum = '349'
card.type = 'VI'
# The type of card is cardType
transaction.card = card

# Notice that 1003 is a different merchant.  In our system, they could be setup for USD purchases
conf.merchantId = '1001'
# Send request to server and get response as object
response = online.request(transaction, conf)

# Print results
print('Message: %s' % response.transactionResponse.message)
print('LitleTransaction ID: %s' % response.transactionResponse.litleTxnId)

# Notice that 1003 is a different merchant.  In our system, they could be setup for CDN purchases
conf.merchantId = '1001'
# Send request to server and get response as object
response = online.request(transaction, conf)

# Print results
print('Message: %s' % response.transactionResponse.message)
print('LitleTransaction ID: %s' % response.transactionResponse.litleTxnId)

# Notice that 1003 is a different merchant.  In our system, they could be setup for YEN purchases
conf.merchantId = '1003'
# Send request to server and get response as object
response = online.request(transaction, conf)

# Print results
print('Message: %s' % response.transactionResponse.message)
print('LitleTransaction ID: %s' % response.transactionResponse.litleTxnId)

# Send request to server and get response as XML
# response = online.request(transaction, conf, 'xml')
# print('Get response as XML:\n %s' % response)

# In your sample, you can ignore this
if response.transactionResponse.message != 'Approved':
    raise Exception('the example does not give the right response')