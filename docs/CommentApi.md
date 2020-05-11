# dex_api_python.CommentApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**followup_comment**](CommentApi.md#followup_comment) | **POST** /comment/followup-comment | Post a follow-up comment under some thread
[**new_thread**](CommentApi.md#new_thread) | **POST** /comment/new-thread | Post a new comment to open a new thread
[**query_comment**](CommentApi.md#query_comment) | **GET** /comment/comments | Query token comment
[**reward_comments**](CommentApi.md#reward_comments) | **POST** /comment/reward-comments | reward some comments with coins


# **followup_comment**
> StdTx followup_comment(followup_comment_req)

Post a follow-up comment under some thread

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.CommentApi()
followup_comment_req = dex_api_python.FollowupCommentReq() # FollowupCommentReq | Post a follow-up comment

try:
    # Post a follow-up comment under some thread
    api_response = api_instance.followup_comment(followup_comment_req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->followup_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **followup_comment_req** | [**FollowupCommentReq**](FollowupCommentReq.md)| Post a follow-up comment | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_thread**
> StdTx new_thread(new_thread_req)

Post a new comment to open a new thread

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.CommentApi()
new_thread_req = dex_api_python.NewThreadReq() # NewThreadReq | open a new thread

try:
    # Post a new comment to open a new thread
    api_response = api_instance.new_thread(new_thread_req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->new_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_thread_req** | [**NewThreadReq**](NewThreadReq.md)| open a new thread | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_comment**
> InlineResponse20063 query_comment(token, time, sid, count)

Query token comment

Query all comments about given token until to time

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.CommentApi()
token = 'token_example' # str | Symbol
time = 789 # int | Unix timestamp
sid = 789 # int | Sequence id
count = 56 # int | Querier comment count limited to 1024

try:
    # Query token comment
    api_response = api_instance.query_comment(token, time, sid, count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->query_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Symbol | 
 **time** | **int**| Unix timestamp | 
 **sid** | **int**| Sequence id | 
 **count** | **int**| Querier comment count limited to 1024 | 

### Return type

[**InlineResponse20063**](InlineResponse20063.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reward_comments**
> StdTx reward_comments(reward_comments_req)

reward some comments with coins

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.CommentApi()
reward_comments_req = dex_api_python.RewardCommentsReq() # RewardCommentsReq | reward some comments

try:
    # reward some comments with coins
    api_response = api_instance.reward_comments(reward_comments_req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentApi->reward_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reward_comments_req** | [**RewardCommentsReq**](RewardCommentsReq.md)| reward some comments | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

