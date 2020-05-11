# dex_api_python.IncentiveApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_incentive_params**](IncentiveApi.md#get_incentive_params) | **GET** /incentive/parameters | Get the current incentive parameters


# **get_incentive_params**
> InlineResponse20036 get_incentive_params()

Get the current incentive parameters

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.IncentiveApi()

try:
    # Get the current incentive parameters
    api_response = api_instance.get_incentive_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncentiveApi->get_incentive_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

