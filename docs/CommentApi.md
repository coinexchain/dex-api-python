# swagger_client.CommentApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**followup_comment**](CommentApi.md#followup_comment) | **POST** /comment/followup-comment | Post a follow-up comment under some thread
[**new_thread**](CommentApi.md#new_thread) | **POST** /comment/new-thread | Post a new comment to open a new thread
[**reward_comments**](CommentApi.md#reward_comments) | **POST** /comment/reward-comments | reward some comments with coins


# **followup_comment**
> StdTx followup_comment(followup_comment_req)

Post a follow-up comment under some thread

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommentApi()
followup_comment_req = swagger_client.FollowupCommentReq() # FollowupCommentReq | Post a follow-up comment

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
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommentApi()
new_thread_req = swagger_client.NewThreadReq() # NewThreadReq | open a new thread

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

# **reward_comments**
> StdTx reward_comments(reward_comments_req)

reward some comments with coins

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommentApi()
reward_comments_req = swagger_client.RewardCommentsReq() # RewardCommentsReq | reward some comments

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

