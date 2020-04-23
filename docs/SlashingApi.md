# swagger_client.SlashingApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_signing_info**](SlashingApi.md#get_signing_info) | **GET** /slashing/validators/{validatorPubKey}/signing_info | Get sign info of given validator
[**get_signing_infos**](SlashingApi.md#get_signing_infos) | **GET** /slashing/signing_infos | Get sign info of given all validators
[**get_slashing_params**](SlashingApi.md#get_slashing_params) | **GET** /slashing/parameters | Get the current slashing parameters
[**unjail_validator**](SlashingApi.md#unjail_validator) | **POST** /slashing/validators/{validatorAddr}/unjail | Unjail a jailed validator


# **get_signing_info**
> InlineResponse20015 get_signing_info(validator_pub_key)

Get sign info of given validator

Get sign info of given validator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SlashingApi()
validator_pub_key = 'validator_pub_key_example' # str | Bech32 validator public key

try:
    # Get sign info of given validator
    api_response = api_instance.get_signing_info(validator_pub_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlashingApi->get_signing_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_pub_key** | **str**| Bech32 validator public key | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signing_infos**
> InlineResponse20016 get_signing_infos(page, limit)

Get sign info of given all validators

Get sign info of all validators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SlashingApi()
page = 56 # int | Page number
limit = 56 # int | Maximum number of items per page

try:
    # Get sign info of given all validators
    api_response = api_instance.get_signing_infos(page, limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlashingApi->get_signing_infos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | 
 **limit** | **int**| Maximum number of items per page | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slashing_params**
> InlineResponse20017 get_slashing_params()

Get the current slashing parameters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SlashingApi()

try:
    # Get the current slashing parameters
    api_response = api_instance.get_slashing_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlashingApi->get_slashing_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unjail_validator**
> BroadcastTxCommitResult unjail_validator(validator_addr, unjail_body)

Unjail a jailed validator

Send transaction to unjail a jailed validator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SlashingApi()
validator_addr = 'validator_addr_example' # str | Bech32 validator address
unjail_body = swagger_client.UnjailBody() # UnjailBody | 

try:
    # Unjail a jailed validator
    api_response = api_instance.unjail_validator(validator_addr, unjail_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlashingApi->unjail_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| Bech32 validator address | 
 **unjail_body** | [**UnjailBody**](UnjailBody.md)|  | 

### Return type

[**BroadcastTxCommitResult**](BroadcastTxCommitResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

