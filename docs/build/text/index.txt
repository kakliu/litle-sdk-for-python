Vantiv eCommerce Python SDK's documentation 11.0!
*************************************************


Batch
=====


batch.stream
------------

   litle_sdk_python.batch.stream(transactions, conf, return_format='object', timeout_send=60, timeout_rev=2)

      stream batch request to IBC (inbound batch communicator) via
      socket and get return object

      Parameters:
         * **transactions** -- an instance of batch.Transactions.

         * **conf** -- An instance of utils.Configuration.

         * **return_format** -- Return format. The default is
           'object'. Could be either 'object' or 'xml'.

         * **timeout_send** -- Positive int. Timeout in second for
           socket connection when sending.

         * **timeout_rev** -- Positive int. Timeout in second for
           socket connection when receiving.

      Returns:
         response XML in desired format.


batch.download
--------------

   litle_sdk_python.batch.download(filename, conf, delete_remote=True, timeout=60)

      Download Processed Session File from server via sFTP

      Get xml file from server and save to local file system

      Parameters:
         * **filename** -- filename of file in outbound folder at
           remote server with '.asc' as extension.

         * **conf** -- An instance of utils.Configuration.

         * **delete_remote** -- If delete the remote file after
           download. The default is True

         * **timeout** -- Timeout in second for ssh connection for
           sftp.

      Returns:
         path for file that saved in local file system.

      Raises:
         Exception depends on when get it.


batch.submit
------------

   litle_sdk_python.batch.submit(transactions, conf, filename='', timeout=60)

      Submitting a Session File for Processing to server via sFTP

      1. Generate litleRequest xml.

      2. Save xml at local file system.

      3. Send xml file to server.

      Parameters:
         * **transactions** -- an instance of batch.Transactions.

         * **conf** -- An instance of utils.Configuration.

         * **filename** -- String. File name for generated xml file.
           If the file exist, a timestamp string will be added.

         * **timeout** -- Positive int. Timeout in second for ssh
           connection for sftp.

      Returns:
         filename of file in inbound folder at remote server with
         '.asc' as extension.

      Raises:
         Exception depends on when get it.


batch.retrieve
--------------

   litle_sdk_python.batch.retrieve(filename, conf, return_format='object', save_to_local=False, delete_remote=True, timeout=60)

      Retrieving Processed Session File from server via sFTP

      1. Get xml file string from server and return object

      2. If save_to_local, save to local file system

      Parameters:
         * **filename** -- filename of file in outbound folder at
           remote server with '.asc' as extension.

         * **conf** -- An instance of utils.Configuration.

         * **return_format** -- Return format. The default is
           'object'. Could be either 'object' or 'xml'.

         * **save_to_local** -- whether save file to local. default
           is false.

         * **delete_remote** -- If delete the remote file after
           download. The default is True

         * **timeout** -- Timeout in second for ssh connection for
           sftp.

      Returns:
         response XML in desired format.

      Raises:
         Exception depends on when get it.


batch.Transactions
------------------

   class litle_sdk_python.batch.Transactions

      Container of transactions for batch request

      Then transactions could be RFRRequest and any batch request
      supported transactions and recurringTransaction. RFRRequest
      cannot exist in the same instance with any other transactions.

      A instance cannot contain more than 1,000,000 transactions.

      add(transaction)

         Add transaction to the container class.

         Parameters:
            **transaction** -- an instance of Transactions or
            RFRRequest which could process by Batch.

         Returns:
            None

         Raises:
            "Exceptions."

      is_rfr_request

         A property, whether current instanc include a RFRRequest

         Returns:
            Boolean

      transactions

         A property, return a new list of transactions.

         Returns:
            list of transactions


Configuration
=============

   class litle_sdk_python.utils.Configuration

      Setup Configuration variables.

      user

         *Str* -- authentication.user

      password

         *Str* -- authentication.password

      merchantId

         *Str* -- The unique string to identify the merchant within
         the system.

      reportGroup

         *Str* -- To separate your transactions into different
         categories,

      url

         *Str* -- Url for server.

      proxy

         *Str* -- Https proxy server address. Must start with
         "https://"

      sftp_username

         *Str* -- Username for sftp

      sftp_password

         *Str* -- Password for sftp

      sftp_url

         *Str* -- Address for sftp

      batch_requests_path

         *Str* -- Location for saving generated batch request xml

      batch_response_path

         *Str* -- Location for saving batch response xml

      fast_url

         *Str* -- Fast address, using for batch stream

      fast_port

         *Str* -- Fast port, using for batch stream

      print_xml

         *Str* -- Whether print request and response xml

      save()

         Save Class Attributes to .vantiv_python_sdk.conf

         Returns:
            full path for configuration file.

         Raises:
            "IOError" -- An error occurred


