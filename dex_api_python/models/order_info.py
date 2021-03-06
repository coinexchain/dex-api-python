# coding: utf-8

"""
    CET-Lite for CoinEx Chain

    A REST interface for state queries, transaction generation and broadcasting.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OrderInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'order_type': 'int',
        'trading_pair': 'str',
        'price_precision': 'str',
        'price': 'str',
        'quantity': 'str',
        'side': 'int',
        'identify': 'int',
        'sender': 'str',
        'sequence': 'str',
        'time_in_force': 'str',
        'height': 'str',
        'frozen_fee': 'str',
        'left_stock': 'str',
        'freeze': 'str',
        'deal_stock': 'str',
        'deal_money': 'str'
    }

    attribute_map = {
        'order_type': 'order_type',
        'trading_pair': 'trading_pair',
        'price_precision': 'price_precision',
        'price': 'price',
        'quantity': 'quantity',
        'side': 'side',
        'identify': 'identify',
        'sender': 'sender',
        'sequence': 'sequence',
        'time_in_force': 'time_in_force',
        'height': 'height',
        'frozen_fee': 'frozen_fee',
        'left_stock': 'left_stock',
        'freeze': 'freeze',
        'deal_stock': 'DealStock',
        'deal_money': 'DealMoney'
    }

    def __init__(self, order_type=None, trading_pair=None, price_precision=None, price=None, quantity=None, side=None, identify=None, sender=None, sequence=None, time_in_force=None, height=None, frozen_fee=None, left_stock=None, freeze=None, deal_stock=None, deal_money=None):  # noqa: E501
        """OrderInfo - a model defined in Swagger"""  # noqa: E501

        self._order_type = None
        self._trading_pair = None
        self._price_precision = None
        self._price = None
        self._quantity = None
        self._side = None
        self._identify = None
        self._sender = None
        self._sequence = None
        self._time_in_force = None
        self._height = None
        self._frozen_fee = None
        self._left_stock = None
        self._freeze = None
        self._deal_stock = None
        self._deal_money = None
        self.discriminator = None

        self.order_type = order_type
        self.trading_pair = trading_pair
        if price_precision is not None:
            self.price_precision = price_precision
        self.price = price
        self.quantity = quantity
        self.side = side
        self.identify = identify
        if sender is not None:
            self.sender = sender
        if sequence is not None:
            self.sequence = sequence
        if time_in_force is not None:
            self.time_in_force = time_in_force
        if height is not None:
            self.height = height
        if frozen_fee is not None:
            self.frozen_fee = frozen_fee
        if left_stock is not None:
            self.left_stock = left_stock
        if freeze is not None:
            self.freeze = freeze
        if deal_stock is not None:
            self.deal_stock = deal_stock
        if deal_money is not None:
            self.deal_money = deal_money

    @property
    def order_type(self):
        """Gets the order_type of this OrderInfo.  # noqa: E501

        The identify of the price limit : 2; (Currently, only price limit orders are supported)  # noqa: E501

        :return: The order_type of this OrderInfo.  # noqa: E501
        :rtype: int
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this OrderInfo.

        The identify of the price limit : 2; (Currently, only price limit orders are supported)  # noqa: E501

        :param order_type: The order_type of this OrderInfo.  # noqa: E501
        :type: int
        """
        if order_type is None:
            raise ValueError("Invalid value for `order_type`, must not be `None`")  # noqa: E501

        self._order_type = order_type

    @property
    def trading_pair(self):
        """Gets the trading_pair of this OrderInfo.  # noqa: E501


        :return: The trading_pair of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._trading_pair

    @trading_pair.setter
    def trading_pair(self, trading_pair):
        """Sets the trading_pair of this OrderInfo.


        :param trading_pair: The trading_pair of this OrderInfo.  # noqa: E501
        :type: str
        """
        if trading_pair is None:
            raise ValueError("Invalid value for `trading_pair`, must not be `None`")  # noqa: E501

        self._trading_pair = trading_pair

    @property
    def price_precision(self):
        """Gets the price_precision of this OrderInfo.  # noqa: E501


        :return: The price_precision of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._price_precision

    @price_precision.setter
    def price_precision(self, price_precision):
        """Sets the price_precision of this OrderInfo.


        :param price_precision: The price_precision of this OrderInfo.  # noqa: E501
        :type: str
        """

        self._price_precision = price_precision

    @property
    def price(self):
        """Gets the price of this OrderInfo.  # noqa: E501


        :return: The price of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OrderInfo.


        :param price: The price of this OrderInfo.  # noqa: E501
        :type: str
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def quantity(self):
        """Gets the quantity of this OrderInfo.  # noqa: E501


        :return: The quantity of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OrderInfo.


        :param quantity: The quantity of this OrderInfo.  # noqa: E501
        :type: str
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def side(self):
        """Gets the side of this OrderInfo.  # noqa: E501

        The buying or selling direction of an order.(buy : 1; sell : 2)  # noqa: E501

        :return: The side of this OrderInfo.  # noqa: E501
        :rtype: int
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this OrderInfo.

        The buying or selling direction of an order.(buy : 1; sell : 2)  # noqa: E501

        :param side: The side of this OrderInfo.  # noqa: E501
        :type: int
        """
        if side is None:
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501

        self._side = side

    @property
    def identify(self):
        """Gets the identify of this OrderInfo.  # noqa: E501

        A transaction can contain multiple order creation messages, the identify field was added to the order creation message to give each order a unique ID. So the order ID consists of user address, user sequence, identify.  # noqa: E501

        :return: The identify of this OrderInfo.  # noqa: E501
        :rtype: int
        """
        return self._identify

    @identify.setter
    def identify(self, identify):
        """Sets the identify of this OrderInfo.

        A transaction can contain multiple order creation messages, the identify field was added to the order creation message to give each order a unique ID. So the order ID consists of user address, user sequence, identify.  # noqa: E501

        :param identify: The identify of this OrderInfo.  # noqa: E501
        :type: int
        """
        if identify is None:
            raise ValueError("Invalid value for `identify`, must not be `None`")  # noqa: E501

        self._identify = identify

    @property
    def sender(self):
        """Gets the sender of this OrderInfo.  # noqa: E501


        :return: The sender of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this OrderInfo.


        :param sender: The sender of this OrderInfo.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def sequence(self):
        """Gets the sequence of this OrderInfo.  # noqa: E501


        :return: The sequence of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this OrderInfo.


        :param sequence: The sequence of this OrderInfo.  # noqa: E501
        :type: str
        """

        self._sequence = sequence

    @property
    def time_in_force(self):
        """Gets the time_in_force of this OrderInfo.  # noqa: E501


        :return: The time_in_force of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """Sets the time_in_force of this OrderInfo.


        :param time_in_force: The time_in_force of this OrderInfo.  # noqa: E501
        :type: str
        """

        self._time_in_force = time_in_force

    @property
    def height(self):
        """Gets the height of this OrderInfo.  # noqa: E501


        :return: The height of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this OrderInfo.


        :param height: The height of this OrderInfo.  # noqa: E501
        :type: str
        """

        self._height = height

    @property
    def frozen_fee(self):
        """Gets the frozen_fee of this OrderInfo.  # noqa: E501


        :return: The frozen_fee of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._frozen_fee

    @frozen_fee.setter
    def frozen_fee(self, frozen_fee):
        """Sets the frozen_fee of this OrderInfo.


        :param frozen_fee: The frozen_fee of this OrderInfo.  # noqa: E501
        :type: str
        """

        self._frozen_fee = frozen_fee

    @property
    def left_stock(self):
        """Gets the left_stock of this OrderInfo.  # noqa: E501


        :return: The left_stock of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._left_stock

    @left_stock.setter
    def left_stock(self, left_stock):
        """Sets the left_stock of this OrderInfo.


        :param left_stock: The left_stock of this OrderInfo.  # noqa: E501
        :type: str
        """

        self._left_stock = left_stock

    @property
    def freeze(self):
        """Gets the freeze of this OrderInfo.  # noqa: E501


        :return: The freeze of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._freeze

    @freeze.setter
    def freeze(self, freeze):
        """Sets the freeze of this OrderInfo.


        :param freeze: The freeze of this OrderInfo.  # noqa: E501
        :type: str
        """

        self._freeze = freeze

    @property
    def deal_stock(self):
        """Gets the deal_stock of this OrderInfo.  # noqa: E501


        :return: The deal_stock of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._deal_stock

    @deal_stock.setter
    def deal_stock(self, deal_stock):
        """Sets the deal_stock of this OrderInfo.


        :param deal_stock: The deal_stock of this OrderInfo.  # noqa: E501
        :type: str
        """

        self._deal_stock = deal_stock

    @property
    def deal_money(self):
        """Gets the deal_money of this OrderInfo.  # noqa: E501


        :return: The deal_money of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._deal_money

    @deal_money.setter
    def deal_money(self, deal_money):
        """Sets the deal_money of this OrderInfo.


        :param deal_money: The deal_money of this OrderInfo.  # noqa: E501
        :type: str
        """

        self._deal_money = deal_money

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OrderInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrderInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
