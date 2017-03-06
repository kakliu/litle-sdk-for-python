Vantiv eCommerce Python SDK's documentation 9.10!
==================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Batch
------
batch.stream
............
    .. autofunction:: litle_sdk_python.batch.stream

batch.download
..............
    .. autofunction:: litle_sdk_python.batch.download

batch.submit
............
    .. autofunction:: litle_sdk_python.batch.submit

batch.retrieve
..............
    .. autofunction:: litle_sdk_python.batch.retrieve

batch.Transactions
..................
    .. autoclass:: litle_sdk_python.batch.Transactions
        :members:

Configuration
-------------
    .. autoclass:: litle_sdk_python.utils.Configuration
        :members:

Online
------
    .. autofunction:: litle_sdk_python.online.request

Transactions
------------
accountUpdate
.............
    .. py:class:: litle_sdk_python.fields.accountUpdate

        :var cardOrToken: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var reportGroup: String or Number

activate
........
    .. py:class:: litle_sdk_python.fields.activate

        :var amount: String or Number
        :var card: instance of :py:class:`litle_sdk_python.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number
        :var virtualGiftCard: String or Number

activateReversal
................
    .. py:class:: litle_sdk_python.fields.activateReversal

        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var reportGroup: String or Number

authReversal
............
    .. py:class:: litle_sdk_python.fields.authReversal

        :var actionReason: String or Number
        :var amount: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var payPalNotes: String or Number
        :var reportGroup: String or Number
        :var surchargeAmount: String or Number

authorization
.............
    .. py:class:: litle_sdk_python.fields.authorization

        :var advancedFraudChecks: String or Number
        :var allowPartialAuth: String or Number
        :var amexAggregatorData: instance of :py:class:`litle_sdk_python.fields.amexAggregatorData`
        :var amount: String or Number
        :var applepay: String or Number
        :var billMeLaterRequest: instance of :py:class:`litle_sdk_python.fields.billMeLaterRequest`
        :var billToAddress: instance of :py:class:`litle_sdk_python.fields.contact`
        :var card: instance of :py:class:`litle_sdk_python.fields.cardType`
        :var cardholderAuthentication: String or Number
        :var customBilling: instance of :py:class:`litle_sdk_python.fields.customBilling`
        :var customerId: String or Number
        :var customerInfo: instance of :py:class:`litle_sdk_python.fields.customerInfo`
        :var debtRepayment: String or Number
        :var enhancedData: instance of :py:class:`litle_sdk_python.fields.enhancedData`
        :var filtering: String or Number
        :var fraudFilterOverride: String or Number
        :var healthcareIIAS: instance of :py:class:`litle_sdk_python.fields.healthcareIIAS`
        :var id: String or Number
        :var litleTxnId: String or Number
        :var merchantData: String or Number
        :var mpos: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var originalNetworkTransactionId: String or Number
        :var originalTransactionAmount: String or Number
        :var paypage: String or Number
        :var paypal: String or Number
        :var pos: instance of :py:class:`litle_sdk_python.fields.pos`
        :var processingInstructions: instance of :py:class:`litle_sdk_python.fields.processingInstructions`
        :var processingType: String or Number
        :var recurringRequest: String or Number
        :var recyclingRequest: String or Number
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number
        :var shipToAddress: instance of :py:class:`litle_sdk_python.fields.contact`
        :var surchargeAmount: String or Number
        :var taxType: String or Number
        :var token: instance of :py:class:`litle_sdk_python.fields.cardTokenType`
        :var wallet: instance of :py:class:`litle_sdk_python.fields.wallet`

balanceInquiry
..............
    .. py:class:: litle_sdk_python.fields.balanceInquiry

        :var card: instance of :py:class:`litle_sdk_python.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

capture
.......
    .. py:class:: litle_sdk_python.fields.capture

        :var amount: String or Number
        :var customBilling: instance of :py:class:`litle_sdk_python.fields.customBilling`
        :var customerId: String or Number
        :var enhancedData: instance of :py:class:`litle_sdk_python.fields.enhancedData`
        :var id: String or Number
        :var litleTxnId: String or Number
        :var partial: String or Number
        :var payPalNotes: String or Number
        :var payPalOrderComplete: String or Number
        :var pin: String or Number
        :var processingInstructions: instance of :py:class:`litle_sdk_python.fields.processingInstructions`
        :var reportGroup: String or Number
        :var surchargeAmount: String or Number

