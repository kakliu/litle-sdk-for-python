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

class TestCertEcheck(unittest.TestCase):
    def test_table_2_4_37(self):
        # orderId 37
        transaction = litle_xml_fields.echeckVerification()
        transaction.orderId = '37'
        transaction.amount = 3001
        transaction.orderSource = 'telephone'

        billtoaddress = litle_xml_fields.contact()
        billtoaddress.firstName = 'Tom'
        billtoaddress.lastName = 'Black'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = litle_xml_fields.echeck()
        echeck.accNum = '10@BC99999'
        echeck.accType = 'Checking'
        echeck.routingNum = '053100300'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('301', response.transactionResponse.response)
        self.assertEquals('Invalid Account Number', response.transactionResponse.message)


    def test_table_2_4_38(self):
        # orderId *
        transaction = litle_xml_fields.echeckVerification()
        transaction.orderId = '38'
        transaction.amount = 3002
        transaction.orderSource = 'telephone'

        billtoaddress = litle_xml_fields.contact()
        billtoaddress.firstName = 'John'
        billtoaddress.lastName = 'Smith'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = litle_xml_fields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '1099999999'
        echeck.routingNum = '011075150'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)


    def test_table_2_4_39(self):
        # orderId *
        transaction = litle_xml_fields.echeckVerification()
        transaction.orderId = '39'
        transaction.amount = 3003
        transaction.orderSource = 'telephone'

        billtoaddress = litle_xml_fields.contact()
        billtoaddress.firstName = 'Robert'
        billtoaddress.lastName = 'Jones'
        billtoaddress.companyName = 'Good Goods Inc'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = litle_xml_fields.echeck()
        echeck.accType = 'Corporate'
        echeck.accNum = '3099999999'
        echeck.routingNum = '053100300'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('950', response.transactionResponse.response)
        self.assertEquals('Decline - Negative Information on File', response.transactionResponse.message)


    def test_table_2_4_40(self):
        # orderId *
        transaction = litle_xml_fields.echeckVerification()
        transaction.orderId = '40'
        transaction.amount = 3004
        transaction.orderSource = 'telephone'

        billtoaddress = litle_xml_fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = litle_xml_fields.echeck()
        echeck.accType = 'Corporate'
        echeck.accNum = '8099999999'
        echeck.routingNum = '011075150'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('951', response.transactionResponse.response)
        self.assertEquals('Absolute Decline', response.transactionResponse.message)


    def test_table_2_6_41(self):
        # orderId *
        transaction = litle_xml_fields.echeckSale()
        transaction.orderId = '41'
        transaction.amount = 2008
        transaction.orderSource = 'telephone'

        billtoaddress = litle_xml_fields.contact()
        billtoaddress.firstName = 'Mike'
        billtoaddress.middleInitial = 'J'
        billtoaddress.lastName = 'Hammer'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = litle_xml_fields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '10@BC99999'
        echeck.routingNum = '053100300'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('301', response.transactionResponse.response)
        self.assertEquals('Invalid Account Number', response.transactionResponse.message)


    def test_table_2_6_42(self):
        # orderId *
        transaction = litle_xml_fields.echeckSale()
        transaction.orderId = '42'
        transaction.amount = 2004
        transaction.orderSource = 'telephone'

        billtoaddress = litle_xml_fields.contact()
        billtoaddress.firstName = 'Tom'
        billtoaddress.lastName = 'Black'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = litle_xml_fields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '4099999992'
        echeck.routingNum = '011075150'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)

        # eCheck Void
        transaction = litle_xml_fields.echeckVoid()
        transaction.litleTxnId = response.transactionResponse.litleTxnId

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)



    def test_table_2_6_43(self):
        # orderId *
        transaction = litle_xml_fields.echeckSale()
        transaction.orderId = '43'
        transaction.amount = 2007
        transaction.orderSource = 'telephone'

        billtoaddress = litle_xml_fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = litle_xml_fields.echeck()
        echeck.accType = 'Corporate'
        echeck.accNum = '6099999992'
        echeck.routingNum = '011075150'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)
        #TODO no accountUpdater element.


    def test_table_2_6_44(self):
        # orderId *
        transaction = litle_xml_fields.echeckSale()
        transaction.orderId = '44'
        transaction.amount = 2009
        transaction.orderSource = 'telephone'

        billtoaddress = litle_xml_fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = litle_xml_fields.echeck()
        echeck.accType = 'Corporate'
        echeck.accNum = '6099999992'
        echeck.routingNum = '053133052'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('900', response.transactionResponse.response)
        self.assertEquals('Invalid Bank Routing Number', response.transactionResponse.message)


    def test_table_2_7_45(self):
        # orderId *
        transaction = litle_xml_fields.echeckCredit()
        transaction.orderId = '45'
        transaction.amount = 1001
        transaction.orderSource = 'telephone'

        billtoaddress = litle_xml_fields.contact()
        billtoaddress.firstName = 'John'
        billtoaddress.lastName = 'Smith'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = litle_xml_fields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '10@BC99999'
        echeck.routingNum = '053100300'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('301', response.transactionResponse.response)
        self.assertEquals('Invalid Account Number', response.transactionResponse.message)


    def test_table_2_7_46(self):
        # orderId *
        transaction = litle_xml_fields.echeckCredit()
        transaction.orderId = '46'
        transaction.amount = 1003
        transaction.orderSource = 'telephone'

        billtoaddress = litle_xml_fields.contact()
        billtoaddress.firstName = 'Robert'
        billtoaddress.lastName = 'Jones'
        billtoaddress.companyName = 'Widget Inc'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = litle_xml_fields.echeck()
        echeck.accType = 'Corporate'
        echeck.accNum = '3099999999'
        echeck.routingNum = '011075150'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)

        # eCheck Void
        transaction = litle_xml_fields.echeckVoid()
        transaction.litleTxnId = response.transactionResponse.litleTxnId

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)


    def test_table_2_7_47(self):
        # orderId *
        transaction = litle_xml_fields.echeckCredit()
        transaction.orderId = '47'
        transaction.amount = 1007
        transaction.orderSource = 'telephone'

        billtoaddress = litle_xml_fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = litle_xml_fields.echeck()
        echeck.accType = 'Corporate'
        echeck.accNum = '6099999993'
        echeck.routingNum = '211370545'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)

    def test_table_2_6_48(self):
        # orderId *
        transaction = litle_xml_fields.echeckSale()
        transaction.orderId = '43'
        transaction.amount = 2007
        transaction.orderSource = 'telephone'

        billtoaddress = litle_xml_fields.contact()
        billtoaddress.firstName = 'Peter'
        billtoaddress.lastName = 'Green'
        billtoaddress.companyName = 'Green Co'
        billtoaddress.phone = '999-999-9999'
        transaction.billToAddress = billtoaddress

        echeck = litle_xml_fields.echeck()
        echeck.accType = 'Corporate'
        echeck.accNum = '6099999992'
        echeck.routingNum = '011075150'
        transaction.echeckOrEcheckToken = echeck

        response = online.request(transaction, conf)

        transaction = litle_xml_fields.echeckCredit()
        transaction.litleTxnId = response.transactionResponse.litleTxnId

        response = online.request(transaction, conf)
        self.assertEquals('000', response.transactionResponse.response)
        self.assertEquals('Approved', response.transactionResponse.message)


    def test_table_2_6_49(self):
        # orderId *
        transaction = litle_xml_fields.echeckCredit()
        transaction.litleTxnId = '2'

        response = online.request(transaction, conf)
        self.assertEquals('360', response.transactionResponse.response)
        self.assertEquals('No transaction found with specified litleTxnId', response.transactionResponse.message)

    def test_echeck_void_4(self):
        # orderId *
        transaction = litle_xml_fields.echeckVoid()
        transaction.litleTxnId = '2'

        response = online.request(transaction, conf)
        self.assertEquals('360', response.transactionResponse.response)
        self.assertEquals('No transaction found with specified litleTxnId', response.transactionResponse.message)