Online
======

   litle_sdk_python.online.request(transaction, conf, return_format='object', timeout=30)

      Send request to server.

      Parameters:
         * **transaction** -- An instance of transaction class

         * **conf** -- An instance of utils.Configuration

         * **return_format** -- Return format. The default is
           'object'. Could be either 'object' or 'xml'.

         * **timeout** -- timeout for the request in seconds.
           timeout is not a time limit on the entire response.

         * **the time that server has not issued a response.**
           (*It's*) --

      Returns:
         response XML in desired format.

      Raises:
         Vantiv Exceptions.


Transactions
============


accountUpdate
-------------

   class litle_sdk_python.fields.accountUpdate

      Variables:
         * **cardOrToken** -- String or Number

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **orderId** -- String or Number

         * **reportGroup** -- String or Number


activate
--------

   class litle_sdk_python.fields.activate

      Variables:
         * **amount** -- String or Number

         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **orderId** -- String or Number

         * **orderSource** -- String or Number

         * **reportGroup** -- String or Number

         * **virtualGiftCard** -- String or Number


activateReversal
----------------

   class litle_sdk_python.fields.activateReversal

      Variables:
         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **originalAmount** -- String or Number

         * **originalRefCode** -- String or Number

         * **originalSequenceNumber** -- String or Number

         * **originalSystemTraceId** -- String or Number

         * **originalTxnTime** -- String or Number

         * **reportGroup** -- String or Number

         * **virtualGiftCardBin** -- String or Number


authReversal
------------

   class litle_sdk_python.fields.authReversal

      Variables:
         * **actionReason** -- String or Number

         * **amount** -- String or Number

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **payPalNotes** -- String or Number

         * **reportGroup** -- String or Number

         * **surchargeAmount** -- String or Number


authorization
-------------

   class litle_sdk_python.fields.authorization

      Variables:
         * **advancedFraudChecks** -- String or Number

         * **allowPartialAuth** -- String or Number

         * **amexAggregatorData** -- instance of
           "litle_sdk_python.fields.amexAggregatorData"

         * **amount** -- String or Number

         * **applepay** -- String or Number

         * **billMeLaterRequest** -- instance of
           "litle_sdk_python.fields.billMeLaterRequest"

         * **billToAddress** -- instance of
           "litle_sdk_python.fields.contact"

         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **cardholderAuthentication** -- String or Number

         * **customBilling** -- instance of
           "litle_sdk_python.fields.customBilling"

         * **customerId** -- String or Number

         * **customerInfo** -- instance of
           "litle_sdk_python.fields.customerInfo"

         * **debtRepayment** -- String or Number

         * **enhancedData** -- instance of
           "litle_sdk_python.fields.enhancedData"

         * **filtering** -- String or Number

         * **fraudFilterOverride** -- String or Number

         * **healthcareIIAS** -- instance of
           "litle_sdk_python.fields.healthcareIIAS"

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **merchantData** -- String or Number

         * **mpos** -- String or Number

         * **orderId** -- String or Number

         * **orderSource** -- String or Number

         * **originalNetworkTransactionId** -- String or Number

         * **originalTransactionAmount** -- String or Number

         * **paypage** -- String or Number

         * **paypal** -- String or Number

         * **pos** -- instance of "litle_sdk_python.fields.pos"

         * **processingInstructions** -- instance of
           "litle_sdk_python.fields.processingInstructions"

         * **processingType** -- String or Number

         * **recurringRequest** -- String or Number

         * **recyclingRequest** -- String or Number

         * **reportGroup** -- String or Number

         * **secondaryAmount** -- String or Number

         * **shipToAddress** -- instance of
           "litle_sdk_python.fields.contact"

         * **surchargeAmount** -- String or Number

         * **taxType** -- String or Number

         * **token** -- instance of
           "litle_sdk_python.fields.cardTokenType"

         * **wallet** -- instance of
           "litle_sdk_python.fields.wallet"


balanceInquiry
--------------

   class litle_sdk_python.fields.balanceInquiry

      Variables:
         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **orderId** -- String or Number

         * **orderSource** -- String or Number

         * **reportGroup** -- String or Number


capture
-------

   class litle_sdk_python.fields.capture

      Variables:
         * **amount** -- String or Number

         * **customBilling** -- instance of
           "litle_sdk_python.fields.customBilling"

         * **customerId** -- String or Number

         * **enhancedData** -- instance of
           "litle_sdk_python.fields.enhancedData"

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **partial** -- String or Number

         * **payPalNotes** -- String or Number

         * **payPalOrderComplete** -- String or Number

         * **pin** -- String or Number

         * **processingInstructions** -- instance of
           "litle_sdk_python.fields.processingInstructions"

         * **reportGroup** -- String or Number

         * **surchargeAmount** -- String or Number


captureGivenAuth
----------------

   class litle_sdk_python.fields.captureGivenAuth

      Variables:
         * **amexAggregatorData** -- instance of
           "litle_sdk_python.fields.amexAggregatorData"

         * **amount** -- String or Number

         * **authInformation** -- instance of
           "litle_sdk_python.fields.authInformation"

         * **billMeLaterRequest** -- instance of
           "litle_sdk_python.fields.billMeLaterRequest"

         * **billToAddress** -- instance of
           "litle_sdk_python.fields.contact"

         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **customBilling** -- instance of
           "litle_sdk_python.fields.customBilling"

         * **customerId** -- String or Number

         * **debtRepayment** -- String or Number

         * **enhancedData** -- instance of
           "litle_sdk_python.fields.enhancedData"

         * **id** -- String or Number

         * **merchantData** -- String or Number

         * **mpos** -- String or Number

         * **orderId** -- String or Number

         * **orderSource** -- String or Number

         * **originalNetworkTransactionId** -- String or Number

         * **originalTransactionAmount** -- String or Number

         * **paypage** -- String or Number

         * **pos** -- instance of "litle_sdk_python.fields.pos"

         * **processingInstructions** -- instance of
           "litle_sdk_python.fields.processingInstructions"

         * **processingType** -- String or Number

         * **reportGroup** -- String or Number

         * **secondaryAmount** -- String or Number

         * **shipToAddress** -- instance of
           "litle_sdk_python.fields.contact"

         * **surchargeAmount** -- String or Number

         * **taxType** -- String or Number

         * **token** -- instance of
           "litle_sdk_python.fields.cardTokenType"


credit
------

   class litle_sdk_python.fields.credit

      Variables:
         * **actionReason** -- String or Number

         * **amexAggregatorData** -- instance of
           "litle_sdk_python.fields.amexAggregatorData"

         * **amount** -- String or Number

         * **billMeLaterRequest** -- instance of
           "litle_sdk_python.fields.billMeLaterRequest"

         * **billToAddress** -- instance of
           "litle_sdk_python.fields.contact"

         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **customBilling** -- instance of
           "litle_sdk_python.fields.customBilling"

         * **customerId** -- String or Number

         * **enhancedData** -- instance of
           "litle_sdk_python.fields.enhancedData"

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **merchantData** -- String or Number

         * **mpos** -- String or Number

         * **orderId** -- String or Number

         * **orderSource** -- String or Number

         * **payPalNotes** -- String or Number

         * **paypage** -- String or Number

         * **paypal** -- String or Number

         * **pin** -- String or Number

         * **pos** -- instance of "litle_sdk_python.fields.pos"

         * **processingInstructions** -- instance of
           "litle_sdk_python.fields.processingInstructions"

         * **reportGroup** -- String or Number

         * **secondaryAmount** -- String or Number

         * **surchargeAmount** -- String or Number

         * **taxType** -- String or Number

         * **token** -- instance of
           "litle_sdk_python.fields.cardTokenType"


deactivate
----------

   class litle_sdk_python.fields.deactivate

      Variables:
         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **orderId** -- String or Number

         * **orderSource** -- String or Number

         * **reportGroup** -- String or Number


deactivateReversal
------------------

   class litle_sdk_python.fields.deactivateReversal

      Variables:
         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **originalRefCode** -- String or Number

         * **originalSequenceNumber** -- String or Number

         * **originalSystemTraceId** -- String or Number

         * **originalTxnTime** -- String or Number

         * **reportGroup** -- String or Number


depositReversal
---------------

   class litle_sdk_python.fields.depositReversal

      Variables:
         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **originalAmount** -- String or Number

         * **originalRefCode** -- String or Number

         * **originalSequenceNumber** -- String or Number

         * **originalSystemTraceId** -- String or Number

         * **originalTxnTime** -- String or Number

         * **reportGroup** -- String or Number


echeckCredit
------------

   class litle_sdk_python.fields.echeckCredit

      Variables:
         * **amount** -- String or Number

         * **billToAddress** -- instance of
           "litle_sdk_python.fields.contact"

         * **customBilling** -- instance of
           "litle_sdk_python.fields.customBilling"

         * **customIdentifier** -- String or Number

         * **customerId** -- String or Number

         * **echeckOrEcheckToken** -- String or Number

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **merchantData** -- String or Number

         * **orderId** -- String or Number

         * **orderSource** -- String or Number

         * **reportGroup** -- String or Number

         * **secondaryAmount** -- String or Number


echeckPreNoteCredit
-------------------

   class litle_sdk_python.fields.echeckPreNoteCredit

      Variables:
         * **billToAddress** -- instance of
           "litle_sdk_python.fields.contact"

         * **customerId** -- String or Number

         * **echeck** -- instance of
           "litle_sdk_python.fields.echeckType"

         * **id** -- String or Number

         * **merchantData** -- String or Number

         * **orderId** -- String or Number

         * **orderSource** -- String or Number

         * **reportGroup** -- String or Number


echeckPreNoteSale
-----------------

   class litle_sdk_python.fields.echeckPreNoteSale

      Variables:
         * **billToAddress** -- instance of
           "litle_sdk_python.fields.contact"

         * **customerId** -- String or Number

         * **echeck** -- instance of
           "litle_sdk_python.fields.echeckType"

         * **id** -- String or Number

         * **merchantData** -- String or Number

         * **orderId** -- String or Number

         * **orderSource** -- String or Number

         * **reportGroup** -- String or Number


echeckRedeposit
---------------

   class litle_sdk_python.fields.echeckRedeposit

      Variables:
         * **customIdentifier** -- String or Number

         * **customerId** -- String or Number

         * **echeckOrEcheckToken** -- String or Number

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **merchantData** -- String or Number

         * **reportGroup** -- String or Number


echeckSale
----------

   class litle_sdk_python.fields.echeckSale

      Variables:
         * **amount** -- String or Number

         * **billToAddress** -- instance of
           "litle_sdk_python.fields.contact"

         * **customBilling** -- instance of
           "litle_sdk_python.fields.customBilling"

         * **customIdentifier** -- String or Number

         * **customerId** -- String or Number

         * **echeckOrEcheckToken** -- String or Number

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **merchantData** -- String or Number

         * **orderId** -- String or Number

         * **orderSource** -- String or Number

         * **reportGroup** -- String or Number

         * **secondaryAmount** -- String or Number

         * **shipToAddress** -- instance of
           "litle_sdk_python.fields.contact"

         * **verify** -- String or Number


echeckVerification
------------------

   class litle_sdk_python.fields.echeckVerification

      Variables:
         * **amount** -- String or Number

         * **billToAddress** -- instance of
           "litle_sdk_python.fields.contact"

         * **customerId** -- String or Number

         * **echeckOrEcheckToken** -- String or Number

         * **id** -- String or Number

         * **merchantData** -- String or Number

         * **orderId** -- String or Number

         * **orderSource** -- String or Number

         * **reportGroup** -- String or Number


echeckVoid
----------

   class litle_sdk_python.fields.echeckVoid

      Variables:
         * **customerId** -- String or Number

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **reportGroup** -- String or Number


forceCapture
------------

   class litle_sdk_python.fields.forceCapture

      Variables:
         * **amexAggregatorData** -- instance of
           "litle_sdk_python.fields.amexAggregatorData"

         * **amount** -- String or Number

         * **billToAddress** -- instance of
           "litle_sdk_python.fields.contact"

         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **customBilling** -- instance of
           "litle_sdk_python.fields.customBilling"

         * **customerId** -- String or Number

         * **debtRepayment** -- String or Number

         * **enhancedData** -- instance of
           "litle_sdk_python.fields.enhancedData"

         * **id** -- String or Number

         * **merchantData** -- String or Number

         * **mpos** -- String or Number

         * **orderId** -- String or Number

         * **orderSource** -- String or Number

         * **paypage** -- String or Number

         * **pos** -- instance of "litle_sdk_python.fields.pos"

         * **processingInstructions** -- instance of
           "litle_sdk_python.fields.processingInstructions"

         * **processingType** -- String or Number

         * **reportGroup** -- String or Number

         * **secondaryAmount** -- String or Number

         * **surchargeAmount** -- String or Number

         * **taxType** -- String or Number

         * **token** -- instance of
           "litle_sdk_python.fields.cardTokenType"


fraudCheck
----------

   class litle_sdk_python.fields.fraudCheck

      Variables:
         * **advancedFraudChecks** -- String or Number

         * **amount** -- String or Number

         * **billToAddress** -- instance of
           "litle_sdk_python.fields.contact"

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **reportGroup** -- String or Number

         * **shipToAddress** -- instance of
           "litle_sdk_python.fields.contact"


fundingInstructionVoid
----------------------

   class litle_sdk_python.fields.fundingInstructionVoid

      Variables:
         * **customerId** -- String or Number

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **reportGroup** -- String or Number


giftCardAuthReversal
--------------------

   class litle_sdk_python.fields.giftCardAuthReversal

      Variables:
         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **originalAmount** -- String or Number

         * **originalRefCode** -- String or Number

         * **originalSequenceNumber** -- String or Number

         * **originalSystemTraceId** -- String or Number

         * **originalTxnTime** -- String or Number

         * **reportGroup** -- String or Number


giftCardCapture
---------------

   class litle_sdk_python.fields.giftCardCapture

      Variables:
         * **captureAmount** -- String or Number

         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **originalAmount** -- String or Number

         * **originalRefCode** -- String or Number

         * **originalTxnTime** -- String or Number

         * **partial** -- String or Number

         * **reportGroup** -- String or Number


giftCardCredit
--------------

   class litle_sdk_python.fields.giftCardCredit

      Variables:
         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **creditAmount** -- String or Number

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **orderId** -- String or Number

         * **orderSource** -- String or Number

         * **reportGroup** -- String or Number


load
----

   class litle_sdk_python.fields.load

      Variables:
         * **amount** -- String or Number

         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **orderId** -- String or Number

         * **orderSource** -- String or Number

         * **reportGroup** -- String or Number


loadReversal
------------

   class litle_sdk_python.fields.loadReversal

      Variables:
         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **originalAmount** -- String or Number

         * **originalRefCode** -- String or Number

         * **originalSequenceNumber** -- String or Number

         * **originalSystemTraceId** -- String or Number

         * **originalTxnTime** -- String or Number

         * **reportGroup** -- String or Number


payFacCredit
------------

   class litle_sdk_python.fields.payFacCredit

      Variables:
         * **amount** -- String or Number

         * **customerId** -- String or Number

         * **fundingSubmerchantId** -- String or Number

         * **fundsTransferId** -- String or Number

         * **id** -- String or Number

         * **reportGroup** -- String or Number


payFacDebit
-----------

   class litle_sdk_python.fields.payFacDebit

      Variables:
         * **amount** -- String or Number

         * **customerId** -- String or Number

         * **fundingSubmerchantId** -- String or Number

         * **fundsTransferId** -- String or Number

         * **id** -- String or Number

         * **reportGroup** -- String or Number


physicalCheckCredit
-------------------

   class litle_sdk_python.fields.physicalCheckCredit

      Variables:
         * **amount** -- String or Number

         * **customerId** -- String or Number

         * **fundingSubmerchantId** -- String or Number

         * **fundsTransferId** -- String or Number

         * **id** -- String or Number

         * **reportGroup** -- String or Number


physicalCheckDebit
------------------

   class litle_sdk_python.fields.physicalCheckDebit

      Variables:
         * **amount** -- String or Number

         * **customerId** -- String or Number

         * **fundingSubmerchantId** -- String or Number

         * **fundsTransferId** -- String or Number

         * **id** -- String or Number

         * **reportGroup** -- String or Number


queryTransaction
----------------

   class litle_sdk_python.fields.queryTransaction

      Variables:
         * **customerId** -- String or Number

         * **id** -- String or Number

         * **origActionType** -- String or Number

         * **origId** -- String or Number

         * **origLitleTxnId** -- String or Number

         * **reportGroup** -- String or Number


refundReversal
--------------

   class litle_sdk_python.fields.refundReversal

      Variables:
         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **originalAmount** -- String or Number

         * **originalRefCode** -- String or Number

         * **originalSequenceNumber** -- String or Number

         * **originalSystemTraceId** -- String or Number

         * **originalTxnTime** -- String or Number

         * **reportGroup** -- String or Number


reserveCredit
-------------

   class litle_sdk_python.fields.reserveCredit

      Variables:
         * **amount** -- String or Number

         * **customerId** -- String or Number

         * **fundingSubmerchantId** -- String or Number

         * **fundsTransferId** -- String or Number

         * **id** -- String or Number

         * **reportGroup** -- String or Number


reserveDebit
------------

   class litle_sdk_python.fields.reserveDebit

      Variables:
         * **amount** -- String or Number

         * **customerId** -- String or Number

         * **fundingSubmerchantId** -- String or Number

         * **fundsTransferId** -- String or Number

         * **id** -- String or Number

         * **reportGroup** -- String or Number


sale
----

   class litle_sdk_python.fields.sale

      Variables:
         * **advancedFraudChecks** -- String or Number

         * **allowPartialAuth** -- String or Number

         * **amexAggregatorData** -- instance of
           "litle_sdk_python.fields.amexAggregatorData"

         * **amount** -- String or Number

         * **applepay** -- String or Number

         * **billMeLaterRequest** -- instance of
           "litle_sdk_python.fields.billMeLaterRequest"

         * **billToAddress** -- instance of
           "litle_sdk_python.fields.contact"

         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **cardholderAuthentication** -- String or Number

         * **customBilling** -- instance of
           "litle_sdk_python.fields.customBilling"

         * **customerId** -- String or Number

         * **customerInfo** -- instance of
           "litle_sdk_python.fields.customerInfo"

         * **debtRepayment** -- String or Number

         * **enhancedData** -- instance of
           "litle_sdk_python.fields.enhancedData"

         * **filtering** -- String or Number

         * **fraudCheck** -- instance of
           "litle_sdk_python.fields.fraudCheck"

         * **fraudFilterOverride** -- String or Number

         * **healthcareIIAS** -- instance of
           "litle_sdk_python.fields.healthcareIIAS"

         * **id** -- String or Number

         * **litleInternalRecurringRequest** -- String or Number

         * **litleTxnId** -- String or Number

         * **merchantData** -- String or Number

         * **mpos** -- String or Number

         * **orderId** -- String or Number

         * **orderSource** -- String or Number

         * **originalNetworkTransactionId** -- String or Number

         * **originalTransactionAmount** -- String or Number

         * **payPalNotes** -- String or Number

         * **payPalOrderComplete** -- String or Number

         * **paypage** -- String or Number

         * **paypal** -- String or Number

         * **pos** -- instance of "litle_sdk_python.fields.pos"

         * **processingInstructions** -- instance of
           "litle_sdk_python.fields.processingInstructions"

         * **processingType** -- String or Number

         * **recurringRequest** -- String or Number

         * **recyclingRequest** -- String or Number

         * **reportGroup** -- String or Number

         * **secondaryAmount** -- String or Number

         * **sepaDirectDebit** -- String or Number

         * **shipToAddress** -- instance of
           "litle_sdk_python.fields.contact"

         * **surchargeAmount** -- String or Number

         * **taxType** -- String or Number

         * **token** -- instance of
           "litle_sdk_python.fields.cardTokenType"

         * **wallet** -- instance of
           "litle_sdk_python.fields.wallet"


serviceStatusRequest
--------------------

   class litle_sdk_python.fields.serviceStatusRequest

      Variables:
         * **customerId** -- String or Number

         * **id** -- String or Number

         * **pathId** -- String or Number

         * **reportGroup** -- String or Number

         * **serviceId** -- String or Number


submerchantCredit
-----------------

   class litle_sdk_python.fields.submerchantCredit

      Variables:
         * **accountInfo** -- String or Number

         * **amount** -- String or Number

         * **customIdentifier** -- String or Number

         * **customerId** -- String or Number

         * **fundingSubmerchantId** -- String or Number

         * **fundsTransferId** -- String or Number

         * **id** -- String or Number

         * **reportGroup** -- String or Number

         * **submerchantName** -- String or Number


submerchantDebit
----------------

   class litle_sdk_python.fields.submerchantDebit

      Variables:
         * **accountInfo** -- String or Number

         * **amount** -- String or Number

         * **customIdentifier** -- String or Number

         * **customerId** -- String or Number

         * **fundingSubmerchantId** -- String or Number

         * **fundsTransferId** -- String or Number

         * **id** -- String or Number

         * **reportGroup** -- String or Number

         * **submerchantName** -- String or Number


unload
------

   class litle_sdk_python.fields.unload

      Variables:
         * **amount** -- String or Number

         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **orderId** -- String or Number

         * **orderSource** -- String or Number

         * **reportGroup** -- String or Number


unloadReversal
--------------

   class litle_sdk_python.fields.unloadReversal

      Variables:
         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **originalAmount** -- String or Number

         * **originalRefCode** -- String or Number

         * **originalSequenceNumber** -- String or Number

         * **originalSystemTraceId** -- String or Number

         * **originalTxnTime** -- String or Number

         * **reportGroup** -- String or Number


vendorCredit
------------

   class litle_sdk_python.fields.vendorCredit

      Variables:
         * **accountInfo** -- String or Number

         * **amount** -- String or Number

         * **customerId** -- String or Number

         * **fundingSubmerchantId** -- String or Number

         * **fundsTransferId** -- String or Number

         * **id** -- String or Number

         * **reportGroup** -- String or Number

         * **vendorName** -- String or Number


vendorDebit
-----------

   class litle_sdk_python.fields.vendorDebit

      Variables:
         * **accountInfo** -- String or Number

         * **amount** -- String or Number

         * **customerId** -- String or Number

         * **fundingSubmerchantId** -- String or Number

         * **fundsTransferId** -- String or Number

         * **id** -- String or Number

         * **reportGroup** -- String or Number

         * **vendorName** -- String or Number


void
----

   class litle_sdk_python.fields.void

      Variables:
         * **customerId** -- String or Number

         * **id** -- String or Number

         * **litleTxnId** -- String or Number

         * **processingInstructions** -- instance of
           "litle_sdk_python.fields.processingInstructions"

         * **reportGroup** -- String or Number


Complex Types
=============


CTD_ANON_15
-----------

   class litle_sdk_python.fields.CTD_ANON_15

      Variables:
         * **availableBalance** -- String or Number

         * **prepaidCardType** -- String or Number

         * **reloadable** -- String or Number

         * **type** -- String or Number


CTD_ANON_32
-----------

   class litle_sdk_python.fields.CTD_ANON_32

      Variables:
         **transactionResponse** -- String or Number


RFRRequest
----------

   class litle_sdk_python.fields.RFRRequest

      Variables:
         * **accountUpdateFileRequestData** -- instance of
           "litle_sdk_python.fields.accountUpdateFileRequestData"

         * **litleSessionId** -- String or Number


accountInfoType
---------------

   class litle_sdk_python.fields.accountInfoType

      Variables:
         * **number** -- String or Number

         * **type** -- String or Number


accountUpdateFileRequestData
----------------------------

   class litle_sdk_python.fields.accountUpdateFileRequestData

      Variables:
         * **merchantId** -- String or Number

         * **postDay** -- String or Number


accountUpdater
--------------

   class litle_sdk_python.fields.accountUpdater

      Variables:
         * **extendedCardResponse** -- String or Number

         * **newAccountInfo** -- String or Number

         * **newCardInfo** -- String or Number

         * **newCardTokenInfo** -- String or Number

         * **newTokenInfo** -- String or Number

         * **originalAccountInfo** -- String or Number

         * **originalCardInfo** -- String or Number

         * **originalCardTokenInfo** -- String or Number

         * **originalTokenInfo** -- String or Number


advancedFraudChecksType
-----------------------

   class litle_sdk_python.fields.advancedFraudChecksType

      Variables:
         * **customAttribute1** -- String or Number

         * **customAttribute2** -- String or Number

         * **customAttribute3** -- String or Number

         * **customAttribute4** -- String or Number

         * **customAttribute5** -- String or Number

         * **threatMetrixSessionId** -- String or Number


advancedFraudResultsType
------------------------

   class litle_sdk_python.fields.advancedFraudResultsType

      Variables:
         * **deviceReputationScore** -- String or Number

         * **deviceReviewStatus** -- String or Number

         * **triggeredRule** -- String or Number


amexAggregatorData
------------------

   class litle_sdk_python.fields.amexAggregatorData

      Variables:
         * **sellerId** -- String or Number

         * **sellerMerchantCategoryCode** -- String or Number


applepayHeaderType
------------------

   class litle_sdk_python.fields.applepayHeaderType

      Variables:
         * **applicationData** -- String or Number

         * **ephemeralPublicKey** -- String or Number

         * **publicKeyHash** -- String or Number

         * **transactionId** -- String or Number


applepayType
------------

   class litle_sdk_python.fields.applepayType

      Variables:
         * **data** -- String or Number

         * **header** -- String or Number

         * **signature** -- String or Number

         * **version** -- String or Number


authInformation
---------------

   class litle_sdk_python.fields.authInformation

      Variables:
         * **authAmount** -- String or Number

         * **authCode** -- String or Number

         * **authDate** -- String or Number

         * **fraudResult** -- instance of
           "litle_sdk_python.fields.fraudResult"


authentication
--------------

   class litle_sdk_python.fields.authentication

      Variables:
         * **password** -- String or Number

         * **user** -- String or Number


baseRequest
-----------

   class litle_sdk_python.fields.baseRequest

      Variables:
         * **authentication** -- instance of
           "litle_sdk_python.fields.authentication"

         * **recurringTransaction** -- String or Number

         * **transaction** -- String or Number

         * **version** -- String or Number


batchRequest
------------

   class litle_sdk_python.fields.batchRequest

      Variables:
         * **activateAmount** -- String or Number

         * **authAmount** -- String or Number

         * **authReversalAmount** -- String or Number

         * **captureAmount** -- String or Number

         * **captureGivenAuthAmount** -- String or Number

         * **creditAmount** -- String or Number

         * **echeckCreditAmount** -- String or Number

         * **echeckSalesAmount** -- String or Number

         * **echeckVerificationAmount** -- String or Number

         * **extCaptureAmount** -- String or Number

         * **forceCaptureAmount** -- String or Number

         * **giftCardAuthReversalOriginalAmount** -- String or
           Number

         * **giftCardCaptureAmount** -- String or Number

         * **giftCardCreditAmount** -- String or Number

         * **id** -- String or Number

         * **loadAmount** -- String or Number

         * **merchantId** -- String or Number

         * **merchantSdk** -- String or Number

         * **numAccountUpdates** -- String or Number

         * **numActivates** -- String or Number

         * **numAuthReversals** -- String or Number

         * **numAuths** -- String or Number

         * **numBalanceInquirys** -- String or Number

         * **numCancelSubscriptions** -- String or Number

         * **numCaptureGivenAuths** -- String or Number

         * **numCaptures** -- String or Number

         * **numCreatePlans** -- String or Number

         * **numCredits** -- String or Number

         * **numDeactivates** -- String or Number

         * **numEcheckCredit** -- String or Number

         * **numEcheckPreNoteCredit** -- String or Number

         * **numEcheckPreNoteSale** -- String or Number

         * **numEcheckRedeposit** -- String or Number

         * **numEcheckSales** -- String or Number

         * **numEcheckVerification** -- String or Number

         * **numExtCaptures** -- String or Number

         * **numForceCaptures** -- String or Number

         * **numFundingInstructionVoid** -- String or Number

         * **numGiftCardAuthReversals** -- String or Number

         * **numGiftCardCaptures** -- String or Number

         * **numGiftCardCredits** -- String or Number

         * **numLoads** -- String or Number

         * **numPayFacCredit** -- String or Number

         * **numPayFacDebit** -- String or Number

         * **numPhysicalCheckCredit** -- String or Number

         * **numPhysicalCheckDebit** -- String or Number

         * **numReserveCredit** -- String or Number

         * **numReserveDebit** -- String or Number

         * **numSales** -- String or Number

         * **numSubmerchantCredit** -- String or Number

         * **numSubmerchantDebit** -- String or Number

         * **numTokenRegistrations** -- String or Number

         * **numUnloads** -- String or Number

         * **numUpdateCardValidationNumOnTokens** -- String or
           Number

         * **numUpdatePlans** -- String or Number

         * **numUpdateSubscriptions** -- String or Number

         * **numVendorCredit** -- String or Number

         * **numVendorDebit** -- String or Number

         * **payFacCreditAmount** -- String or Number

         * **payFacDebitAmount** -- String or Number

         * **physicalCheckCreditAmount** -- String or Number

         * **physicalCheckDebitAmount** -- String or Number

         * **recurringTransaction** -- String or Number

         * **reserveCreditAmount** -- String or Number

         * **reserveDebitAmount** -- String or Number

         * **saleAmount** -- String or Number

         * **submerchantCreditAmount** -- String or Number

         * **submerchantDebitAmount** -- String or Number

         * **transaction** -- String or Number

         * **unloadAmount** -- String or Number

         * **vendorCreditAmount** -- String or Number

         * **vendorDebitAmount** -- String or Number


billMeLaterRequest
------------------

   class litle_sdk_python.fields.billMeLaterRequest

      Variables:
         * **authorizationSourcePlatform** -- String or Number

         * **bmlMerchantId** -- String or Number

         * **bmlProductType** -- String or Number

         * **customerBillingAddressChanged** -- String or Number

         * **customerEmailChanged** -- String or Number

         * **customerPasswordChanged** -- String or Number

         * **customerPhoneChanged** -- String or Number

         * **itemCategoryCode** -- String or Number

         * **merchantPromotionalCode** -- String or Number

         * **preapprovalNumber** -- String or Number

         * **secretQuestionAnswer** -- String or Number

         * **secretQuestionCode** -- String or Number

         * **termsAndConditions** -- String or Number

         * **virtualAuthenticationKeyData** -- String or Number

         * **virtualAuthenticationKeyPresenceIndicator** -- String
           or Number


cancelSubscription
------------------

   class litle_sdk_python.fields.cancelSubscription

      Variables:
         **subscriptionId** -- String or Number


cardAccountInfoType
-------------------

   class litle_sdk_python.fields.cardAccountInfoType

      Variables:
         * **expDate** -- String or Number

         * **number** -- String or Number

         * **type** -- String or Number


cardPaypageType
---------------

   class litle_sdk_python.fields.cardPaypageType

      Variables:
         * **cardValidationNum** -- String or Number

         * **expDate** -- String or Number

         * **paypageRegistrationId** -- String or Number

         * **type** -- String or Number


cardTokenInfoType
-----------------

   class litle_sdk_python.fields.cardTokenInfoType

      Variables:
         * **bin** -- String or Number

         * **expDate** -- String or Number

         * **litleToken** -- String or Number

         * **type** -- String or Number


cardTokenType
-------------

   class litle_sdk_python.fields.cardTokenType

      Variables:
         * **cardValidationNum** -- String or Number

         * **expDate** -- String or Number

         * **litleToken** -- String or Number

         * **type** -- String or Number


cardTokenTypeAU
---------------

   class litle_sdk_python.fields.cardTokenTypeAU

      Variables:
         * **bin** -- String or Number

         * **cardValidationNum** -- String or Number

         * **expDate** -- String or Number

         * **litleToken** -- String or Number

         * **type** -- String or Number


cardType
--------

   class litle_sdk_python.fields.cardType

      Variables:
         * **cardValidationNum** -- String or Number

         * **expDate** -- String or Number

         * **number** -- String or Number

         * **pin** -- String or Number

         * **track** -- String or Number

         * **type** -- String or Number


contact
-------

   class litle_sdk_python.fields.contact

      Variables:
         * **addressLine1** -- String or Number

         * **addressLine2** -- String or Number

         * **addressLine3** -- String or Number

         * **city** -- String or Number

         * **companyName** -- String or Number

         * **country** -- String or Number

         * **email** -- String or Number

         * **firstName** -- String or Number

         * **lastName** -- String or Number

         * **middleInitial** -- String or Number

         * **name** -- String or Number

         * **phone** -- String or Number

         * **state** -- String or Number

         * **zip** -- String or Number


createAddOnType
---------------

   class litle_sdk_python.fields.createAddOnType

      Variables:
         * **addOnCode** -- String or Number

         * **amount** -- String or Number

         * **endDate** -- String or Number

         * **name** -- String or Number

         * **startDate** -- String or Number


createDiscountType
------------------

   class litle_sdk_python.fields.createDiscountType

      Variables:
         * **amount** -- String or Number

         * **discountCode** -- String or Number

         * **endDate** -- String or Number

         * **name** -- String or Number

         * **startDate** -- String or Number


createPlan
----------

   class litle_sdk_python.fields.createPlan

      Variables:
         * **active** -- String or Number

         * **amount** -- String or Number

         * **description** -- String or Number

         * **intervalType** -- String or Number

         * **name** -- String or Number

         * **numberOfPayments** -- String or Number

         * **planCode** -- String or Number

         * **trialIntervalType** -- String or Number

         * **trialNumberOfIntervals** -- String or Number


customBilling
-------------

   class litle_sdk_python.fields.customBilling

      Variables:
         * **city** -- String or Number

         * **descriptor** -- String or Number

         * **phone** -- String or Number

         * **url** -- String or Number


customerInfo
------------

   class litle_sdk_python.fields.customerInfo

      Variables:
         * **customerCheckingAccount** -- String or Number

         * **customerRegistrationDate** -- String or Number

         * **customerSavingAccount** -- String or Number

         * **customerType** -- String or Number

         * **customerWorkTelephone** -- String or Number

         * **dob** -- String or Number

         * **employerName** -- String or Number

         * **incomeAmount** -- String or Number

         * **incomeCurrency** -- String or Number

         * **residenceStatus** -- String or Number

         * **ssn** -- String or Number

         * **yearsAtEmployer** -- String or Number

         * **yearsAtResidence** -- String or Number


deleteAddOnType
---------------

   class litle_sdk_python.fields.deleteAddOnType

      Variables:
         **addOnCode** -- String or Number


deleteDiscountType
------------------

   class litle_sdk_python.fields.deleteDiscountType

      Variables:
         **discountCode** -- String or Number


detailTax
---------

   class litle_sdk_python.fields.detailTax

      Variables:
         * **cardAcceptorTaxId** -- String or Number

         * **taxAmount** -- String or Number

         * **taxIncludedInTotal** -- String or Number

         * **taxRate** -- String or Number

         * **taxTypeIdentifier** -- String or Number


driversLicenseInfo
------------------

   class litle_sdk_python.fields.driversLicenseInfo

      Variables:
         * **dateOfBirth** -- String or Number

         * **licenseNumber** -- String or Number

         * **state** -- String or Number


echeckAccountInfoType
---------------------

   class litle_sdk_python.fields.echeckAccountInfoType

      Variables:
         * **accNum** -- String or Number

         * **accType** -- String or Number

         * **routingNum** -- String or Number


echeckForTokenType
------------------

   class litle_sdk_python.fields.echeckForTokenType

      Variables:
         * **accNum** -- String or Number

         * **routingNum** -- String or Number


echeckTokenInfoType
-------------------

   class litle_sdk_python.fields.echeckTokenInfoType

      Variables:
         * **accType** -- String or Number

         * **litleToken** -- String or Number

         * **routingNum** -- String or Number


echeckTokenType
---------------

   class litle_sdk_python.fields.echeckTokenType

      Variables:
         * **accType** -- String or Number

         * **checkNum** -- String or Number

         * **litleToken** -- String or Number

         * **routingNum** -- String or Number


echeckType
----------

   class litle_sdk_python.fields.echeckType

      Variables:
         * **accNum** -- String or Number

         * **accType** -- String or Number

         * **ccdPaymentInformation** -- String or Number

         * **checkNum** -- String or Number

         * **routingNum** -- String or Number


enhancedData
------------

   class litle_sdk_python.fields.enhancedData

      Variables:
         * **customerReference** -- String or Number

         * **deliveryType** -- String or Number

         * **destinationCountryCode** -- String or Number

         * **destinationPostalCode** -- String or Number

         * **detailTax** -- instance of
           "litle_sdk_python.fields.detailTax"

         * **discountAmount** -- String or Number

         * **dutyAmount** -- String or Number

         * **invoiceReferenceNumber** -- String or Number

         * **lineItemData** -- instance of
           "litle_sdk_python.fields.lineItemData"

         * **orderDate** -- String or Number

         * **salesTax** -- String or Number

         * **shipFromPostalCode** -- String or Number

         * **shippingAmount** -- String or Number

         * **taxExempt** -- String or Number


filteringType
-------------

   class litle_sdk_python.fields.filteringType

      Variables:
         * **chargeback** -- String or Number

         * **international** -- String or Number

         * **prepaid** -- String or Number


fraudCheckType
--------------

   class litle_sdk_python.fields.fraudCheckType

      Variables:
         * **authenticatedByMerchant** -- String or Number

         * **authenticationTransactionId** -- String or Number

         * **authenticationValue** -- String or Number

         * **customerIpAddress** -- String or Number


fraudResult
-----------

   class litle_sdk_python.fields.fraudResult

      Variables:
         * **advancedAVSResult** -- String or Number

         * **advancedFraudResults** -- String or Number

         * **authenticationResult** -- String or Number

         * **avsResult** -- String or Number

         * **cardValidationResult** -- String or Number


giftCardCardType
----------------

   class litle_sdk_python.fields.giftCardCardType

      Variables:
         * **cardValidationNum** -- String or Number

         * **expDate** -- String or Number

         * **number** -- String or Number

         * **pin** -- String or Number

         * **track** -- String or Number

         * **type** -- String or Number


healthcareAmounts
-----------------

   class litle_sdk_python.fields.healthcareAmounts

      Variables:
         * **RxAmount** -- String or Number

         * **clinicOtherAmount** -- String or Number

         * **dentalAmount** -- String or Number

         * **totalHealthcareAmount** -- String or Number

         * **visionAmount** -- String or Number


healthcareIIAS
--------------

   class litle_sdk_python.fields.healthcareIIAS

      Variables:
         * **IIASFlag** -- String or Number

         * **healthcareAmounts** -- instance of
           "litle_sdk_python.fields.healthcareAmounts"


lineItemData
------------

   class litle_sdk_python.fields.lineItemData

      Variables:
         * **commodityCode** -- String or Number

         * **detailTax** -- instance of
           "litle_sdk_python.fields.detailTax"

         * **itemDescription** -- String or Number

         * **itemDiscountAmount** -- String or Number

         * **itemSequenceNumber** -- String or Number

         * **lineItemTotal** -- String or Number

         * **lineItemTotalWithTax** -- String or Number

         * **productCode** -- String or Number

         * **quantity** -- String or Number

         * **taxAmount** -- String or Number

         * **unitCost** -- String or Number

         * **unitOfMeasure** -- String or Number


litleInternalRecurringRequestType
---------------------------------

   class litle_sdk_python.fields.litleInternalRecurringRequestType

      Variables:
         * **finalPayment** -- String or Number

         * **recurringTxnId** -- String or Number

         * **subscriptionId** -- String or Number


litleOnlineRequest
------------------

   class litle_sdk_python.fields.litleOnlineRequest

      Variables:
         * **authentication** -- instance of
           "litle_sdk_python.fields.authentication"

         * **loggedInUser** -- String or Number

         * **merchantId** -- String or Number

         * **merchantSdk** -- String or Number

         * **recurringTransaction** -- String or Number

         * **transaction** -- String or Number

         * **version** -- String or Number


litleRequest
------------

   class litle_sdk_python.fields.litleRequest

      Variables:
         * **RFRRequest** -- instance of
           "litle_sdk_python.fields.RFRRequest"

         * **authentication** -- instance of
           "litle_sdk_python.fields.authentication"

         * **batchRequest** -- instance of
           "litle_sdk_python.fields.batchRequest"

         * **id** -- String or Number

         * **numBatchRequests** -- String or Number

         * **version** -- String or Number


merchantDataType
----------------

   class litle_sdk_python.fields.merchantDataType

      Variables:
         * **affiliate** -- String or Number

         * **campaign** -- String or Number

         * **merchantGroupingId** -- String or Number


mposType
--------

   class litle_sdk_python.fields.mposType

      Variables:
         * **encryptedTrack** -- String or Number

         * **formatId** -- String or Number

         * **ksn** -- String or Number

         * **track1Status** -- String or Number

         * **track2Status** -- String or Number


networkField
------------

   class litle_sdk_python.fields.networkField

      Variables:
         * **fieldName** -- String or Number

         * **fieldNumber** -- String or Number

         * **fieldValue** -- String or Number

         * **networkSubField** -- instance of
           "litle_sdk_python.fields.networkSubField"


networkSubField
---------------

   class litle_sdk_python.fields.networkSubField

      Variables:
         * **fieldNumber** -- String or Number

         * **fieldValue** -- String or Number


payPal
------

   class litle_sdk_python.fields.payPal

      Variables:
         * **payerEmail** -- String or Number

         * **payerId** -- String or Number

         * **token** -- instance of
           "litle_sdk_python.fields.cardTokenType"

         * **transactionId** -- String or Number


pos
---

   class litle_sdk_python.fields.pos

      Variables:
         * **capability** -- String or Number

         * **cardholderId** -- String or Number

         * **catLevel** -- String or Number

         * **entryMode** -- String or Number

         * **terminalId** -- String or Number


processingInstructions
----------------------

   class litle_sdk_python.fields.processingInstructions

      Variables:
         **bypassVelocityCheck** -- String or Number


recurringRequestType
--------------------

   class litle_sdk_python.fields.recurringRequestType

      Variables:
         **subscription** -- String or Number


recurringSubscriptionType
-------------------------

   class litle_sdk_python.fields.recurringSubscriptionType

      Variables:
         * **amount** -- String or Number

         * **createAddOn** -- String or Number

         * **createDiscount** -- String or Number

         * **numberOfPayments** -- String or Number

         * **planCode** -- String or Number

         * **startDate** -- String or Number


recurringTransactionType
------------------------

   class litle_sdk_python.fields.recurringTransactionType


recycleAdviceType
-----------------

   class litle_sdk_python.fields.recycleAdviceType

      Variables:
         * **nextRecycleTime** -- String or Number

         * **recycleAdviceEnd** -- String or Number


recyclingRequestType
--------------------

   class litle_sdk_python.fields.recyclingRequestType

      Variables:
         * **recycleBy** -- String or Number

         * **recycleId** -- String or Number


recyclingType
-------------

   class litle_sdk_python.fields.recyclingType

      Variables:
         * **recycleAdvice** -- String or Number

         * **recycleEngineActive** -- String or Number


registerTokenRequestType
------------------------

   class litle_sdk_python.fields.registerTokenRequestType

      Variables:
         * **accountNumber** -- String or Number

         * **applepay** -- String or Number

         * **cardValidationNum** -- String or Number

         * **customerId** -- String or Number

         * **echeckForToken** -- String or Number

         * **id** -- String or Number

         * **mpos** -- String or Number

         * **orderId** -- String or Number

         * **paypageRegistrationId** -- String or Number

         * **reportGroup** -- String or Number


sepaDirectDebitType
-------------------

   class litle_sdk_python.fields.sepaDirectDebitType

      Variables:
         * **iban** -- String or Number

         * **mandateProvider** -- String or Number

         * **mandateReference** -- String or Number

         * **mandateSignatureDate** -- String or Number

         * **mandateUrl** -- String or Number

         * **preferredLanguage** -- String or Number

         * **sequenceType** -- String or Number


transactionType
---------------

   class litle_sdk_python.fields.transactionType

      Variables:
         * **customerId** -- String or Number

         * **id** -- String or Number


transactionTypeOptionReportGroup
--------------------------------

   class litle_sdk_python.fields.transactionTypeOptionReportGroup

      Variables:
         * **customerId** -- String or Number

         * **id** -- String or Number

         * **reportGroup** -- String or Number


transactionTypeWithReportGroup
------------------------------

   class litle_sdk_python.fields.transactionTypeWithReportGroup

      Variables:
         * **customerId** -- String or Number

         * **id** -- String or Number

         * **reportGroup** -- String or Number


transactionTypeWithReportGroupAndPartial
----------------------------------------

   class litle_sdk_python.fields.transactionTypeWithReportGroupAndPartial

      Variables:
         * **customerId** -- String or Number

         * **id** -- String or Number

         * **partial** -- String or Number

         * **reportGroup** -- String or Number


updateAddOnType
---------------

   class litle_sdk_python.fields.updateAddOnType

      Variables:
         * **addOnCode** -- String or Number

         * **amount** -- String or Number

         * **endDate** -- String or Number

         * **name** -- String or Number

         * **startDate** -- String or Number


updateCardValidationNumOnToken
------------------------------

   class litle_sdk_python.fields.updateCardValidationNumOnToken_

      Variables:
         * **cardValidationNum** -- String or Number

         * **customerId** -- String or Number

         * **id** -- String or Number

         * **litleToken** -- String or Number

         * **orderId** -- String or Number

         * **reportGroup** -- String or Number


updateDiscountType
------------------

   class litle_sdk_python.fields.updateDiscountType

      Variables:
         * **amount** -- String or Number

         * **discountCode** -- String or Number

         * **endDate** -- String or Number

         * **name** -- String or Number

         * **startDate** -- String or Number


updatePlan
----------

   class litle_sdk_python.fields.updatePlan

      Variables:
         * **active** -- String or Number

         * **planCode** -- String or Number


updateSubscription
------------------

   class litle_sdk_python.fields.updateSubscription

      Variables:
         * **billToAddress** -- instance of
           "litle_sdk_python.fields.contact"

         * **billingDate** -- String or Number

         * **card** -- instance of
           "litle_sdk_python.fields.cardType"

         * **createAddOn** -- String or Number

         * **createDiscount** -- String or Number

         * **deleteAddOn** -- String or Number

         * **deleteDiscount** -- String or Number

         * **paypage** -- String or Number

         * **planCode** -- String or Number

         * **subscriptionId** -- String or Number

         * **token** -- instance of
           "litle_sdk_python.fields.cardTokenType"

         * **updateAddOn** -- String or Number

         * **updateDiscount** -- String or Number


virtualGiftCardType
-------------------

   class litle_sdk_python.fields.virtualGiftCardType

      Variables:
         * **accountNumberLength** -- String or Number

         * **giftCardBin** -- String or Number


wallet
------

   class litle_sdk_python.fields.wallet

      Variables:
         * **walletSourceType** -- String or Number

         * **walletSourceTypeId** -- String or Number
