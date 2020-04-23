# swagger_client.AliasApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address_from_alias**](AliasApi.md#get_address_from_alias) | **GET** /alias/address-of-alias/{alias} | Given an alias, query the corresponding address
[**get_alias_params**](AliasApi.md#get_alias_params) | **GET** /alias/parameters | Get the current alias parameters
[**get_aliases_from_address**](AliasApi.md#get_aliases_from_address) | **GET** /alias/aliases-of-address/{address} | Given an account&#39;s address, query all the corresponding aliases
[**update_alias**](AliasApi.md#update_alias) | **POST** /alias/update | Add or remove alias for an address


# **get_address_from_alias**
> InlineResponse20048 get_address_from_alias(alias)

Given an alias, query the corresponding address

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AliasApi()
alias = 'alias_example' # str | The alias to be queried

try:
    # Given an alias, query the corresponding address
    api_response = api_instance.get_address_from_alias(alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApi->get_address_from_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| The alias to be queried | 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alias_params**
> InlineResponse20050 get_alias_params()

Get the current alias parameters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AliasApi()

try:
    # Get the current alias parameters
    api_response = api_instance.get_alias_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApi->get_alias_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aliases_from_address**
> InlineResponse20049 get_aliases_from_address(address)

Given an account's address, query all the corresponding aliases

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AliasApi()
address = 'address_example' # str | The account's address to be queried

try:
    # Given an account's address, query all the corresponding aliases
    api_response = api_instance.get_aliases_from_address(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApi->get_aliases_from_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The account&#39;s address to be queried | 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alias**
> StdTx update_alias(alias_update_req)

Add or remove alias for an address

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AliasApi()
alias_update_req = swagger_client.AliasUpdateReq() # AliasUpdateReq | update an address's aliases

try:
    # Add or remove alias for an address
    api_response = api_instance.update_alias(alias_update_req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasApi->update_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias_update_req** | [**AliasUpdateReq**](AliasUpdateReq.md)| update an address&#39;s aliases | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

