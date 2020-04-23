# swagger_client.BankApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address_balances**](BankApi.md#get_address_balances) | **GET** /bank/balances/{address} | Get the account balances
[**get_bank_params**](BankApi.md#get_bank_params) | **GET** /bank/parameters | Get the current bankx parameters
[**send_coins**](BankApi.md#send_coins) | **POST** /bank/accounts/{address}/transfers | Send coins from one account to another
[**set_memo_required**](BankApi.md#set_memo_required) | **POST** /bank/accounts/memo | Mark if memo is required to receive coins
[**transfer_supervised_coins**](BankApi.md#transfer_supervised_coins) | **POST** /bank/accounts/{address}/supervised_transfers | Operate a supervised transfer


# **get_address_balances**
> dict(str, object) get_address_balances(address)

Get the account balances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BankApi()
address = 'address_example' # str | Account address in bech32 format

try:
    # Get the account balances
    api_response = api_instance.get_address_balances(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankApi->get_address_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address in bech32 format | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_params**
> InlineResponse20035 get_bank_params()

Get the current bankx parameters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BankApi()

try:
    # Get the current bankx parameters
    api_response = api_instance.get_bank_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankApi->get_bank_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_coins**
> StdTx send_coins(address, account)

Send coins from one account to another

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BankApi()
address = 'address_example' # str | Account address in bech32 format
account = swagger_client.Account() # Account | The sender and tx information

try:
    # Send coins from one account to another
    api_response = api_instance.send_coins(address, account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankApi->send_coins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address in bech32 format | 
 **account** | [**Account**](Account.md)| The sender and tx information | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_memo_required**
> StdTx set_memo_required(account)

Mark if memo is required to receive coins

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BankApi()
account = swagger_client.Account1() # Account1 | The mark

try:
    # Mark if memo is required to receive coins
    api_response = api_instance.set_memo_required(account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankApi->set_memo_required: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**Account1**](Account1.md)| The mark | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_supervised_coins**
> StdTx transfer_supervised_coins(address, post_tx_body)

Operate a supervised transfer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BankApi()
address = 'address_example' # str | Account address in bech32 format
post_tx_body = swagger_client.PostTxBody() # PostTxBody | The sender and tx information

try:
    # Operate a supervised transfer
    api_response = api_instance.transfer_supervised_coins(address, post_tx_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankApi->transfer_supervised_coins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address in bech32 format | 
 **post_tx_body** | [**PostTxBody**](PostTxBody.md)| The sender and tx information | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

