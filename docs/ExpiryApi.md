# dex_api_python.ExpiryApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_redelegation**](ExpiryApi.md#query_redelegation) | **GET** /expiry/redelegations | Query redelegation
[**query_unbonding**](ExpiryApi.md#query_unbonding) | **GET** /expiry/unbondings | Query Unbonding
[**query_unlock**](ExpiryApi.md#query_unlock) | **GET** /expiry/unlocks | Query Unlock
[**querylocked**](ExpiryApi.md#querylocked) | **GET** /expiry/lockeds | Query lock tx


# **query_redelegation**
> InlineResponse20058 query_redelegation(account, time, sid, count)

Query redelegation

Query delegator's redelegation-completion info

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.ExpiryApi()
account = 'account_example' # str | Bech32 address
time = 789 # int | Unix timestamp
sid = 789 # int | Sequence id
count = 56 # int | Querier count limited to 1024

try:
    # Query redelegation
    api_response = api_instance.query_redelegation(account, time, sid, count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpiryApi->query_redelegation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Bech32 address | 
 **time** | **int**| Unix timestamp | 
 **sid** | **int**| Sequence id | 
 **count** | **int**| Querier count limited to 1024 | 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_unbonding**
> InlineResponse20059 query_unbonding(account, time, sid, count)

Query Unbonding

Query delegator's unbonding-completion info

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.ExpiryApi()
account = 'account_example' # str | Bech32 address
time = 789 # int | Unix timestamp
sid = 789 # int | Sequence id
count = 56 # int | Querier count

try:
    # Query Unbonding
    api_response = api_instance.query_unbonding(account, time, sid, count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpiryApi->query_unbonding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Bech32 address | 
 **time** | **int**| Unix timestamp | 
 **sid** | **int**| Sequence id | 
 **count** | **int**| Querier count | 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_unlock**
> InlineResponse20061 query_unlock(account, time, sid, count, token=token)

Query Unlock

Query Unlock info

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.ExpiryApi()
account = 'account_example' # str | Bech32 address
time = 789 # int | Unix timestamp
sid = 789 # int | Sequence id
count = 56 # int | Querier count
token = 'token_example' # str | Symbol (optional)

try:
    # Query Unlock
    api_response = api_instance.query_unlock(account, time, sid, count, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpiryApi->query_unlock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Bech32 address | 
 **time** | **int**| Unix timestamp | 
 **sid** | **int**| Sequence id | 
 **count** | **int**| Querier count | 
 **token** | **str**| Symbol | [optional] 

### Return type

[**InlineResponse20061**](InlineResponse20061.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **querylocked**
> InlineResponse20060 querylocked(account, time, sid, count, token=token)

Query lock tx

Query lock transfer info

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.ExpiryApi()
account = 'account_example' # str | Bech32 address
time = 789 # int | Unix timestamp
sid = 789 # int | Sequence id
count = 56 # int | Querier count
token = 'token_example' # str | Symbol (optional)

try:
    # Query lock tx
    api_response = api_instance.querylocked(account, time, sid, count, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpiryApi->querylocked: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Bech32 address | 
 **time** | **int**| Unix timestamp | 
 **sid** | **int**| Sequence id | 
 **count** | **int**| Querier count | 
 **token** | **str**| Symbol | [optional] 

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

