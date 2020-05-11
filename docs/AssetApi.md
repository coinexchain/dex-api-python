# dex_api_python.AssetApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_whitelist**](AssetApi.md#add_whitelist) | **POST** /asset/tokens/{symbol}/forbidden/whitelist | Add forbid whitelist
[**burn_token**](AssetApi.md#burn_token) | **POST** /asset/tokens/{symbol}/burns | Burn token
[**forbid_addr**](AssetApi.md#forbid_addr) | **POST** /asset/tokens/{symbol}/forbidden/addresses | Forbid address
[**forbid_token**](AssetApi.md#forbid_token) | **POST** /asset/tokens/{symbol}/forbids | Forbid token
[**get_asset_params**](AssetApi.md#get_asset_params) | **GET** /asset/parameters | Get the current asset parameters
[**get_forbidden_addresses**](AssetApi.md#get_forbidden_addresses) | **GET** /asset/tokens/{symbol}/forbidden/addresses | query forbidden addresses
[**get_reserved_symbols**](AssetApi.md#get_reserved_symbols) | **GET** /asset/tokens/reserved/symbols | List reserved symbols
[**get_token**](AssetApi.md#get_token) | **GET** /asset/tokens/{symbol} | queryToken
[**get_token_list**](AssetApi.md#get_token_list) | **GET** /asset/tokens | List tokens
[**get_whitelist**](AssetApi.md#get_whitelist) | **GET** /asset/tokens/{symbol}/forbidden/whitelist | queryWhitelist
[**issue_token**](AssetApi.md#issue_token) | **POST** /asset/tokens | Issue token
[**mint_token**](AssetApi.md#mint_token) | **POST** /asset/tokens/{symbol}/mints | Mint token
[**modify_token_info**](AssetApi.md#modify_token_info) | **POST** /asset/tokens/{symbol}/infos | Modify token info
[**remove_whitelist**](AssetApi.md#remove_whitelist) | **POST** /asset/tokens/{symbol}/unforbidden/whitelist | Remove forbid whitelist
[**transfer_ownership**](AssetApi.md#transfer_ownership) | **POST** /asset/tokens/{symbol}/ownerships | Transfer ownership
[**un_forbid_addr**](AssetApi.md#un_forbid_addr) | **POST** /asset/tokens/{symbol}/unforbidden/addresses | UnForbid address
[**un_frobid_token**](AssetApi.md#un_frobid_token) | **POST** /asset/tokens/{symbol}/unforbids | UnForbid token


# **add_whitelist**
> StdTx add_whitelist(symbol, whitelist)

Add forbid whitelist

Add forbiddable token whitelist addr

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AssetApi()
symbol = 'abc' # str | token symbol
whitelist = dex_api_python.Whitelist() # Whitelist | token whitelist addr

try:
    # Add forbid whitelist
    api_response = api_instance.add_whitelist(symbol, whitelist)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->add_whitelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| token symbol | 
 **whitelist** | [**Whitelist**](Whitelist.md)| token whitelist addr | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **burn_token**
> StdTx burn_token(symbol, amount)

Burn token

Burn burnable token

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AssetApi()
symbol = 'abc' # str | token symbol
amount = dex_api_python.Amount2() # Amount2 | burn token amount

try:
    # Burn token
    api_response = api_instance.burn_token(symbol, amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->burn_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| token symbol | 
 **amount** | [**Amount2**](Amount2.md)| burn token amount | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forbid_addr**
> StdTx forbid_addr(symbol, addresses)

Forbid address

Add forbidden addresses

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AssetApi()
symbol = 'abc' # str | token symbol
addresses = dex_api_python.Addresses() # Addresses | forbidden addresses

try:
    # Forbid address
    api_response = api_instance.forbid_addr(symbol, addresses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->forbid_addr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| token symbol | 
 **addresses** | [**Addresses**](Addresses.md)| forbidden addresses | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forbid_token**
> StdTx forbid_token(symbol, base_req)

Forbid token

Forbid forbiddable token

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AssetApi()
symbol = 'abc' # str | token symbol
base_req = dex_api_python.BaseReq() # BaseReq | base req

try:
    # Forbid token
    api_response = api_instance.forbid_token(symbol, base_req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->forbid_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| token symbol | 
 **base_req** | [**BaseReq**](BaseReq.md)| base req | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_params**
> InlineResponse20037 get_asset_params()

Get the current asset parameters

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AssetApi()

try:
    # Get the current asset parameters
    api_response = api_instance.get_asset_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forbidden_addresses**
> InlineResponse20040 get_forbidden_addresses(symbol)

query forbidden addresses

Get forbidden addresses with provided `symbol`

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AssetApi()
symbol = 'abc' # str | token symbol

try:
    # query forbidden addresses
    api_response = api_instance.get_forbidden_addresses(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_forbidden_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| token symbol | 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reserved_symbols**
> InlineResponse20041 get_reserved_symbols()

List reserved symbols

List all reserved symbols

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AssetApi()

try:
    # List reserved symbols
    api_response = api_instance.get_reserved_symbols()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_reserved_symbols: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token**
> InlineResponse20039 get_token(symbol)

queryToken

Get token with provided `symbol`

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AssetApi()
symbol = 'abc' # str | token symbol

try:
    # queryToken
    api_response = api_instance.get_token(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| token symbol | 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_list**
> InlineResponse20038 get_token_list()

List tokens

List all existing tokens

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AssetApi()

try:
    # List tokens
    api_response = api_instance.get_token_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_token_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_whitelist**
> InlineResponse20040 get_whitelist(symbol)

queryWhitelist

Get token whitelist with provided `symbol`

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AssetApi()
symbol = 'abc' # str | token symbol

try:
    # queryWhitelist
    api_response = api_instance.get_whitelist(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_whitelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| token symbol | 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_token**
> StdTx issue_token(token_info)

Issue token

Issue a new Token

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AssetApi()
token_info = dex_api_python.IssueToken() # IssueToken | the detail info about the Token to issue

try:
    # Issue token
    api_response = api_instance.issue_token(token_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->issue_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_info** | [**IssueToken**](IssueToken.md)| the detail info about the Token to issue | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mint_token**
> StdTx mint_token(symbol, amount)

Mint token

Mint mintable token

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AssetApi()
symbol = 'abc' # str | token symbol
amount = dex_api_python.Amount1() # Amount1 | mint token amount

try:
    # Mint token
    api_response = api_instance.mint_token(symbol, amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->mint_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| token symbol | 
 **amount** | [**Amount1**](Amount1.md)| mint token amount | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_token_info**
> StdTx modify_token_info(symbol, info)

Modify token info

Modify token info

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AssetApi()
symbol = 'abc' # str | token symbol
info = dex_api_python.Info() # Info | new token info

try:
    # Modify token info
    api_response = api_instance.modify_token_info(symbol, info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->modify_token_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| token symbol | 
 **info** | [**Info**](Info.md)| new token info | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_whitelist**
> StdTx remove_whitelist(symbol, whitelist)

Remove forbid whitelist

Remove forbiddable token whitelist addr

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AssetApi()
symbol = 'abc' # str | token symbol
whitelist = dex_api_python.Whitelist() # Whitelist | token whitelist addr

try:
    # Remove forbid whitelist
    api_response = api_instance.remove_whitelist(symbol, whitelist)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->remove_whitelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| token symbol | 
 **whitelist** | [**Whitelist**](Whitelist.md)| token whitelist addr | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_ownership**
> StdTx transfer_ownership(symbol, new_owner)

Transfer ownership

Transfer token owner ship

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AssetApi()
symbol = 'abc' # str | token symbol
new_owner = dex_api_python.NewOwner() # NewOwner | transfer ownership to new owner

try:
    # Transfer ownership
    api_response = api_instance.transfer_ownership(symbol, new_owner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->transfer_ownership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| token symbol | 
 **new_owner** | [**NewOwner**](NewOwner.md)| transfer ownership to new owner | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **un_forbid_addr**
> StdTx un_forbid_addr(symbol, addresses)

UnForbid address

Remove forbidden addresses

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AssetApi()
symbol = 'abc' # str | token symbol
addresses = dex_api_python.Addresses() # Addresses | un forbidden addresses

try:
    # UnForbid address
    api_response = api_instance.un_forbid_addr(symbol, addresses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->un_forbid_addr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| token symbol | 
 **addresses** | [**Addresses**](Addresses.md)| un forbidden addresses | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **un_frobid_token**
> StdTx un_frobid_token(symbol, base_req)

UnForbid token

UnForbid forbiddable token

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.AssetApi()
symbol = 'abc' # str | token symbol
base_req = dex_api_python.BaseReq1() # BaseReq1 | base req

try:
    # UnForbid token
    api_response = api_instance.un_frobid_token(symbol, base_req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->un_frobid_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| token symbol | 
 **base_req** | [**BaseReq1**](BaseReq1.md)| base req | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

