# dex_api_python.MarketApi

All URIs are relative to *https://dex-api.coinex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](MarketApi.md#cancel_order) | **POST** /market/cancel-order | Cancel the order
[**cancel_trading_pair**](MarketApi.md#cancel_trading_pair) | **POST** /market/cancel-trading-pair | Cancel the trading-pair
[**create_gte_order**](MarketApi.md#create_gte_order) | **POST** /market/gte-orders | Create GTE order in blockchain
[**create_ioc_order**](MarketApi.md#create_ioc_order) | **POST** /market/ioc-orders | Create IOC order in blockchain
[**create_trading_pair**](MarketApi.md#create_trading_pair) | **POST** /market/trading-pairs | Create trading-pair in blockchain
[**get_market_params**](MarketApi.md#get_market_params) | **GET** /market/parameters | Get the current market parameters
[**get_order**](MarketApi.md#get_order) | **GET** /market/orders/{order-id} | Query order info
[**get_orders**](MarketApi.md#get_orders) | **GET** /market/orders/account/{address} | Query user order-id list
[**get_orders_in_market**](MarketApi.md#get_orders_in_market) | **GET** /market/orderbook/{stock}/{money} | Query trading-pair&#39;s orderbook
[**get_trading_pair**](MarketApi.md#get_trading_pair) | **GET** /market/trading-pairs/{stock}/{money} | Query trading-pair info
[**modify_price_precision**](MarketApi.md#modify_price_precision) | **POST** /market/price-precision | Modify the price precision of the trading pair in the dex
[**query_candle_stick**](MarketApi.md#query_candle_stick) | **GET** /market/candle-sticks | Query market candleStick
[**query_deal**](MarketApi.md#query_deal) | **GET** /market/deals | Query market deal
[**query_depth**](MarketApi.md#query_depth) | **GET** /market/depths | Query market depth
[**query_order**](MarketApi.md#query_order) | **GET** /market/user-orders | Query account&#39;s order
[**query_tickers**](MarketApi.md#query_tickers) | **GET** /market/tickers | Query market tickers
[**query_trading_pairs**](MarketApi.md#query_trading_pairs) | **GET** /market/exist-trading-pairs | Query all trading-pair infos in blockchain


# **cancel_order**
> StdTx cancel_order(order_info)

Cancel the order

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MarketApi()
order_info = dex_api_python.OrderInfo() # OrderInfo | cancel order tx

try:
    # Cancel the order
    api_response = api_instance.cancel_order(order_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_info** | [**OrderInfo**](OrderInfo.md)| cancel order tx | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_trading_pair**
> StdTx cancel_trading_pair(info)

Cancel the trading-pair

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MarketApi()
info = dex_api_python.Info2() # Info2 | cancel trading-pair in dex

try:
    # Cancel the trading-pair
    api_response = api_instance.cancel_trading_pair(info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->cancel_trading_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **info** | [**Info2**](Info2.md)| cancel trading-pair in dex | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_gte_order**
> StdTx create_gte_order(order_info)

Create GTE order in blockchain

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MarketApi()
order_info = NULL # object | create order tx

try:
    # Create GTE order in blockchain
    api_response = api_instance.create_gte_order(order_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->create_gte_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_info** | [**object**](.md)| create order tx | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ioc_order**
> StdTx create_ioc_order(order_info)

Create IOC order in blockchain

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MarketApi()
order_info = NULL # object | create order tx

try:
    # Create IOC order in blockchain
    api_response = api_instance.create_ioc_order(order_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->create_ioc_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_info** | [**object**](.md)| create order tx | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_trading_pair**
> StdTx create_trading_pair(info)

Create trading-pair in blockchain

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MarketApi()
info = NULL # object | Create trading-pair

try:
    # Create trading-pair in blockchain
    api_response = api_instance.create_trading_pair(info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->create_trading_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **info** | [**object**](.md)| Create trading-pair | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_market_params**
> InlineResponse20042 get_market_params()

Get the current market parameters

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MarketApi()

try:
    # Get the current market parameters
    api_response = api_instance.get_market_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_market_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> InlineResponse20046 get_order(order_id)

Query order info

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MarketApi()
order_id = 'coinex1dmz7e2fddhejdz5n7e3qc5szx3zn2gj3ta8rwj' # str | The order id

try:
    # Query order info
    api_response = api_instance.get_order(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order id | 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders**
> InlineResponse20047 get_orders(address)

Query user order-id list

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MarketApi()
address = 'coinex1dmz7e2fddhejdz5n7e3qc5szx3zn2gj3ta8rwj' # str | The user address

try:
    # Query user order-id list
    api_response = api_instance.get_orders(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The user address | 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders_in_market**
> InlineResponse20045 get_orders_in_market(stock, money)

Query trading-pair's orderbook

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MarketApi()
stock = 'btc' # str | stock symbol
money = 'cet' # str | money symbol

try:
    # Query trading-pair's orderbook
    api_response = api_instance.get_orders_in_market(stock, money)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_orders_in_market: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock** | **str**| stock symbol | 
 **money** | **str**| money symbol | 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trading_pair**
> InlineResponse20044 get_trading_pair(stock, money)

Query trading-pair info

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MarketApi()
stock = 'btc' # str | stock symbol
money = 'cet' # str | money symbol

try:
    # Query trading-pair info
    api_response = api_instance.get_trading_pair(stock, money)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_trading_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock** | **str**| stock symbol | 
 **money** | **str**| money symbol | 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_price_precision**
> StdTx modify_price_precision(info)

Modify the price precision of the trading pair in the dex

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MarketApi()
info = dex_api_python.Info1() # Info1 | trading-pair, price-precision as params

try:
    # Modify the price precision of the trading pair in the dex
    api_response = api_instance.modify_price_precision(info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->modify_price_precision: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **info** | [**Info1**](Info1.md)| trading-pair, price-precision as params | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_candle_stick**
> list[CandleStick] query_candle_stick(market, timespan, time, sid, count)

Query market candleStick

Query candleStick until to given time

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MarketApi()
market = 'market_example' # str | stock/money
timespan = 'timespan_example' # str | 1min/1hour/1day
time = 789 # int | Unix timestamp
sid = 789 # int | Sequence id
count = 56 # int | Querier candleStick count limited to 1024

try:
    # Query market candleStick
    api_response = api_instance.query_candle_stick(market, timespan, time, sid, count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->query_candle_stick: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**| stock/money | 
 **timespan** | **str**| 1min/1hour/1day | 
 **time** | **int**| Unix timestamp | 
 **sid** | **int**| Sequence id | 
 **count** | **int**| Querier candleStick count limited to 1024 | 

### Return type

[**list[CandleStick]**](CandleStick.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_deal**
> InlineResponse20056 query_deal(market, time, sid, count)

Query market deal

Query market deal until to given time

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MarketApi()
market = 'market_example' # str | stock/money
time = 789 # int | Unix timestamp
sid = 789 # int | Sequence id
count = 56 # int | Querier deal count limited to 1024

try:
    # Query market deal
    api_response = api_instance.query_deal(market, time, sid, count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->query_deal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**| stock/money | 
 **time** | **int**| Unix timestamp | 
 **sid** | **int**| Sequence id | 
 **count** | **int**| Querier deal count limited to 1024 | 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_depth**
> InlineResponse20055 query_depth(market, count)

Query market depth

Query purchases and sales of a market at all price levels

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MarketApi()
market = 'market_example' # str | stock/money
count = 56 # int | Querier count limited to 1024

try:
    # Query market depth
    api_response = api_instance.query_depth(market, count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->query_depth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**| stock/money | 
 **count** | **int**| Querier count limited to 1024 | 

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_order**
> UserOrder query_order(account, time, sid, count, token=token, tag=tag)

Query account's order

Query account's order activities in all markets until to given time

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MarketApi()
account = 'account_example' # str | Bech32 address
time = 789 # int | Unix timestamp
sid = 789 # int | Sequence id
count = 56 # int | Querier order count limited to 1024
token = 'token_example' # str | Symbol (optional)
tag = 'tag_example' # str | Filter responses type by tag string create/fill/cancel (optional)

try:
    # Query account's order
    api_response = api_instance.query_order(account, time, sid, count, token=token, tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->query_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Bech32 address | 
 **time** | **int**| Unix timestamp | 
 **sid** | **int**| Sequence id | 
 **count** | **int**| Querier order count limited to 1024 | 
 **token** | **str**| Symbol | [optional] 
 **tag** | **str**| Filter responses type by tag string create/fill/cancel | [optional] 

### Return type

[**UserOrder**](UserOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_tickers**
> list[Tickers] query_tickers(market_list)

Query market tickers

Query tickers info

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MarketApi()
market_list = ['market_list_example'] # list[str] | Market count limited to 1~100

try:
    # Query market tickers
    api_response = api_instance.query_tickers(market_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->query_tickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_list** | [**list[str]**](str.md)| Market count limited to 1~100 | 

### Return type

[**list[Tickers]**](Tickers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_trading_pairs**
> InlineResponse20043 query_trading_pairs()

Query all trading-pair infos in blockchain

### Example
```python
from __future__ import print_function
import time
import dex_api_python
from dex_api_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dex_api_python.MarketApi()

try:
    # Query all trading-pair infos in blockchain
    api_response = api_instance.query_trading_pairs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->query_trading_pairs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