captureGivenAuth
................
    .. py:class:: litle_sdk_python.fields.captureGivenAuth

        :var amexAggregatorData: instance of :py:class:`litle_sdk_python.fields.amexAggregatorData`
        :var amount: String or Number
        :var authInformation: instance of :py:class:`litle_sdk_python.fields.authInformation`
        :var billMeLaterRequest: instance of :py:class:`litle_sdk_python.fields.billMeLaterRequest`
        :var billToAddress: instance of :py:class:`litle_sdk_python.fields.contact`
        :var card: instance of :py:class:`litle_sdk_python.fields.cardType`
        :var customBilling: instance of :py:class:`litle_sdk_python.fields.customBilling`
        :var customerId: String or Number
        :var debtRepayment: String or Number
        :var enhancedData: instance of :py:class:`litle_sdk_python.fields.enhancedData`
        :var id: String or Number
        :var merchantData: String or Number
        :var mpos: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var originalNetworkTransactionId: String or Number
        :var originalTransactionAmount: String or Number
        :var paypage: String or Number
        :var pos: instance of :py:class:`litle_sdk_python.fields.pos`
        :var processingInstructions: instance of :py:class:`litle_sdk_python.fields.processingInstructions`
        :var processingType: String or Number
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number
        :var shipToAddress: instance of :py:class:`litle_sdk_python.fields.contact`
        :var surchargeAmount: String or Number
        :var taxType: String or Number
        :var token: instance of :py:class:`litle_sdk_python.fields.cardTokenType`

credit
......
    .. py:class:: litle_sdk_python.fields.credit

        :var actionReason: String or Number
        :var amexAggregatorData: instance of :py:class:`litle_sdk_python.fields.amexAggregatorData`
        :var amount: String or Number
        :var billMeLaterRequest: instance of :py:class:`litle_sdk_python.fields.billMeLaterRequest`
        :var billToAddress: instance of :py:class:`litle_sdk_python.fields.contact`
        :var card: instance of :py:class:`litle_sdk_python.fields.cardType`
        :var customBilling: instance of :py:class:`litle_sdk_python.fields.customBilling`
        :var customerId: String or Number
        :var enhancedData: instance of :py:class:`litle_sdk_python.fields.enhancedData`
        :var id: String or Number
        :var litleTxnId: String or Number
        :var merchantData: String or Number
        :var mpos: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var payPalNotes: String or Number
        :var paypage: String or Number
        :var paypal: String or Number
        :var pin: String or Number
        :var pos: instance of :py:class:`litle_sdk_python.fields.pos`
        :var processingInstructions: instance of :py:class:`litle_sdk_python.fields.processingInstructions`
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number
        :var surchargeAmount: String or Number
        :var taxType: String or Number
        :var token: instance of :py:class:`litle_sdk_python.fields.cardTokenType`

deactivate
..........
    .. py:class:: litle_sdk_python.fields.deactivate

        :var card: instance of :py:class:`litle_sdk_python.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

deactivateReversal
..................
    .. py:class:: litle_sdk_python.fields.deactivateReversal

        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var reportGroup: String or Number

depositReversal
...............
    .. py:class:: litle_sdk_python.fields.depositReversal

        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var reportGroup: String or Number

echeckCredit
............
    .. py:class:: litle_sdk_python.fields.echeckCredit

        :var amount: String or Number
        :var billToAddress: instance of :py:class:`litle_sdk_python.fields.contact`
        :var customBilling: instance of :py:class:`litle_sdk_python.fields.customBilling`
        :var customerId: String or Number
        :var echeckOrEcheckToken: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var merchantData: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number

echeckPreNoteCredit
...................
    .. py:class:: litle_sdk_python.fields.echeckPreNoteCredit

        :var billToAddress: instance of :py:class:`litle_sdk_python.fields.contact`
        :var customerId: String or Number
        :var echeck: instance of :py:class:`litle_sdk_python.fields.echeckType`
        :var id: String or Number
        :var merchantData: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

echeckPreNoteSale
.................
    .. py:class:: litle_sdk_python.fields.echeckPreNoteSale

        :var billToAddress: instance of :py:class:`litle_sdk_python.fields.contact`
        :var customerId: String or Number
        :var echeck: instance of :py:class:`litle_sdk_python.fields.echeckType`
        :var id: String or Number
        :var merchantData: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

echeckRedeposit
...............
    .. py:class:: litle_sdk_python.fields.echeckRedeposit

        :var customerId: String or Number
        :var echeckOrEcheckToken: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var merchantData: String or Number
        :var reportGroup: String or Number

echeckSale
..........
    .. py:class:: litle_sdk_python.fields.echeckSale

        :var amount: String or Number
        :var billToAddress: instance of :py:class:`litle_sdk_python.fields.contact`
        :var customBilling: instance of :py:class:`litle_sdk_python.fields.customBilling`
        :var customerId: String or Number
        :var echeckOrEcheckToken: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var merchantData: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number
        :var shipToAddress: instance of :py:class:`litle_sdk_python.fields.contact`
        :var verify: String or Number

echeckVerification
..................
    .. py:class:: litle_sdk_python.fields.echeckVerification

        :var amount: String or Number
        :var billToAddress: instance of :py:class:`litle_sdk_python.fields.contact`
        :var customerId: String or Number
        :var echeckOrEcheckToken: String or Number
        :var id: String or Number
            :var litleTxnId: String or Number
        :var merchantData: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

echeckVoid
..........
    .. py:class:: litle_sdk_python.fields.echeckVoid

        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var reportGroup: String or Number

forceCapture
............
    .. py:class:: litle_sdk_python.fields.forceCapture

        :var amexAggregatorData: instance of :py:class:`litle_sdk_python.fields.amexAggregatorData`
        :var amount: String or Number
        :var billToAddress: instance of :py:class:`litle_sdk_python.fields.contact`
        :var card: instance of :py:class:`litle_sdk_python.fields.cardType`
        :var customBilling: instance of :py:class:`litle_sdk_python.fields.customBilling`
        :var customerId: String or Number
        :var debtRepayment: String or Number
        :var enhancedData: instance of :py:class:`litle_sdk_python.fields.enhancedData`
        :var id: String or Number
        :var merchantData: String or Number
        :var mpos: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var paypage: String or Number
        :var pos: instance of :py:class:`litle_sdk_python.fields.pos`
        :var processingInstructions: instance of :py:class:`litle_sdk_python.fields.processingInstructions`
        :var processingType: String or Number
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number
        :var surchargeAmount: String or Number
        :var taxType: String or Number
        :var token: instance of :py:class:`litle_sdk_python.fields.cardTokenType`

fraudCheck
..........
    .. py:class:: litle_sdk_python.fields.fraudCheck

        :var advancedFraudChecks: String or Number
        :var amount: String or Number
        :var billToAddress: instance of :py:class:`litle_sdk_python.fields.contact`
        :var customerId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number
        :var shipToAddress: instance of :py:class:`litle_sdk_python.fields.contact`

load
....
    .. py:class:: litle_sdk_python.fields.load

        :var amount: String or Number
        :var card: instance of :py:class:`litle_sdk_python.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

