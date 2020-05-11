# dex_api_python.DistributionApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**donate_to_community_pool**](DistributionApi.md#donate_to_community_pool) | **POST** /distribution/{accAddress}/donates | Donate to the community pool
[**get_all_rewards**](DistributionApi.md#get_all_rewards) | **GET** /distribution/delegators/{delegatorAddr}/rewards | Get the total rewards balance from all delegations
[**get_community_pool**](DistributionApi.md#get_community_pool) | **GET** /distribution/community_pool | Community pool parameters
[**get_distribution_info**](DistributionApi.md#get_distribution_info) | **GET** /distribution/validators/{validatorAddr} | Validator distribution information
[**get_distribution_params**](DistributionApi.md#get_distribution_params) | **GET** /distribution/parameters | Fee distribution parameters
[**get_outstanding_rewards**](DistributionApi.md#get_outstanding_rewards) | **GET** /distribution/validators/{validatorAddr}/outstanding_rewards | Fee distribution outstanding rewards of a single validator
[**get_reward_by_validator**](DistributionApi.md#get_reward_by_validator) | **GET** /distribution/delegators/{delegatorAddr}/rewards/{validatorAddr} | Query a delegation reward
[**get_validator_rewards**](DistributionApi.md#get_validator_rewards) | **GET** /distribution/validators/{validatorAddr}/rewards | Commission and self-delegation rewards of a single validator
[**get_withdraw_address**](DistributionApi.md#get_withdraw_address) | **GET** /distribution/delegators/{delegatorAddr}/withdraw_address | Get the rewards withdrawal address
[**set_withdraw_address**](DistributionApi.md#set_withdraw_address) | **POST** /distribution/delegators/{delegatorAddr}/withdraw_address | Replace the rewards withdrawal address
[**withdraw_all_rewards**](DistributionApi.md#withdraw_all_rewards) | **POST** /distribution/delegators/{delegatorAddr}/rewards | Withdraw all the delegator&#39;s delegation rewards
[**withdraw_all_validator_rewards**](DistributionApi.md#withdraw_all_validator_rewards) | **POST** /distribution/validators/{validatorAddr}/rewards | Withdraw the validator&#39;s rewards
[**withdraw_rewards_by_validator**](DistributionApi.md#withdraw_rewards_by_validator) | **POST** /distribution/delegators/{delegatorAddr}/rewards/{validatorAddr} | Withdraw a delegation reward


# **donate_to_community_pool**
> StdTx donate_to_community_pool(acc_address, amount)

Donate to the community pool

Donate some amount of cet to the community pool

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.DistributionApi()
acc_address = 'coinex1628t2zxa9antj3qtkg7xj2m4t68uljqvyjqrup' # str | Account address of the user
amount = dex_api_python.Amount() # Amount | Amount of cet to donate

try:
    # Donate to the community pool
    api_response = api_instance.donate_to_community_pool(acc_address, amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->donate_to_community_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acc_address** | **str**| Account address of the user | 
 **amount** | [**Amount**](Amount.md)| Amount of cet to donate | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_rewards**
> InlineResponse20029 get_all_rewards(delegator_addr)

Get the total rewards balance from all delegations

Get the sum of all the rewards earned by delegations by a single delegator

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.DistributionApi()
delegator_addr = 'coinex167w96tdvmazakdwkw2u57227eduula2cy572lf' # str | Bech32 AccAddress of Delegator

try:
    # Get the total rewards balance from all delegations
    api_response = api_instance.get_all_rewards(delegator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->get_all_rewards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_community_pool**
> object get_community_pool()

Community pool parameters

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.DistributionApi()

try:
    # Community pool parameters
    api_response = api_instance.get_community_pool()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->get_community_pool: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_distribution_info**
> InlineResponse20032 get_distribution_info(validator_addr)

Validator distribution information

Query the distribution information of a single validator

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.DistributionApi()
validator_addr = 'coinexvaloper1qwl879nx9t6kef4supyazayf7vjhennyh568ys' # str | Bech32 OperatorAddress of validator

try:
    # Validator distribution information
    api_response = api_instance.get_distribution_info(validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->get_distribution_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_distribution_params**
> InlineResponse20033 get_distribution_params()

Fee distribution parameters

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.DistributionApi()

try:
    # Fee distribution parameters
    api_response = api_instance.get_distribution_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->get_distribution_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outstanding_rewards**
> object get_outstanding_rewards(validator_addr)

Fee distribution outstanding rewards of a single validator

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.DistributionApi()
validator_addr = 'coinexvaloper1qwl879nx9t6kef4supyazayf7vjhennyh568ys' # str | Bech32 OperatorAddress of validator

try:
    # Fee distribution outstanding rewards of a single validator
    api_response = api_instance.get_outstanding_rewards(validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->get_outstanding_rewards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reward_by_validator**
> InlineResponse20030 get_reward_by_validator(delegator_addr, validator_addr)

Query a delegation reward

Query a single delegation reward by a delegator

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.DistributionApi()
delegator_addr = 'coinex167w96tdvmazakdwkw2u57227eduula2cy572lf' # str | Bech32 AccAddress of Delegator
validator_addr = 'coinexvaloper1qwl879nx9t6kef4supyazayf7vjhennyh568ys' # str | Bech32 OperatorAddress of validator

try:
    # Query a delegation reward
    api_response = api_instance.get_reward_by_validator(delegator_addr, validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->get_reward_by_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validator_rewards**
> InlineResponse20030 get_validator_rewards(validator_addr)

Commission and self-delegation rewards of a single validator

Query the commission and self-delegation rewards of validator.

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.DistributionApi()
validator_addr = 'coinexvaloper1qwl879nx9t6kef4supyazayf7vjhennyh568ys' # str | Bech32 OperatorAddress of validator

try:
    # Commission and self-delegation rewards of a single validator
    api_response = api_instance.get_validator_rewards(validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->get_validator_rewards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_withdraw_address**
> InlineResponse20031 get_withdraw_address(delegator_addr)

Get the rewards withdrawal address

Get the delegations' rewards withdrawal address. This is the address in which the user will receive the reward funds

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.DistributionApi()
delegator_addr = 'coinex167w96tdvmazakdwkw2u57227eduula2cy572lf' # str | Bech32 AccAddress of Delegator

try:
    # Get the rewards withdrawal address
    api_response = api_instance.get_withdraw_address(delegator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->get_withdraw_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_withdraw_address**
> BroadcastTxCommitResult set_withdraw_address(delegator_addr, withdraw_request_body=withdraw_request_body)

Replace the rewards withdrawal address

Replace the delegations' rewards withdrawal address for a new one.

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.DistributionApi()
delegator_addr = 'coinex167w96tdvmazakdwkw2u57227eduula2cy572lf' # str | Bech32 AccAddress of Delegator
withdraw_request_body = dex_api_python.WithdrawRequestBody2() # WithdrawRequestBody2 |  (optional)

try:
    # Replace the rewards withdrawal address
    api_response = api_instance.set_withdraw_address(delegator_addr, withdraw_request_body=withdraw_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->set_withdraw_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **withdraw_request_body** | [**WithdrawRequestBody2**](WithdrawRequestBody2.md)|  | [optional] 

### Return type

[**BroadcastTxCommitResult**](BroadcastTxCommitResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_all_rewards**
> BroadcastTxCommitResult withdraw_all_rewards(delegator_addr, withdraw_request_body=withdraw_request_body)

Withdraw all the delegator's delegation rewards

Withdraw all the delegator's delegation rewards

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.DistributionApi()
delegator_addr = 'coinex167w96tdvmazakdwkw2u57227eduula2cy572lf' # str | Bech32 AccAddress of Delegator
withdraw_request_body = dex_api_python.WithdrawRequestBody() # WithdrawRequestBody |  (optional)

try:
    # Withdraw all the delegator's delegation rewards
    api_response = api_instance.withdraw_all_rewards(delegator_addr, withdraw_request_body=withdraw_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->withdraw_all_rewards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **withdraw_request_body** | [**WithdrawRequestBody**](WithdrawRequestBody.md)|  | [optional] 

### Return type

[**BroadcastTxCommitResult**](BroadcastTxCommitResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_all_validator_rewards**
> BroadcastTxCommitResult withdraw_all_validator_rewards(validator_addr, withdraw_request_body=withdraw_request_body)

Withdraw the validator's rewards

Withdraw the validator's self-delegation and commissions rewards

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.DistributionApi()
validator_addr = 'coinexvaloper1qwl879nx9t6kef4supyazayf7vjhennyh568ys' # str | Bech32 OperatorAddress of validator
withdraw_request_body = dex_api_python.WithdrawRequestBody3() # WithdrawRequestBody3 |  (optional)

try:
    # Withdraw the validator's rewards
    api_response = api_instance.withdraw_all_validator_rewards(validator_addr, withdraw_request_body=withdraw_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->withdraw_all_validator_rewards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 
 **withdraw_request_body** | [**WithdrawRequestBody3**](WithdrawRequestBody3.md)|  | [optional] 

### Return type

[**BroadcastTxCommitResult**](BroadcastTxCommitResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_rewards_by_validator**
> BroadcastTxCommitResult withdraw_rewards_by_validator(delegator_addr, validator_addr, withdraw_request_body=withdraw_request_body)

Withdraw a delegation reward

Withdraw a delegator's delegation reward from a single validator

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.DistributionApi()
delegator_addr = 'coinex167w96tdvmazakdwkw2u57227eduula2cy572lf' # str | Bech32 AccAddress of Delegator
validator_addr = 'coinexvaloper1qwl879nx9t6kef4supyazayf7vjhennyh568ys' # str | Bech32 OperatorAddress of validator
withdraw_request_body = dex_api_python.WithdrawRequestBody1() # WithdrawRequestBody1 |  (optional)

try:
    # Withdraw a delegation reward
    api_response = api_instance.withdraw_rewards_by_validator(delegator_addr, validator_addr, withdraw_request_body=withdraw_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->withdraw_rewards_by_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 
 **withdraw_request_body** | [**WithdrawRequestBody1**](WithdrawRequestBody1.md)|  | [optional] 

### Return type

[**BroadcastTxCommitResult**](BroadcastTxCommitResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

