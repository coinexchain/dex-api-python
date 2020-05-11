# dex_api_python.MiscApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_block_times**](MiscApi.md#query_block_times) | **GET** /misc/block-times | Query block time
[**query_donation**](MiscApi.md#query_donation) | **GET** /misc/donations | Query donations info
[**query_last_block**](MiscApi.md#query_last_block) | **GET** /misc/height | Query least block info


# **query_block_times**
> list[int] query_block_times(height, count)

Query block time

Query the block time up to given height

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MiscApi()
height = 789 # int | Block height
count = 56 # int | Querier count limited to 1024

try:
    # Query block time
    api_response = api_instance.query_block_times(height, count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscApi->query_block_times: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | **int**| Block height | 
 **count** | **int**| Querier count limited to 1024 | 

### Return type

**list[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_donation**
> InlineResponse20054 query_donation(time, sid, count)

Query donations info

Query donations by DonateToCommunityPool or CommentToken

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MiscApi()
time = 789 # int | Unix timestamp
sid = 789 # int | Sequence id
count = 56 # int | Querier count limited to 1024

try:
    # Query donations info
    api_response = api_instance.query_donation(time, sid, count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscApi->query_donation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time** | **int**| Unix timestamp | 
 **sid** | **int**| Sequence id | 
 **count** | **int**| Querier count limited to 1024 | 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_last_block**
> InlineResponse20053 query_last_block()

Query least block info

Query least block info

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MiscApi()

try:
    # Query least block info
    api_response = api_instance.query_last_block()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscApi->query_last_block: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

