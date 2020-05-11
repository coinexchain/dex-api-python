# CreateOrderInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**sender** | [**Address**](Address.md) |  | [optional] 
**trading_pair** | **str** |  | [optional] 
**order_type** | **int** | Limited value 2 | [optional] 
**price** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**side** | **int** | BUY:1/SELL:2 | [optional] 
**time_in_force** | **int** | GTE:3/IOC:4 | [optional] 
**feature_fee** | **int** | Order feature fee, sato.CET as the unit | [optional] 
**height** | **int** |  | [optional] 
**frozen_fee** | **int** | Order frozen fee, sato.CET as the unit | [optional] 
**freeze** | **int** | Freeze sato.CET amount | [optional] 
**tx_hash** | **str** | The tx hash | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


