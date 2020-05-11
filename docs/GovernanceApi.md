# dex_api_python.GovernanceApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deposit_to_proposal**](GovernanceApi.md#deposit_to_proposal) | **POST** /gov/proposals/{proposalId}/deposits | Deposit tokens to a proposal
[**get_deposit_by_addr**](GovernanceApi.md#get_deposit_by_addr) | **GET** /gov/proposals/{proposalId}/deposits/{depositor} | Query deposit
[**get_deposit_parameters**](GovernanceApi.md#get_deposit_parameters) | **GET** /gov/parameters/deposit | Query governance deposit parameters
[**get_deposits**](GovernanceApi.md#get_deposits) | **GET** /gov/proposals/{proposalId}/deposits | Query deposits
[**get_proposal_by_id**](GovernanceApi.md#get_proposal_by_id) | **GET** /gov/proposals/{proposalId} | Query a proposal
[**get_proposals**](GovernanceApi.md#get_proposals) | **GET** /gov/proposals | Query proposals
[**get_proposer**](GovernanceApi.md#get_proposer) | **GET** /gov/proposals/{proposalId}/proposer | Query proposer
[**get_tally**](GovernanceApi.md#get_tally) | **GET** /gov/proposals/{proposalId}/tally | Get a proposal&#39;s tally result at the current time
[**get_tallying_parameters**](GovernanceApi.md#get_tallying_parameters) | **GET** /gov/parameters/tallying | Query governance tally parameters
[**get_voter_by_addr**](GovernanceApi.md#get_voter_by_addr) | **GET** /gov/proposals/{proposalId}/votes/{voter} | Query vote
[**get_voters**](GovernanceApi.md#get_voters) | **GET** /gov/proposals/{proposalId}/votes | Query voters
[**get_voting_parameters**](GovernanceApi.md#get_voting_parameters) | **GET** /gov/parameters/voting | Query governance voting parameters
[**submit_community_pool_spend_proposal**](GovernanceApi.md#submit_community_pool_spend_proposal) | **POST** /gov/proposals/community_pool_spend | Generate a community pool spend proposal transaction
[**submit_parameter_change_proposal**](GovernanceApi.md#submit_parameter_change_proposal) | **POST** /gov/proposals/param_change | Generate a parameter change proposal transaction
[**submit_proposal**](GovernanceApi.md#submit_proposal) | **POST** /gov/proposals | Submit a proposal
[**vote_proposal**](GovernanceApi.md#vote_proposal) | **POST** /gov/proposals/{proposalId}/votes | Vote a proposal


# **deposit_to_proposal**
> BroadcastTxCommitResult deposit_to_proposal(proposal_id, post_deposit_body)

Deposit tokens to a proposal

Send transaction to deposit tokens to a proposal

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.GovernanceApi()
proposal_id = '2' # str | proposal id
post_deposit_body = dex_api_python.PostDepositBody() # PostDepositBody | 

try:
    # Deposit tokens to a proposal
    api_response = api_instance.deposit_to_proposal(proposal_id, post_deposit_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->deposit_to_proposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal id | 
 **post_deposit_body** | [**PostDepositBody**](PostDepositBody.md)|  | 

### Return type

[**BroadcastTxCommitResult**](BroadcastTxCommitResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deposit_by_addr**
> InlineResponse20022 get_deposit_by_addr(proposal_id, depositor)

Query deposit

Query deposit by proposalId and depositor address

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.GovernanceApi()
proposal_id = '2' # str | proposal id
depositor = 'coinex1xl6453f6q6dv5770c9ue6hspdc0vxfuqtudkhz' # str | Bech32 depositor address

try:
    # Query deposit
    api_response = api_instance.get_deposit_by_addr(proposal_id, depositor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->get_deposit_by_addr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal id | 
 **depositor** | **str**| Bech32 depositor address | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deposit_parameters**
> InlineResponse20026 get_deposit_parameters()

Query governance deposit parameters

Query governance deposit parameters. The max_deposit_period units are in nanoseconds.

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.GovernanceApi()

try:
    # Query governance deposit parameters
    api_response = api_instance.get_deposit_parameters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->get_deposit_parameters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deposits**
> InlineResponse20021 get_deposits(proposal_id)

Query deposits

Query deposits by proposalId

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.GovernanceApi()
proposal_id = '2' # str | 

try:
    # Query deposits
    api_response = api_instance.get_deposits(proposal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->get_deposits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**|  | 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_proposal_by_id**
> InlineResponse20019 get_proposal_by_id(proposal_id)

Query a proposal

Query a proposal by id

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.GovernanceApi()
proposal_id = '1' # str | 

try:
    # Query a proposal
    api_response = api_instance.get_proposal_by_id(proposal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->get_proposal_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**|  | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_proposals**
> InlineResponse20018 get_proposals(voter=voter, depositor=depositor, status=status)

Query proposals

Query proposals information with parameters

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.GovernanceApi()
voter = 'voter_example' # str | voter address (optional)
depositor = 'depositor_example' # str | depositor address (optional)
status = 'status_example' # str | proposal status, valid values can be `\"deposit_period\"`, `\"voting_period\"`, `\"passed\"`, `\"rejected\"` (optional)

try:
    # Query proposals
    api_response = api_instance.get_proposals(voter=voter, depositor=depositor, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->get_proposals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voter** | **str**| voter address | [optional] 
 **depositor** | **str**| depositor address | [optional] 
 **status** | **str**| proposal status, valid values can be &#x60;\&quot;deposit_period\&quot;&#x60;, &#x60;\&quot;voting_period\&quot;&#x60;, &#x60;\&quot;passed\&quot;&#x60;, &#x60;\&quot;rejected\&quot;&#x60; | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_proposer**
> InlineResponse20020 get_proposer(proposal_id)

Query proposer

Query for the proposer for a proposal

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.GovernanceApi()
proposal_id = '2' # str | 

try:
    # Query proposer
    api_response = api_instance.get_proposer(proposal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->get_proposer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**|  | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tally**
> InlineResponse20025 get_tally(proposal_id)

Get a proposal's tally result at the current time

Gets a proposal's tally result at the current time. If the proposal is pending deposits (i.e status 'DepositPeriod') it returns an empty tally result.

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.GovernanceApi()
proposal_id = '2' # str | proposal id

try:
    # Get a proposal's tally result at the current time
    api_response = api_instance.get_tally(proposal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->get_tally: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal id | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tallying_parameters**
> InlineResponse20027 get_tallying_parameters()

Query governance tally parameters

Query governance tally parameters

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.GovernanceApi()

try:
    # Query governance tally parameters
    api_response = api_instance.get_tallying_parameters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->get_tallying_parameters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voter_by_addr**
> InlineResponse20024 get_voter_by_addr(proposal_id, voter)

Query vote

Query vote information by proposal Id and voter address

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.GovernanceApi()
proposal_id = '2' # str | proposal id
voter = 'coinex1qwl879nx9t6kef4supyazayf7vjhennyjqwjgr' # str | Bech32 voter address

try:
    # Query vote
    api_response = api_instance.get_voter_by_addr(proposal_id, voter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->get_voter_by_addr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal id | 
 **voter** | **str**| Bech32 voter address | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voters**
> InlineResponse20023 get_voters(proposal_id)

Query voters

Query voters information by proposalId

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.GovernanceApi()
proposal_id = '2' # str | proposal id

try:
    # Query voters
    api_response = api_instance.get_voters(proposal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->get_voters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal id | 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voting_parameters**
> InlineResponse20028 get_voting_parameters()

Query governance voting parameters

Query governance voting parameters. The voting_period units are in nanoseconds.

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.GovernanceApi()

try:
    # Query governance voting parameters
    api_response = api_instance.get_voting_parameters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->get_voting_parameters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_community_pool_spend_proposal**
> StdTx submit_community_pool_spend_proposal(post_proposal_body)

Generate a community pool spend proposal transaction

Generate a community pool spend proposal transaction

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.GovernanceApi()
post_proposal_body = dex_api_python.PostProposalBody2() # PostProposalBody2 | The community pool spend proposal body contains coin amount to be spent

try:
    # Generate a community pool spend proposal transaction
    api_response = api_instance.submit_community_pool_spend_proposal(post_proposal_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->submit_community_pool_spend_proposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_proposal_body** | [**PostProposalBody2**](PostProposalBody2.md)| The community pool spend proposal body contains coin amount to be spent | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_parameter_change_proposal**
> StdTx submit_parameter_change_proposal(post_proposal_body)

Generate a parameter change proposal transaction

Generate a parameter change proposal transaction

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.GovernanceApi()
post_proposal_body = dex_api_python.PostProposalBody1() # PostProposalBody1 | The parameter change proposal body that contains all parameter changes

try:
    # Generate a parameter change proposal transaction
    api_response = api_instance.submit_parameter_change_proposal(post_proposal_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->submit_parameter_change_proposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_proposal_body** | [**PostProposalBody1**](PostProposalBody1.md)| The parameter change proposal body that contains all parameter changes | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_proposal**
> StdTx submit_proposal(post_proposal_body)

Submit a proposal

Send transaction to submit a proposal

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.GovernanceApi()
post_proposal_body = dex_api_python.PostProposalBody() # PostProposalBody | valid value of `\"proposal_type\"` can be `\"text\"`, `\"parameter_change\"`, `\"software_upgrade\"`

try:
    # Submit a proposal
    api_response = api_instance.submit_proposal(post_proposal_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->submit_proposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_proposal_body** | [**PostProposalBody**](PostProposalBody.md)| valid value of &#x60;\&quot;proposal_type\&quot;&#x60; can be &#x60;\&quot;text\&quot;&#x60;, &#x60;\&quot;parameter_change\&quot;&#x60;, &#x60;\&quot;software_upgrade\&quot;&#x60; | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vote_proposal**
> BroadcastTxCommitResult vote_proposal(proposal_id, post_vote_body)

Vote a proposal

Send transaction to vote a proposal

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.GovernanceApi()
proposal_id = '2' # str | proposal id
post_vote_body = dex_api_python.PostVoteBody() # PostVoteBody | valid value of `\"option\"` field can be `\"yes\"`, `\"no\"`, `\"no_with_veto\"` and `\"abstain\"`

try:
    # Vote a proposal
    api_response = api_instance.vote_proposal(proposal_id, post_vote_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->vote_proposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal id | 
 **post_vote_body** | [**PostVoteBody**](PostVoteBody.md)| valid value of &#x60;\&quot;option\&quot;&#x60; field can be &#x60;\&quot;yes\&quot;&#x60;, &#x60;\&quot;no\&quot;&#x60;, &#x60;\&quot;no_with_veto\&quot;&#x60; and &#x60;\&quot;abstain\&quot;&#x60; | 

### Return type

[**BroadcastTxCommitResult**](BroadcastTxCommitResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

