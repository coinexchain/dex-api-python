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


class BancorInit(object):
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
        'base_req': 'BaseReq',
        'stock': 'str',
        'money': 'str',
        'init_price': 'str',
        'max_supply': 'str',
        'stock_precision': 'str',
        'max_price': 'str',
        'max_money': 'str',
        'earliest_cancel_time': 'str'
    }

    attribute_map = {
        'base_req': 'base_req',
        'stock': 'stock',
        'money': 'money',
        'init_price': 'init_price',
        'max_supply': 'max_supply',
        'stock_precision': 'stock_precision',
        'max_price': 'max_price',
        'max_money': 'max_money',
        'earliest_cancel_time': 'earliest_cancel_time'
    }

    def __init__(self, base_req=None, stock=None, money=None, init_price=None, max_supply=None, stock_precision=None, max_price=None, max_money=None, earliest_cancel_time=None):  # noqa: E501
        """BancorInit - a model defined in Swagger"""  # noqa: E501

        self._base_req = None
        self._stock = None
        self._money = None
        self._init_price = None
        self._max_supply = None
        self._stock_precision = None
        self._max_price = None
        self._max_money = None
        self._earliest_cancel_time = None
        self.discriminator = None

        self.base_req = base_req
        self.stock = stock
        self.money = money
        self.init_price = init_price
        self.max_supply = max_supply
        if stock_precision is not None:
            self.stock_precision = stock_precision
        self.max_price = max_price
        self.max_money = max_money
        self.earliest_cancel_time = earliest_cancel_time

    @property
    def base_req(self):
        """Gets the base_req of this BancorInit.  # noqa: E501


        :return: The base_req of this BancorInit.  # noqa: E501
        :rtype: BaseReq
        """
        return self._base_req

    @base_req.setter
    def base_req(self, base_req):
        """Sets the base_req of this BancorInit.


        :param base_req: The base_req of this BancorInit.  # noqa: E501
        :type: BaseReq
        """
        if base_req is None:
            raise ValueError("Invalid value for `base_req`, must not be `None`")  # noqa: E501

        self._base_req = base_req

    @property
    def stock(self):
        """Gets the stock of this BancorInit.  # noqa: E501


        :return: The stock of this BancorInit.  # noqa: E501
        :rtype: str
        """
        return self._stock

    @stock.setter
    def stock(self, stock):
        """Sets the stock of this BancorInit.


        :param stock: The stock of this BancorInit.  # noqa: E501
        :type: str
        """
        if stock is None:
            raise ValueError("Invalid value for `stock`, must not be `None`")  # noqa: E501

        self._stock = stock

    @property
    def money(self):
        """Gets the money of this BancorInit.  # noqa: E501


        :return: The money of this BancorInit.  # noqa: E501
        :rtype: str
        """
        return self._money

    @money.setter
    def money(self, money):
        """Sets the money of this BancorInit.


        :param money: The money of this BancorInit.  # noqa: E501
        :type: str
        """
        if money is None:
            raise ValueError("Invalid value for `money`, must not be `None`")  # noqa: E501

        self._money = money

    @property
    def init_price(self):
        """Gets the init_price of this BancorInit.  # noqa: E501


        :return: The init_price of this BancorInit.  # noqa: E501
        :rtype: str
        """
        return self._init_price

    @init_price.setter
    def init_price(self, init_price):
        """Sets the init_price of this BancorInit.


        :param init_price: The init_price of this BancorInit.  # noqa: E501
        :type: str
        """
        if init_price is None:
            raise ValueError("Invalid value for `init_price`, must not be `None`")  # noqa: E501

        self._init_price = init_price

    @property
    def max_supply(self):
        """Gets the max_supply of this BancorInit.  # noqa: E501


        :return: The max_supply of this BancorInit.  # noqa: E501
        :rtype: str
        """
        return self._max_supply

    @max_supply.setter
    def max_supply(self, max_supply):
        """Sets the max_supply of this BancorInit.


        :param max_supply: The max_supply of this BancorInit.  # noqa: E501
        :type: str
        """
        if max_supply is None:
            raise ValueError("Invalid value for `max_supply`, must not be `None`")  # noqa: E501

        self._max_supply = max_supply

    @property
    def stock_precision(self):
        """Gets the stock_precision of this BancorInit.  # noqa: E501


        :return: The stock_precision of this BancorInit.  # noqa: E501
        :rtype: str
        """
        return self._stock_precision

    @stock_precision.setter
    def stock_precision(self, stock_precision):
        """Sets the stock_precision of this BancorInit.


        :param stock_precision: The stock_precision of this BancorInit.  # noqa: E501
        :type: str
        """

        self._stock_precision = stock_precision

    @property
    def max_price(self):
        """Gets the max_price of this BancorInit.  # noqa: E501


        :return: The max_price of this BancorInit.  # noqa: E501
        :rtype: str
        """
        return self._max_price

    @max_price.setter
    def max_price(self, max_price):
        """Sets the max_price of this BancorInit.


        :param max_price: The max_price of this BancorInit.  # noqa: E501
        :type: str
        """
        if max_price is None:
            raise ValueError("Invalid value for `max_price`, must not be `None`")  # noqa: E501

        self._max_price = max_price

    @property
    def max_money(self):
        """Gets the max_money of this BancorInit.  # noqa: E501


        :return: The max_money of this BancorInit.  # noqa: E501
        :rtype: str
        """
        return self._max_money

    @max_money.setter
    def max_money(self, max_money):
        """Sets the max_money of this BancorInit.


        :param max_money: The max_money of this BancorInit.  # noqa: E501
        :type: str
        """
        if max_money is None:
            raise ValueError("Invalid value for `max_money`, must not be `None`")  # noqa: E501

        self._max_money = max_money

    @property
    def earliest_cancel_time(self):
        """Gets the earliest_cancel_time of this BancorInit.  # noqa: E501


        :return: The earliest_cancel_time of this BancorInit.  # noqa: E501
        :rtype: str
        """
        return self._earliest_cancel_time

    @earliest_cancel_time.setter
    def earliest_cancel_time(self, earliest_cancel_time):
        """Sets the earliest_cancel_time of this BancorInit.


        :param earliest_cancel_time: The earliest_cancel_time of this BancorInit.  # noqa: E501
        :type: str
        """
        if earliest_cancel_time is None:
            raise ValueError("Invalid value for `earliest_cancel_time`, must not be `None`")  # noqa: E501

        self._earliest_cancel_time = earliest_cancel_time

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
        if issubclass(BancorInit, dict):
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
        if not isinstance(other, BancorInit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other