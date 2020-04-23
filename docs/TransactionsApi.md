# swagger_client.TransactionsApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**broadcast_tx**](TransactionsApi.md#broadcast_tx) | **POST** /txs | Broadcast a signed tx
[**encode_tx**](TransactionsApi.md#encode_tx) | **POST** /txs/encode | Encode a transaction to the Amino wire format
[**get_tx_by_hash**](TransactionsApi.md#get_tx_by_hash) | **GET** /txs/{hash} | Get a Tx by hash
[**search_tx**](TransactionsApi.md#search_tx) | **GET** /txs | Search transactions


# **broadcast_tx**
> BroadcastTxCommitResult broadcast_tx(tx_broadcast)

Broadcast a signed tx

Broadcast a signed tx to a full node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
tx_broadcast = swagger_client.TxBroadcast() # TxBroadcast | The tx must be a signed StdTx. The supported broadcast modes include `\"block\"`(return after tx commit), `\"sync\"`(return afer CheckTx) and `\"async\"`(return right away).

try:
    # Broadcast a signed tx
    api_response = api_instance.broadcast_tx(tx_broadcast)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->broadcast_tx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_broadcast** | [**TxBroadcast**](TxBroadcast.md)| The tx must be a signed StdTx. The supported broadcast modes include &#x60;\&quot;block\&quot;&#x60;(return after tx commit), &#x60;\&quot;sync\&quot;&#x60;(return afer CheckTx) and &#x60;\&quot;async\&quot;&#x60;(return right away). | 

### Return type

[**BroadcastTxCommitResult**](BroadcastTxCommitResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **encode_tx**
> InlineResponse2003 encode_tx(tx)

Encode a transaction to the Amino wire format

Encode a transaction (signed or not) from JSON to base64-encoded Amino serialized bytes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
tx = swagger_client.Tx() # Tx | The tx to encode

try:
    # Encode a transaction to the Amino wire format
    api_response = api_instance.encode_tx(tx)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->encode_tx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx** | [**Tx**](Tx.md)| The tx to encode | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tx_by_hash**
> BroadcastTxCommitResult get_tx_by_hash(hash)

Get a Tx by hash

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
hash = 'hash_example' # str | Tx hash

try:
    # Get a Tx by hash
    api_response = api_instance.get_tx_by_hash(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_tx_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Tx hash | 

### Return type

[**BroadcastTxCommitResult**](BroadcastTxCommitResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tx**
> PaginatedQueryTxs search_tx(message_action=message_action, message_sender=message_sender, page=page, limit=limit)

Search transactions

Search transactions by events.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
message_action = 'message_action_example' # str | transaction events such as 'message.action=send' which results in the following endpoint: 'GET /txs?message.action=send' (optional)
message_sender = 'message_sender_example' # str | transaction tags with sender: 'GET /txs?message.action=send&message.sender=cosmos16xyempempp92x9hyzz9wrgf94r6j9h5f06pxxv' (optional)
page = 56 # int | Page number (optional)
limit = 56 # int | Maximum number of items per page (optional)

try:
    # Search transactions
    api_response = api_instance.search_tx(message_action=message_action, message_sender=message_sender, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->search_tx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_action** | **str**| transaction events such as &#39;message.action&#x3D;send&#39; which results in the following endpoint: &#39;GET /txs?message.action&#x3D;send&#39; | [optional] 
 **message_sender** | **str**| transaction tags with sender: &#39;GET /txs?message.action&#x3D;send&amp;message.sender&#x3D;cosmos16xyempempp92x9hyzz9wrgf94r6j9h5f06pxxv&#39; | [optional] 
 **page** | **int**| Page number | [optional] 
 **limit** | **int**| Maximum number of items per page | [optional] 

### Return type

[**PaginatedQueryTxs**](PaginatedQueryTxs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

