# dex_api_python.SlashApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_slash**](SlashApi.md#query_slash) | **GET** /slash/slashings | Query validator slash info


# **query_slash**
> InlineResponse20064 query_slash(time, sid, count)

Query validator slash info

Query validator slash power, reason, and jailed status etc

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.SlashApi()
time = 789 # int | Unix timestamp
sid = 789 # int | Sequence id
count = 56 # int | Querier count limited to 1024

try:
    # Query validator slash info
    api_response = api_instance.query_slash(time, sid, count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlashApi->query_slash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time** | **int**| Unix timestamp | 
 **sid** | **int**| Sequence id | 
 **count** | **int**| Querier count limited to 1024 | 

### Return type

[**InlineResponse20064**](InlineResponse20064.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