loadReversal
............
    .. py:class:: litle_sdk_python.fields.loadReversal

        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var reportGroup: String or Number

payFacCredit
............
    .. py:class:: litle_sdk_python.fields.payFacCredit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

payFacDebit
...........
    .. py:class:: litle_sdk_python.fields.payFacDebit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

physicalCheckCredit
...................
    .. py:class:: litle_sdk_python.fields.physicalCheckCredit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

physicalCheckDebit
..................
    .. py:class:: litle_sdk_python.fields.physicalCheckDebit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

queryTransaction
................
    .. py:class:: litle_sdk_python.fields.queryTransaction

        :var customerId: String or Number
        :var id: String or Number
            :var origAccountNumber: String or Number
        :var origActionType: String or Number
        :var origId: String or Number
        :var origLitleTxnId: String or Number
            :var origOrderId: String or Number
        :var reportGroup: String or Number

refundReversal
..............
    .. py:class:: litle_sdk_python.fields.refundReversal

        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var reportGroup: String or Number

reserveCredit
.............
    .. py:class:: litle_sdk_python.fields.reserveCredit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

reserveDebit
............
    .. py:class:: litle_sdk_python.fields.reserveDebit

        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

sale
....
    .. py:class:: litle_sdk_python.fields.sale

        :var advancedFraudChecks: String or Number
        :var allowPartialAuth: String or Number
        :var amexAggregatorData: instance of :py:class:`litle_sdk_python.fields.amexAggregatorData`
        :var amount: String or Number
        :var applepay: String or Number
        :var billMeLaterRequest: instance of :py:class:`litle_sdk_python.fields.billMeLaterRequest`
        :var billToAddress: instance of :py:class:`litle_sdk_python.fields.contact`
        :var card: instance of :py:class:`litle_sdk_python.fields.cardType`
        :var cardholderAuthentication: String or Number
        :var customBilling: instance of :py:class:`litle_sdk_python.fields.customBilling`
        :var customerId: String or Number
        :var customerInfo: instance of :py:class:`litle_sdk_python.fields.customerInfo`
        :var debtRepayment: String or Number
        :var enhancedData: instance of :py:class:`litle_sdk_python.fields.enhancedData`
        :var filtering: String or Number
        :var fraudCheck: instance of :py:class:`litle_sdk_python.fields.fraudCheck`
        :var fraudFilterOverride: String or Number
        :var healthcareIIAS: instance of :py:class:`litle_sdk_python.fields.healthcareIIAS`
        :var id: String or Number
        :var litleInternalRecurringRequest: String or Number
        :var litleTxnId: String or Number
        :var merchantData: String or Number
        :var mpos: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var originalNetworkTransactionId: String or Number
        :var originalTransactionAmount: String or Number
        :var payPalNotes: String or Number
        :var payPalOrderComplete: String or Number
        :var paypage: String or Number
        :var paypal: String or Number
        :var pos: instance of :py:class:`litle_sdk_python.fields.pos`
        :var processingInstructions: instance of :py:class:`litle_sdk_python.fields.processingInstructions`
        :var processingType: String or Number
        :var recurringRequest: String or Number
        :var recyclingRequest: String or Number
        :var reportGroup: String or Number
        :var secondaryAmount: String or Number
        :var shipToAddress: instance of :py:class:`litle_sdk_python.fields.contact`
        :var surchargeAmount: String or Number
        :var taxType: String or Number
        :var token: instance of :py:class:`litle_sdk_python.fields.cardTokenType`
        :var wallet: instance of :py:class:`litle_sdk_python.fields.wallet`

