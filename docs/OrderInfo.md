# OrderInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_type** | **int** | The identify of the price limit : 2; (Currently, only price limit orders are supported) | 
**trading_pair** | **str** |  | 
**price_precision** | **str** |  | [optional] 
**price** | **str** |  | 
**quantity** | **str** |  | 
**side** | **int** | The buying or selling direction of an order.(buy : 1; sell : 2) | 
**identify** | **int** | A transaction can contain multiple order creation messages, the identify field was added to the order creation message to give each order a unique ID. So the order ID consists of user address, user sequence, identify. | 
**sender** | **str** |  | [optional] 
**sequence** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**height** | **str** |  | [optional] 
**frozen_fee** | **str** |  | [optional] 
**left_stock** | **str** |  | [optional] 
**freeze** | **str** |  | [optional] 
**deal_stock** | **str** |  | [optional] 
**deal_money** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


