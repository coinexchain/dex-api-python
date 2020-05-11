# dex_api_python.AuthApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account**](AuthApi.md#get_account) | **GET** /auth/accounts/{address} | Get the account information on blockchain
[**get_auth_params**](AuthApi.md#get_auth_params) | **GET** /auth/parameters | Get the current auth parameters
[**set_referee**](AuthApi.md#set_referee) | **POST** /auth/accounts/{address}/referee | Set referee for account


# **get_account**
> InlineResponse2004 get_account(address)

Get the account information on blockchain

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AuthApi()
address = 'coinex16gdxm24ht2mxtpz9cma6tr6a6d47x63hlq4pxt' # str | Account address

try:
    # Get the account information on blockchain
    api_response = api_instance.get_account(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_params**
> InlineResponse20034 get_auth_params()

Get the current auth parameters

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AuthApi()

try:
    # Get the current auth parameters
    api_response = api_instance.get_auth_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_referee**
> StdTx set_referee(address, referee)

Set referee for account

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AuthApi()
address = 'coinex16gdxm24ht2mxtpz9cma6tr6a6d47x63hlq4pxt' # str | Account address in bech32 format
referee = dex_api_python.Referee() # Referee | Referee

try:
    # Set referee for account
    api_response = api_instance.set_referee(address, referee)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->set_referee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address in bech32 format | 
 **referee** | [**Referee**](Referee.md)| Referee | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