submerchantCredit
.................
    .. py:class:: litle_sdk_python.fields.submerchantCredit

        :var accountInfo: String or Number
        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number
        :var submerchantName: String or Number

submerchantDebit
................
    .. py:class:: litle_sdk_python.fields.submerchantDebit

        :var accountInfo: String or Number
        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number
        :var submerchantName: String or Number

unload
......
    .. py:class:: litle_sdk_python.fields.unload

        :var amount: String or Number
        :var card: instance of :py:class:`litle_sdk_python.fields.cardType`
        :var customerId: String or Number
        :var id: String or Number
        :var orderId: String or Number
        :var orderSource: String or Number
        :var reportGroup: String or Number

unloadReversal
..............
    .. py:class:: litle_sdk_python.fields.unloadReversal

        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var reportGroup: String or Number

vendorCredit
............
    .. py:class:: litle_sdk_python.fields.vendorCredit

        :var accountInfo: String or Number
        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number
        :var vendorName: String or Number

vendorDebit
...........
    .. py:class:: litle_sdk_python.fields.vendorDebit

        :var accountInfo: String or Number
        :var amount: String or Number
        :var customerId: String or Number
        :var fundingSubmerchantId: String or Number
        :var fundsTransferId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number
        :var vendorName: String or Number

void
....
    .. py:class:: litle_sdk_python.fields.void

        :var customerId: String or Number
        :var id: String or Number
        :var litleTxnId: String or Number
        :var processingInstructions: instance of :py:class:`litle_sdk_python.fields.processingInstructions`
        :var reportGroup: String or Number

Complex Types
-------------
CTD_ANON_15
...........
    .. py:class:: litle_sdk_python.fields.CTD_ANON_15

        :var availableBalance: String or Number
        :var prepaidCardType: String or Number
        :var reloadable: String or Number
        :var type: String or Number

CTD_ANON_31
...........
    .. py:class:: litle_sdk_python.fields.CTD_ANON_31

        :var transactionResponse: String or Number

RFRRequest
..........
    .. py:class:: litle_sdk_python.fields.RFRRequest

        :var accountUpdateFileRequestData: instance of :py:class:`litle_sdk_python.fields.accountUpdateFileRequestData`
        :var litleSessionId: String or Number

accountInfoType
...............
    .. py:class:: litle_sdk_python.fields.accountInfoType

        :var number: String or Number
        :var type: String or Number

accountUpdateFileRequestData
............................
    .. py:class:: litle_sdk_python.fields.accountUpdateFileRequestData

        :var merchantId: String or Number
        :var postDay: String or Number

accountUpdater
..............
    .. py:class:: litle_sdk_python.fields.accountUpdater

        :var extendedCardResponse: String or Number
        :var newAccountInfo: String or Number
        :var newCardInfo: String or Number
        :var newCardTokenInfo: String or Number
        :var newTokenInfo: String or Number
        :var originalAccountInfo: String or Number
        :var originalCardInfo: String or Number
        :var originalCardTokenInfo: String or Number
        :var originalTokenInfo: String or Number

advancedFraudChecksType
.......................
    .. py:class:: litle_sdk_python.fields.advancedFraudChecksType

        :var customAttribute1: String or Number
        :var customAttribute2: String or Number
        :var customAttribute3: String or Number
        :var customAttribute4: String or Number
        :var customAttribute5: String or Number
        :var threatMetrixSessionId: String or Number

advancedFraudResultsType
........................
    .. py:class:: litle_sdk_python.fields.advancedFraudResultsType

        :var deviceReputationScore: String or Number
        :var deviceReviewStatus: String or Number
        :var triggeredRule: String or Number

amexAggregatorData
..................
    .. py:class:: litle_sdk_python.fields.amexAggregatorData

        :var sellerId: String or Number
        :var sellerMerchantCategoryCode: String or Number

