# dex_api_python.BancorApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_bancor_deal**](BancorApi.md#query_bancor_deal) | **GET** /bancorlite/deals | Query bancor market deal


# **query_bancor_deal**
> InlineResponse20057 query_bancor_deal(market, time, sid, count)

Query bancor market deal

Query bancor market deal until to given time

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.BancorApi()
market = 'market_example' # str | B:stock/money
time = 789 # int | Unix timestamp
sid = 789 # int | Sequence id
count = 56 # int | Querier deal count limited to 1024

try:
    # Query bancor market deal
    api_response = api_instance.query_bancor_deal(market, time, sid, count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BancorApi->query_bancor_deal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**| B:stock/money | 
 **time** | **int**| Unix timestamp | 
 **sid** | **int**| Sequence id | 
 **count** | **int**| Querier deal count limited to 1024 | 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

