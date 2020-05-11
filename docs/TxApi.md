# dex_api_python.TxApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tx_from_trade_server**](TxApi.md#get_tx_from_trade_server) | **GET** /tx/txs/{hash} | Get a Tx from trade server by hash
[**query_income**](TxApi.md#query_income) | **GET** /tx/incomes | Query account all income until to given time
[**query_tx**](TxApi.md#query_tx) | **GET** /tx/txs | Query transactions


# **get_tx_from_trade_server**
> Tx get_tx_from_trade_server(hash)

Get a Tx from trade server by hash

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.TxApi()
hash = '2B6D7633C460DAABFCA47592B7F76A95CE95C52B515179C9E9BA49AA620377BA' # str | Tx hash

try:
    # Get a Tx from trade server by hash
    api_response = api_instance.get_tx_from_trade_server(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TxApi->get_tx_from_trade_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Tx hash | 

### Return type

[**Tx**](Tx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_income**
> InlineResponse20062 query_income(account, time, sid, count, token=token)

Query account all income until to given time

Query income info

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.TxApi()
account = 'account_example' # str | Bech32 address
time = 789 # int | Unix timestamp
sid = 789 # int | Sequence id
count = 56 # int | Querier count limited to 1024
token = 'token_example' # str | Symbol (optional)

try:
    # Query account all income until to given time
    api_response = api_instance.query_income(account, time, sid, count, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TxApi->query_income: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Bech32 address | 
 **time** | **int**| Unix timestamp | 
 **sid** | **int**| Sequence id | 
 **count** | **int**| Querier count limited to 1024 | 
 **token** | **str**| Symbol | [optional] 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_tx**
> InlineResponse20062 query_tx(account, time, sid, count, token=token)

Query transactions

Query transactions signed by given account until to given time

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.TxApi()
account = 'account_example' # str | Bech32 address
time = 789 # int | Unix timestamp
sid = 789 # int | Sequence id
count = 56 # int | Querier count limited to 1024
token = 'token_example' # str | Symbol (optional)

try:
    # Query transactions
    api_response = api_instance.query_tx(account, time, sid, count, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TxApi->query_tx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Bech32 address | 
 **time** | **int**| Unix timestamp | 
 **sid** | **int**| Sequence id | 
 **count** | **int**| Querier count limited to 1024 | 
 **token** | **str**| Symbol | [optional] 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