applepayHeaderType
..................
    .. py:class:: litle_sdk_python.fields.applepayHeaderType

        :var applicationData: String or Number
        :var ephemeralPublicKey: String or Number
        :var publicKeyHash: String or Number
        :var transactionId: String or Number

applepayType
............
    .. py:class:: litle_sdk_python.fields.applepayType

        :var data: String or Number
        :var header: String or Number
        :var signature: String or Number
        :var version: String or Number

authInformation
...............
    .. py:class:: litle_sdk_python.fields.authInformation

        :var authAmount: String or Number
        :var authCode: String or Number
        :var authDate: String or Number
        :var fraudResult: instance of :py:class:`litle_sdk_python.fields.fraudResult`

authentication
..............
    .. py:class:: litle_sdk_python.fields.authentication

        :var password: String or Number
        :var user: String or Number

baseRequest
...........
    .. py:class:: litle_sdk_python.fields.baseRequest

        :var authentication: instance of :py:class:`litle_sdk_python.fields.authentication`
        :var recurringTransaction: String or Number
        :var transaction: String or Number
        :var version: String or Number

batchRequest
............
    .. py:class:: litle_sdk_python.fields.batchRequest

        :var activateAmount: String or Number
        :var authAmount: String or Number
        :var authReversalAmount: String or Number
        :var captureAmount: String or Number
        :var captureGivenAuthAmount: String or Number
        :var creditAmount: String or Number
        :var echeckCreditAmount: String or Number
        :var echeckSalesAmount: String or Number
        :var echeckVerificationAmount: String or Number
        :var extCaptureAmount: String or Number
        :var forceCaptureAmount: String or Number
        :var id: String or Number
        :var loadAmount: String or Number
        :var merchantId: String or Number
        :var merchantSdk: String or Number
        :var numAccountUpdates: String or Number
        :var numActivates: String or Number
        :var numAuthReversals: String or Number
        :var numAuths: String or Number
        :var numBalanceInquirys: String or Number
        :var numCancelSubscriptions: String or Number
        :var numCaptureGivenAuths: String or Number
        :var numCaptures: String or Number
        :var numCreatePlans: String or Number
        :var numCredits: String or Number
        :var numDeactivates: String or Number
        :var numEcheckCredit: String or Number
        :var numEcheckPreNoteCredit: String or Number
        :var numEcheckPreNoteSale: String or Number
        :var numEcheckRedeposit: String or Number
        :var numEcheckSales: String or Number
        :var numEcheckVerification: String or Number
        :var numExtCaptures: String or Number
        :var numForceCaptures: String or Number
        :var numLoads: String or Number
        :var numPayFacCredit: String or Number
        :var numPayFacDebit: String or Number
        :var numPhysicalCheckCredit: String or Number
        :var numPhysicalCheckDebit: String or Number
        :var numReserveCredit: String or Number
        :var numReserveDebit: String or Number
        :var numSales: String or Number
        :var numSubmerchantCredit: String or Number
        :var numSubmerchantDebit: String or Number
        :var numTokenRegistrations: String or Number
        :var numUnloads: String or Number
        :var numUpdateCardValidationNumOnTokens: String or Number
        :var numUpdatePlans: String or Number
        :var numUpdateSubscriptions: String or Number
        :var numVendorCredit: String or Number
        :var numVendorDebit: String or Number
        :var payFacCreditAmount: String or Number
        :var payFacDebitAmount: String or Number
        :var physicalCheckCreditAmount: String or Number
        :var physicalCheckDebitAmount: String or Number
        :var recurringTransaction: String or Number
        :var reserveCreditAmount: String or Number
        :var reserveDebitAmount: String or Number
        :var saleAmount: String or Number
        :var submerchantCreditAmount: String or Number
        :var submerchantDebitAmount: String or Number
        :var transaction: String or Number
        :var unloadAmount: String or Number
        :var vendorCreditAmount: String or Number
        :var vendorDebitAmount: String or Number

billMeLaterRequest
..................
    .. py:class:: litle_sdk_python.fields.billMeLaterRequest

        :var authorizationSourcePlatform: String or Number
        :var bmlMerchantId: String or Number
        :var bmlProductType: String or Number
        :var customerBillingAddressChanged: String or Number
        :var customerEmailChanged: String or Number
        :var customerPasswordChanged: String or Number
        :var customerPhoneChanged: String or Number
        :var itemCategoryCode: String or Number
        :var merchantPromotionalCode: String or Number
        :var preapprovalNumber: String or Number
        :var secretQuestionAnswer: String or Number
        :var secretQuestionCode: String or Number
        :var termsAndConditions: String or Number
        :var virtualAuthenticationKeyData: String or Number
        :var virtualAuthenticationKeyPresenceIndicator: String or Number

cancelSubscription
..................
    .. py:class:: litle_sdk_python.fields.cancelSubscription

        :var subscriptionId: String or Number

