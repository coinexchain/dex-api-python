# dex_api_python.BancorliteApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bancor_cancel**](BancorliteApi.md#bancor_cancel) | **POST** /bancorlite/bancor-cancel | cancel bancor
[**bancor_init**](BancorliteApi.md#bancor_init) | **POST** /bancorlite/bancor-init | create bancor
[**bancor_trade**](BancorliteApi.md#bancor_trade) | **POST** /bancorlite/bancor-trade | trade with bancor
[**get_bancor_info**](BancorliteApi.md#get_bancor_info) | **GET** /bancorlite/pools/{symbol} | get the bancor pool info
[**get_bancor_infos**](BancorliteApi.md#get_bancor_infos) | **GET** /bancorlite/infos | get all bancor infos
[**get_bancorlite_params**](BancorliteApi.md#get_bancorlite_params) | **GET** /bancorlite/parameters | Get the current bancorlite parameters


# **bancor_cancel**
> StdTx bancor_cancel(bancor_cancel)

cancel bancor

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.BancorliteApi()
bancor_cancel = dex_api_python.BancorCancel() # BancorCancel | cancel bancor

try:
    # cancel bancor
    api_response = api_instance.bancor_cancel(bancor_cancel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BancorliteApi->bancor_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bancor_cancel** | [**BancorCancel**](BancorCancel.md)| cancel bancor | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bancor_init**
> StdTx bancor_init(bancor_init)

create bancor

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.BancorliteApi()
bancor_init = dex_api_python.BancorInit() # BancorInit | create bancor

try:
    # create bancor
    api_response = api_instance.bancor_init(bancor_init)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BancorliteApi->bancor_init: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bancor_init** | [**BancorInit**](BancorInit.md)| create bancor | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bancor_trade**
> StdTx bancor_trade(bancor_trade)

trade with bancor

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.BancorliteApi()
bancor_trade = dex_api_python.BancorTrade() # BancorTrade | trade with bancor

try:
    # trade with bancor
    api_response = api_instance.bancor_trade(bancor_trade)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BancorliteApi->bancor_trade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bancor_trade** | [**BancorTrade**](BancorTrade.md)| trade with bancor | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bancor_info**
> dict(str, object) get_bancor_info(symbol)

get the bancor pool info

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.BancorliteApi()
symbol = 'btc-cet' # str | stock and money pair

try:
    # get the bancor pool info
    api_response = api_instance.get_bancor_info(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BancorliteApi->get_bancor_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| stock and money pair | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bancor_infos**
> InlineResponse20052 get_bancor_infos()

get all bancor infos

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.BancorliteApi()

try:
    # get all bancor infos
    api_response = api_instance.get_bancor_infos()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BancorliteApi->get_bancor_infos: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bancorlite_params**
> InlineResponse20051 get_bancorlite_params()

Get the current bancorlite parameters

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.BancorliteApi()

try:
    # Get the current bancorlite parameters
    api_response = api_instance.get_bancorlite_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BancorliteApi->get_bancorlite_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

