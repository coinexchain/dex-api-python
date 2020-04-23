# swagger_client.TendermintApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_block**](TendermintApi.md#get_block) | **GET** /blocks/{height} | Get a block at a certain height
[**get_latest_block**](TendermintApi.md#get_latest_block) | **GET** /blocks/latest | Get the latest block
[**get_latest_validator_set**](TendermintApi.md#get_latest_validator_set) | **GET** /validatorsets/latest | Get the latest validator set
[**get_node_info**](TendermintApi.md#get_node_info) | **GET** /node_info | The properties of the connected node
[**get_syncing**](TendermintApi.md#get_syncing) | **GET** /syncing | Syncing state of node
[**get_validator_set**](TendermintApi.md#get_validator_set) | **GET** /validatorsets/{height} | Get a validator set a certain height


# **get_block**
> BlockQuery get_block(height)

Get a block at a certain height

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TendermintApi()
height = 8.14 # float | Block height

try:
    # Get a block at a certain height
    api_response = api_instance.get_block(height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TendermintApi->get_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | **float**| Block height | 

### Return type

[**BlockQuery**](BlockQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_block**
> BlockQuery get_latest_block()

Get the latest block

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TendermintApi()

try:
    # Get the latest block
    api_response = api_instance.get_latest_block()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TendermintApi->get_latest_block: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BlockQuery**](BlockQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_validator_set**
> InlineResponse2001 get_latest_validator_set()

Get the latest validator set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TendermintApi()

try:
    # Get the latest validator set
    api_response = api_instance.get_latest_validator_set()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TendermintApi->get_latest_validator_set: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_info**
> InlineResponse200 get_node_info()

The properties of the connected node

Information about the connected node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TendermintApi()

try:
    # The properties of the connected node
    api_response = api_instance.get_node_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TendermintApi->get_node_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_syncing**
> get_syncing()

Syncing state of node

Get if the node is currently syning with other nodes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TendermintApi()

try:
    # Syncing state of node
    api_instance.get_syncing()
except ApiException as e:
    print("Exception when calling TendermintApi->get_syncing: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validator_set**
> InlineResponse2002 get_validator_set(height)

Get a validator set a certain height

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TendermintApi()
height = 8.14 # float | Block height

try:
    # Get a validator set a certain height
    api_response = api_instance.get_validator_set(height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TendermintApi->get_validator_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | **float**| Block height | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

