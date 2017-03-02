Vantiv eCommerce Python SDK v2
==============================

About Vantiv eCommerce
----------------------
[Vantiv eCommerce](https://developer.vantiv.com/community/ecommerce) powers the payment processing engines for leading companies that sell directly to consumers through  internet retail, direct response marketing (TV, radio and telephone), and online services. Vantiv eCommerce is the leading authority in card-not-present (CNP) commerce, transaction processing and merchant services.


About this SDK
--------------
The Vantiv eCommerce Python SDK v2 is a Python implementation of the [Vantiv eCommerce](https://developer.vantiv.com/community/ecommerce) XML API. This SDK was created to make it as easy as possible to connect to and process payments through Vantiv eCommerce. This SDK utilizes the HTTPS protocol to securely connect to Vantiv eCommerce.  Using the SDK requires coordination with the Vantiv eCommerce team to obtain credentials for accessing our systems.

Each Python SDK release supports all of the functionality present in the associated Vantiv eCommerce XML version (e.g., SDK v9.3.2 supports Vantiv eCommerce XML v9.3). Please see the online copy of our XSD for Vantiv eCommerce XML to get more details on what the Vantiv eCommerce payments engine supports .

This SDK was implemented to support the Python programming language and was created by Vantiv eCommerce Its intended use is for online transaction processing utilizing your account on the Vantiv eCommerce payments engine.

See LICENSE file for details on using this software.

Source Code available from : https://github.com/LitleCo/litle-sdk-for-Python

Please contact [Vantiv eCommerce](https://developer.vantiv.com/community/ecommerce) to receive valid merchant credentials and determine which version of the SDK is right for your business requirements or if you require assistance in any other way.  You can reach us at sdksupport@Vantiv.com

Dependencies
------------
pyxb v1.2.5 : http://pyxb.sourceforge.net/
paramiko v1.14.0: http://www.paramiko.org/
requests v2.13.0: http://docs.python-requests.org/en/master/
six v1.10.0: https://github.com/benjaminp/six

Setup
-----
1) To download and install:

Using pip 

>pip install LitleSdkPython

Without Pip

>wget http://pypi.python.org/packages/source/L/LitleSdkPython/LitleSdkPython-8.13.0.tar.gz#md5=30c83ed753f37482ce5f04e84836a74d

>tar xf LitleSdkPython-VERSION.tar.gz

>cd LitleSdkPython-VERSION

>python setup.py install

2) setup configurations

>vantiv_python_sdk_setup

3) Create a python file similar to:

```python
from __future__ import print_function

from litle_sdk_python import *

# Initial Configuration object. If you have saved configuration in '.vantiv_python_sdk.conf' at system environment
# variable: VANTIV_SDK_CONFIG or user home directory, the saved configuration will be automatically load.
conf = utils.Configuration()

# Configuration has following attributes:
# attributes = default value
# user = ''
# password = ''
# merchantId = ''
# reportGroup = 'Default Report Group'
# url = 'https://www.testlitle.com/sandbox/communicator/online'
# proxy = ''
# sftp_username = ''
# sftp_password = ''
# sftp_url = ''
# batch_requests_path = tempdir + '/vantiv_sdk_batch_request'
# batch_response_path = tempdir + '/vantiv_sdk_batch_response'
# fast_url = ''
# fast_ssl = True
# fast_port = ''
# print_xml = False

# Initial Transaction.
transaction = fields.authorization()
transaction.orderId = '1'
transaction.amount = 10010
transaction.reportGroup = 'Planets'
transaction.orderSource = 'ecommerce'
transaction.id = 'ThisIsRequiredby11'

# Create contact object
contact = fields.contact()
contact.name = 'John & Mary Smith'
contact.addressLine1 = '1 Main St.'
contact.city = 'Burlington'
contact.state = 'MA'
contact.zip = '01803-3747'
contact.country = 'USA'
# The type of billToAddress is contact
transaction.billToAddress = contact

# Create cardType object
card = fields.cardType()
card.number = '375001010000003'
card.expDate = '0112'
card.cardValidationNum = '349'
card.type = 'VI'
# The type of card is cardType
transaction.card = card

# Send request to server and get response as object
response = online.request(transaction, conf)

# Print results
print('Get response as object\n')
print('Message: %s' % response.transactionResponse.message)
print('LitleTransaction ID: %s' % response.transactionResponse.litleTxnId)
```
NOTE: you may need to edit the proxy to to work for your system

4) Next run this file.  You should see the following result.

    Message: Valid Format
    Litle Transaction ID: <your-numeric-litle-txn-id>
    
For information on configuration settings go to: [SDK Config Info](https://github.com/LitleCo/litle-sdk-for-python/wiki/Config-Settings).

More examples can be found here [Python Gists](https://gist.github.com/gists/search?q=Litle+Python+SDK&page=1)

Please contact Vantiv eCommerce with any further questions. You can reach us at SDKSupport@Vantiv.com
