# PostTxBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_req** | [**BaseReq**](BaseReq.md) |  | 
**amount** | [**Coin**](Coin.md) |  | 
**unlock_time** | **str** |  | 
**sender** | **str** | The supervised amount sender&#39;s address (required when return or unlock-by-supervisor) | [optional] 
**supervisor** | **str** | The supervisor&#39;s address (required when create or unlock-by-sender if there is a supervisor) | [optional] 
**reward** | **str** |  | [optional] 
**operation** | **int** | Operation type (create: 0; return: 1; unlock-by-sender: 2; unlock-by-supervisor: 3) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