cardAccountInfoType
...................
    .. py:class:: litle_sdk_python.fields.cardAccountInfoType

        :var expDate: String or Number
        :var number: String or Number
        :var type: String or Number

cardPaypageType
...............
    .. py:class:: litle_sdk_python.fields.cardPaypageType

        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var paypageRegistrationId: String or Number
        :var type: String or Number

cardTokenInfoType
.................
    .. py:class:: litle_sdk_python.fields.cardTokenInfoType

        :var bin: String or Number
        :var expDate: String or Number
        :var litleToken: String or Number
        :var type: String or Number

cardTokenType
.............
    .. py:class:: litle_sdk_python.fields.cardTokenType

        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var litleToken: String or Number
        :var type: String or Number

cardTokenTypeAU
...............
    .. py:class:: litle_sdk_python.fields.cardTokenTypeAU

        :var bin: String or Number
        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var litleToken: String or Number
        :var type: String or Number

cardType
........
    .. py:class:: litle_sdk_python.fields.cardType

        :var cardValidationNum: String or Number
        :var expDate: String or Number
        :var number: String or Number
        :var pin: String or Number
        :var track: String or Number
        :var type: String or Number

contact
.......
    .. py:class:: litle_sdk_python.fields.contact

        :var addressLine1: String or Number
        :var addressLine2: String or Number
        :var addressLine3: String or Number
        :var city: String or Number
        :var companyName: String or Number
        :var country: String or Number
        :var email: String or Number
        :var firstName: String or Number
        :var lastName: String or Number
        :var middleInitial: String or Number
        :var name: String or Number
        :var phone: String or Number
        :var state: String or Number
        :var zip: String or Number

createAddOnType
...............
    .. py:class:: litle_sdk_python.fields.createAddOnType

        :var addOnCode: String or Number
        :var amount: String or Number
        :var endDate: String or Number
        :var name: String or Number
        :var startDate: String or Number

createDiscountType
..................
    .. py:class:: litle_sdk_python.fields.createDiscountType

        :var amount: String or Number
        :var discountCode: String or Number
        :var endDate: String or Number
        :var name: String or Number
        :var startDate: String or Number

createPlan
..........
    .. py:class:: litle_sdk_python.fields.createPlan

        :var active: String or Number
        :var amount: String or Number
        :var description: String or Number
        :var intervalType: String or Number
        :var name: String or Number
        :var numberOfPayments: String or Number
        :var planCode: String or Number
        :var trialIntervalType: String or Number
        :var trialNumberOfIntervals: String or Number

customBilling
.............
    .. py:class:: litle_sdk_python.fields.customBilling

        :var city: String or Number
        :var descriptor: String or Number
        :var phone: String or Number
        :var url: String or Number

customerInfo
............
    .. py:class:: litle_sdk_python.fields.customerInfo

        :var customerCheckingAccount: String or Number
        :var customerRegistrationDate: String or Number
        :var customerSavingAccount: String or Number
        :var customerType: String or Number
        :var customerWorkTelephone: String or Number
        :var dob: String or Number
        :var employerName: String or Number
        :var incomeAmount: String or Number
        :var incomeCurrency: String or Number
        :var residenceStatus: String or Number
        :var ssn: String or Number
        :var yearsAtEmployer: String or Number
        :var yearsAtResidence: String or Number

deleteAddOnType
...............
    .. py:class:: litle_sdk_python.fields.deleteAddOnType

        :var addOnCode: String or Number

deleteDiscountType
..................
    .. py:class:: litle_sdk_python.fields.deleteDiscountType

        :var discountCode: String or Number

detailTax
.........
    .. py:class:: litle_sdk_python.fields.detailTax

        :var cardAcceptorTaxId: String or Number
        :var taxAmount: String or Number
        :var taxIncludedInTotal: String or Number
        :var taxRate: String or Number
        :var taxTypeIdentifier: String or Number

driversLicenseInfo
..................
    .. py:class:: litle_sdk_python.fields.driversLicenseInfo

        :var dateOfBirth: String or Number
        :var licenseNumber: String or Number
        :var state: String or Number

echeckAccountInfoType
.....................
    .. py:class:: litle_sdk_python.fields.echeckAccountInfoType

        :var accNum: String or Number
        :var accType: String or Number
        :var routingNum: String or Number

echeckForTokenType
..................
    .. py:class:: litle_sdk_python.fields.echeckForTokenType

        :var accNum: String or Number
        :var routingNum: String or Number

echeckTokenInfoType
...................
    .. py:class:: litle_sdk_python.fields.echeckTokenInfoType

        :var accType: String or Number
        :var litleToken: String or Number
        :var routingNum: String or Number

