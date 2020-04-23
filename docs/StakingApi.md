# swagger_client.StakingApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_delegations**](StakingApi.md#get_delegations) | **GET** /staking/delegators/{delegatorAddr}/delegations | Get all delegations from a delegator
[**get_delegations_of_validator**](StakingApi.md#get_delegations_of_validator) | **GET** /staking/validators/{validatorAddr}/delegations | Get all delegations from a validator
[**get_delegations_to_validator**](StakingApi.md#get_delegations_to_validator) | **GET** /staking/delegators/{delegatorAddr}/delegations/{validatorAddr} | Query the current delegation between a delegator and a validator
[**get_delegator_txs**](StakingApi.md#get_delegator_txs) | **GET** /staking/delegators/{delegatorAddr}/txs | Get all staking txs (i.e msgs) from a delegator
[**get_redelegations**](StakingApi.md#get_redelegations) | **GET** /staking/redelegations | Get all redelegations (filter by query params)
[**get_staking_parameters**](StakingApi.md#get_staking_parameters) | **GET** /staking/parameters | Get the current staking parameter values
[**get_staking_pool**](StakingApi.md#get_staking_pool) | **GET** /staking/pool | Get the current state of the staking pool
[**get_undelegations_between**](StakingApi.md#get_undelegations_between) | **GET** /staking/delegators/{delegatorAddr}/unbonding_delegations/{validatorAddr} | Query all unbonding delegations between a delegator and a validator
[**get_undelegations_of_delegator**](StakingApi.md#get_undelegations_of_delegator) | **GET** /staking/delegators/{delegatorAddr}/unbonding_delegations | Get all unbonding delegations from a delegator
[**get_undelegations_of_validator**](StakingApi.md#get_undelegations_of_validator) | **GET** /staking/validators/{validatorAddr}/unbonding_delegations | Get all unbonding delegations from a validator
[**get_validator**](StakingApi.md#get_validator) | **GET** /staking/validators/{validatorAddr} | Query the information from a single validator
[**get_validator_of_delegator**](StakingApi.md#get_validator_of_delegator) | **GET** /staking/delegators/{delegatorAddr}/validators/{validatorAddr} | Query a validator that a delegator is bonded to
[**get_validators**](StakingApi.md#get_validators) | **GET** /staking/validators | Get all validator candidates. By default it returns only the bonded validators.
[**get_validators_of_delegator**](StakingApi.md#get_validators_of_delegator) | **GET** /staking/delegators/{delegatorAddr}/validators | Query all validators that a delegator is bonded to
[**submit_delegation**](StakingApi.md#submit_delegation) | **POST** /staking/delegators/{delegatorAddr}/delegations | Submit delegation
[**submit_redelegation**](StakingApi.md#submit_redelegation) | **POST** /staking/delegators/{delegatorAddr}/redelegations | Submit a redelegation
[**undelegate**](StakingApi.md#undelegate) | **POST** /staking/delegators/{delegatorAddr}/unbonding_delegations | Submit an unbonding delegation


# **get_delegations**
> InlineResponse2005 get_delegations(delegator_addr)

Get all delegations from a delegator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator

try:
    # Get all delegations from a delegator
    api_response = api_instance.get_delegations(delegator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->get_delegations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delegations_of_validator**
> InlineResponse2005 get_delegations_of_validator(validator_addr)

Get all delegations from a validator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
validator_addr = 'validator_addr_example' # str | Bech32 OperatorAddress of validator

try:
    # Get all delegations from a validator
    api_response = api_instance.get_delegations_of_validator(validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->get_delegations_of_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delegations_to_validator**
> InlineResponse2006 get_delegations_to_validator(delegator_addr, validator_addr)

Query the current delegation between a delegator and a validator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator
validator_addr = 'validator_addr_example' # str | Bech32 OperatorAddress of validator

try:
    # Query the current delegation between a delegator and a validator
    api_response = api_instance.get_delegations_to_validator(delegator_addr, validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->get_delegations_to_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delegator_txs**
> list[PaginatedQueryTxs] get_delegator_txs(delegator_addr)

Get all staking txs (i.e msgs) from a delegator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator

try:
    # Get all staking txs (i.e msgs) from a delegator
    api_response = api_instance.get_delegator_txs(delegator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->get_delegator_txs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 

### Return type

[**list[PaginatedQueryTxs]**](PaginatedQueryTxs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_redelegations**
> InlineResponse2009 get_redelegations(delegator=delegator, validator_from=validator_from, validator_to=validator_to)

Get all redelegations (filter by query params)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator = 'delegator_example' # str | Bech32 AccAddress of Delegator (optional)
validator_from = 'validator_from_example' # str | Bech32 ValAddress of SrcValidator (optional)
validator_to = 'validator_to_example' # str | Bech32 ValAddress of DstValidator (optional)

try:
    # Get all redelegations (filter by query params)
    api_response = api_instance.get_redelegations(delegator=delegator, validator_from=validator_from, validator_to=validator_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->get_redelegations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator** | **str**| Bech32 AccAddress of Delegator | [optional] 
 **validator_from** | **str**| Bech32 ValAddress of SrcValidator | [optional] 
 **validator_to** | **str**| Bech32 ValAddress of DstValidator | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_staking_parameters**
> InlineResponse20014 get_staking_parameters()

Get the current staking parameter values

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()

try:
    # Get the current staking parameter values
    api_response = api_instance.get_staking_parameters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->get_staking_parameters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_staking_pool**
> InlineResponse20013 get_staking_pool()

Get the current state of the staking pool

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()

try:
    # Get the current state of the staking pool
    api_response = api_instance.get_staking_pool()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->get_staking_pool: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_undelegations_between**
> InlineResponse2008 get_undelegations_between(delegator_addr, validator_addr)

Query all unbonding delegations between a delegator and a validator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator
validator_addr = 'validator_addr_example' # str | Bech32 OperatorAddress of validator

try:
    # Query all unbonding delegations between a delegator and a validator
    api_response = api_instance.get_undelegations_between(delegator_addr, validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->get_undelegations_between: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_undelegations_of_delegator**
> InlineResponse2007 get_undelegations_of_delegator(delegator_addr)

Get all unbonding delegations from a delegator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator

try:
    # Get all unbonding delegations from a delegator
    api_response = api_instance.get_undelegations_of_delegator(delegator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->get_undelegations_of_delegator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_undelegations_of_validator**
> InlineResponse20012 get_undelegations_of_validator(validator_addr)

Get all unbonding delegations from a validator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
validator_addr = 'validator_addr_example' # str | Bech32 OperatorAddress of validator

try:
    # Get all unbonding delegations from a validator
    api_response = api_instance.get_undelegations_of_validator(validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->get_undelegations_of_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validator**
> InlineResponse20011 get_validator(validator_addr)

Query the information from a single validator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
validator_addr = 'validator_addr_example' # str | Bech32 OperatorAddress of validator

try:
    # Query the information from a single validator
    api_response = api_instance.get_validator(validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->get_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validator_of_delegator**
> InlineResponse20011 get_validator_of_delegator(delegator_addr, validator_addr)

Query a validator that a delegator is bonded to

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator
validator_addr = 'validator_addr_example' # str | Bech32 ValAddress of Delegator

try:
    # Query a validator that a delegator is bonded to
    api_response = api_instance.get_validator_of_delegator(delegator_addr, validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->get_validator_of_delegator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **validator_addr** | **str**| Bech32 ValAddress of Delegator | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validators**
> InlineResponse20010 get_validators(status=status, page=page, limit=limit)

Get all validator candidates. By default it returns only the bonded validators.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
status = 'status_example' # str | The validator bond status. Must be either 'bonded', 'unbonded', or 'unbonding'. (optional)
page = 56 # int | The page number. (optional)
limit = 56 # int | The maximum number of items per page. (optional)

try:
    # Get all validator candidates. By default it returns only the bonded validators.
    api_response = api_instance.get_validators(status=status, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->get_validators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| The validator bond status. Must be either &#39;bonded&#39;, &#39;unbonded&#39;, or &#39;unbonding&#39;. | [optional] 
 **page** | **int**| The page number. | [optional] 
 **limit** | **int**| The maximum number of items per page. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validators_of_delegator**
> InlineResponse20010 get_validators_of_delegator(delegator_addr)

Query all validators that a delegator is bonded to

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator

try:
    # Query all validators that a delegator is bonded to
    api_response = api_instance.get_validators_of_delegator(delegator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->get_validators_of_delegator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_delegation**
> BroadcastTxCommitResult submit_delegation(delegator_addr, delegation=delegation)

Submit delegation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator
delegation = swagger_client.Delegation() # Delegation | submit delegation to provided validator (optional)

try:
    # Submit delegation
    api_response = api_instance.submit_delegation(delegator_addr, delegation=delegation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->submit_delegation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **delegation** | [**Delegation**](Delegation.md)| submit delegation to provided validator | [optional] 

### Return type

[**BroadcastTxCommitResult**](BroadcastTxCommitResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_redelegation**
> StdTx submit_redelegation(delegator_addr, delegation=delegation)

Submit a redelegation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator
delegation = swagger_client.Delegation2() # Delegation2 | The sender and tx information (optional)

try:
    # Submit a redelegation
    api_response = api_instance.submit_redelegation(delegator_addr, delegation=delegation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->submit_redelegation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **delegation** | [**Delegation2**](Delegation2.md)| The sender and tx information | [optional] 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undelegate**
> BroadcastTxCommitResult undelegate(delegator_addr, delegation=delegation)

Submit an unbonding delegation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator
delegation = swagger_client.Delegation1() # Delegation1 | The password of the account to remove from the KMS (optional)

try:
    # Submit an unbonding delegation
    api_response = api_instance.undelegate(delegator_addr, delegation=delegation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->undelegate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **delegation** | [**Delegation1**](Delegation1.md)| The password of the account to remove from the KMS | [optional] 

### Return type

[**BroadcastTxCommitResult**](BroadcastTxCommitResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

