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


class Info1(object):
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
        'price_precision': 'str',
        'trading_pair': 'str'
    }

    attribute_map = {
        'base_req': 'base_req',
        'price_precision': 'price_precision',
        'trading_pair': 'trading_pair'
    }

    def __init__(self, base_req=None, price_precision=None, trading_pair=None):  # noqa: E501
        """Info1 - a model defined in Swagger"""  # noqa: E501

        self._base_req = None
        self._price_precision = None
        self._trading_pair = None
        self.discriminator = None

        if base_req is not None:
            self.base_req = base_req
        if price_precision is not None:
            self.price_precision = price_precision
        if trading_pair is not None:
            self.trading_pair = trading_pair

    @property
    def base_req(self):
        """Gets the base_req of this Info1.  # noqa: E501


        :return: The base_req of this Info1.  # noqa: E501
        :rtype: BaseReq
        """
        return self._base_req

    @base_req.setter
    def base_req(self, base_req):
        """Sets the base_req of this Info1.


        :param base_req: The base_req of this Info1.  # noqa: E501
        :type: BaseReq
        """

        self._base_req = base_req

    @property
    def price_precision(self):
        """Gets the price_precision of this Info1.  # noqa: E501


        :return: The price_precision of this Info1.  # noqa: E501
        :rtype: str
        """
        return self._price_precision

    @price_precision.setter
    def price_precision(self, price_precision):
        """Sets the price_precision of this Info1.


        :param price_precision: The price_precision of this Info1.  # noqa: E501
        :type: str
        """

        self._price_precision = price_precision

    @property
    def trading_pair(self):
        """Gets the trading_pair of this Info1.  # noqa: E501


        :return: The trading_pair of this Info1.  # noqa: E501
        :rtype: str
        """
        return self._trading_pair

    @trading_pair.setter
    def trading_pair(self, trading_pair):
        """Sets the trading_pair of this Info1.


        :param trading_pair: The trading_pair of this Info1.  # noqa: E501
        :type: str
        """

        self._trading_pair = trading_pair

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
        if issubclass(Info1, dict):
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
        if not isinstance(other, Info1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