echeckTokenType
...............
    .. py:class:: litle_sdk_python.fields.echeckTokenType

        :var accType: String or Number
        :var checkNum: String or Number
        :var litleToken: String or Number
        :var routingNum: String or Number

echeckType
..........
    .. py:class:: litle_sdk_python.fields.echeckType

        :var accNum: String or Number
        :var accType: String or Number
        :var ccdPaymentInformation: String or Number
        :var checkNum: String or Number
        :var routingNum: String or Number

enhancedData
............
    .. py:class:: litle_sdk_python.fields.enhancedData

        :var customerReference: String or Number
        :var deliveryType: String or Number
        :var destinationCountryCode: String or Number
        :var destinationPostalCode: String or Number
        :var detailTax: instance of :py:class:`litle_sdk_python.fields.detailTax`
        :var discountAmount: String or Number
        :var dutyAmount: String or Number
        :var invoiceReferenceNumber: String or Number
        :var lineItemData: instance of :py:class:`litle_sdk_python.fields.lineItemData`
        :var orderDate: String or Number
        :var salesTax: String or Number
        :var shipFromPostalCode: String or Number
        :var shippingAmount: String or Number
        :var taxExempt: String or Number

filteringType
.............
    .. py:class:: litle_sdk_python.fields.filteringType

        :var chargeback: String or Number
        :var international: String or Number
        :var prepaid: String or Number

fraudCheckType
..............
    .. py:class:: litle_sdk_python.fields.fraudCheckType

        :var authenticatedByMerchant: String or Number
        :var authenticationTransactionId: String or Number
        :var authenticationValue: String or Number
        :var customerIpAddress: String or Number

fraudResult
...........
    .. py:class:: litle_sdk_python.fields.fraudResult

        :var advancedAVSResult: String or Number
        :var advancedFraudResults: String or Number
        :var authenticationResult: String or Number
        :var avsResult: String or Number
        :var cardValidationResult: String or Number

healthcareAmounts
.................
    .. py:class:: litle_sdk_python.fields.healthcareAmounts

        :var RxAmount: String or Number
        :var clinicOtherAmount: String or Number
        :var dentalAmount: String or Number
        :var totalHealthcareAmount: String or Number
        :var visionAmount: String or Number

healthcareIIAS
..............
    .. py:class:: litle_sdk_python.fields.healthcareIIAS

        :var IIASFlag: String or Number
        :var healthcareAmounts: instance of :py:class:`litle_sdk_python.fields.healthcareAmounts`

lineItemData
............
    .. py:class:: litle_sdk_python.fields.lineItemData

        :var commodityCode: String or Number
        :var detailTax: instance of :py:class:`litle_sdk_python.fields.detailTax`
        :var itemDescription: String or Number
        :var itemDiscountAmount: String or Number
        :var itemSequenceNumber: String or Number
        :var lineItemTotal: String or Number
        :var lineItemTotalWithTax: String or Number
        :var productCode: String or Number
        :var quantity: String or Number
        :var taxAmount: String or Number
        :var unitCost: String or Number
        :var unitOfMeasure: String or Number

litleInternalRecurringRequestType
.................................
    .. py:class:: litle_sdk_python.fields.litleInternalRecurringRequestType

        :var finalPayment: String or Number
        :var recurringTxnId: String or Number
        :var subscriptionId: String or Number

litleOnlineRequest
..................
    .. py:class:: litle_sdk_python.fields.litleOnlineRequest

        :var authentication: instance of :py:class:`litle_sdk_python.fields.authentication`
        :var loggedInUser: String or Number
        :var merchantId: String or Number
        :var merchantSdk: String or Number
        :var recurringTransaction: String or Number
        :var transaction: String or Number
        :var version: String or Number

litleRequest
............
    .. py:class:: litle_sdk_python.fields.litleRequest

        :var RFRRequest: instance of :py:class:`litle_sdk_python.fields.RFRRequest`
        :var authentication: instance of :py:class:`litle_sdk_python.fields.authentication`
        :var batchRequest: instance of :py:class:`litle_sdk_python.fields.batchRequest`
        :var id: String or Number
        :var numBatchRequests: String or Number
        :var version: String or Number

merchantDataType
................
    .. py:class:: litle_sdk_python.fields.merchantDataType

        :var affiliate: String or Number
        :var campaign: String or Number
        :var merchantGroupingId: String or Number

mposType
........
    .. py:class:: litle_sdk_python.fields.mposType

        :var encryptedTrack: String or Number
        :var formatId: String or Number
        :var ksn: String or Number
        :var track1Status: String or Number
        :var track2Status: String or Number

payPal
......
    .. py:class:: litle_sdk_python.fields.payPal

        :var payerEmail: String or Number
        :var payerId: String or Number
        :var token: instance of :py:class:`litle_sdk_python.fields.cardTokenType`
        :var transactionId: String or Number

pos
...
    .. py:class:: litle_sdk_python.fields.pos

        :var capability: String or Number
        :var cardholderId: String or Number
        :var catLevel: String or Number
        :var entryMode: String or Number
        :var terminalId: String or Number

processingInstructions
......................
    .. py:class:: litle_sdk_python.fields.processingInstructions

        :var bypassVelocityCheck: String or Number

recurringRequestType
....................
    .. py:class:: litle_sdk_python.fields.recurringRequestType

        :var subscription: String or Number

recurringSubscriptionType
.........................
    .. py:class:: litle_sdk_python.fields.recurringSubscriptionType

        :var amount: String or Number
        :var createAddOn: String or Number
        :var createDiscount: String or Number
        :var numberOfPayments: String or Number
        :var planCode: String or Number
        :var startDate: String or Number

recurringTransactionType
........................
    .. py:class:: litle_sdk_python.fields.recurringTransactionType


recycleAdviceType
.................
    .. py:class:: litle_sdk_python.fields.recycleAdviceType

        :var nextRecycleTime: String or Number
        :var recycleAdviceEnd: String or Number

recyclingRequestType
....................
    .. py:class:: litle_sdk_python.fields.recyclingRequestType

        :var recycleBy: String or Number
        :var recycleId: String or Number

recyclingType
.............
    .. py:class:: litle_sdk_python.fields.recyclingType

        :var recycleAdvice: String or Number
        :var recycleEngineActive: String or Number

registerTokenRequestType
........................
    .. py:class:: litle_sdk_python.fields.registerTokenRequestType

        :var accountNumber: String or Number
        :var applepay: String or Number
        :var cardValidationNum: String or Number
        :var customerId: String or Number
        :var echeckForToken: String or Number
        :var id: String or Number
        :var mpos: String or Number
        :var orderId: String or Number
        :var paypageRegistrationId: String or Number
        :var reportGroup: String or Number

transactionType
...............
    .. py:class:: litle_sdk_python.fields.transactionType

        :var customerId: String or Number
        :var id: String or Number

transactionTypeOptionReportGroup
................................
    .. py:class:: litle_sdk_python.fields.transactionTypeOptionReportGroup

        :var customerId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

transactionTypeWithReportGroup
..............................
    .. py:class:: litle_sdk_python.fields.transactionTypeWithReportGroup

        :var customerId: String or Number
        :var id: String or Number
        :var reportGroup: String or Number

transactionTypeWithReportGroupAndPartial
........................................
    .. py:class:: litle_sdk_python.fields.transactionTypeWithReportGroupAndPartial

        :var customerId: String or Number
        :var id: String or Number
        :var partial: String or Number
        :var reportGroup: String or Number

updateAddOnType
...............
    .. py:class:: litle_sdk_python.fields.updateAddOnType

        :var addOnCode: String or Number
        :var amount: String or Number
        :var endDate: String or Number
        :var name: String or Number
        :var startDate: String or Number

updateCardValidationNumOnToken_
...............................
    .. py:class:: litle_sdk_python.fields.updateCardValidationNumOnToken_

        :var cardValidationNum: String or Number
        :var customerId: String or Number
        :var id: String or Number
        :var litleToken: String or Number
        :var orderId: String or Number
        :var reportGroup: String or Number

updateDiscountType
..................
    .. py:class:: litle_sdk_python.fields.updateDiscountType

        :var amount: String or Number
        :var discountCode: String or Number
        :var endDate: String or Number
        :var name: String or Number
        :var startDate: String or Number

updatePlan
..........
    .. py:class:: litle_sdk_python.fields.updatePlan

        :var active: String or Number
        :var planCode: String or Number

updateSubscription
..................
    .. py:class:: litle_sdk_python.fields.updateSubscription

        :var billToAddress: instance of :py:class:`litle_sdk_python.fields.contact`
        :var billingDate: String or Number
        :var card: instance of :py:class:`litle_sdk_python.fields.cardType`
        :var createAddOn: String or Number
        :var createDiscount: String or Number
        :var deleteAddOn: String or Number
        :var deleteDiscount: String or Number
        :var paypage: String or Number
        :var planCode: String or Number
        :var subscriptionId: String or Number
        :var token: instance of :py:class:`litle_sdk_python.fields.cardTokenType`
        :var updateAddOn: String or Number
        :var updateDiscount: String or Number

virtualGiftCardType
...................
    .. py:class:: litle_sdk_python.fields.virtualGiftCardType

        :var accountNumberLength: String or Number
        :var giftCardBin: String or Number

wallet
......
    .. py:class:: litle_sdk_python.fields.wallet

        :var walletSourceType: String or Number
        :var walletSourceTypeId: String or Number

