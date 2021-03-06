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


class UserOrder(object):
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
        'create_order_info': 'UserOrderCreateOrderInfo',
        'fill_order_info': 'InlineResponse20056',
        'cancel_order_info': 'UserOrderCancelOrderInfo'
    }

    attribute_map = {
        'create_order_info': 'createOrderInfo',
        'fill_order_info': 'fillOrderInfo',
        'cancel_order_info': 'cancelOrderInfo'
    }

    def __init__(self, create_order_info=None, fill_order_info=None, cancel_order_info=None):  # noqa: E501
        """UserOrder - a model defined in Swagger"""  # noqa: E501

        self._create_order_info = None
        self._fill_order_info = None
        self._cancel_order_info = None
        self.discriminator = None

        if create_order_info is not None:
            self.create_order_info = create_order_info
        if fill_order_info is not None:
            self.fill_order_info = fill_order_info
        if cancel_order_info is not None:
            self.cancel_order_info = cancel_order_info

    @property
    def create_order_info(self):
        """Gets the create_order_info of this UserOrder.  # noqa: E501


        :return: The create_order_info of this UserOrder.  # noqa: E501
        :rtype: UserOrderCreateOrderInfo
        """
        return self._create_order_info

    @create_order_info.setter
    def create_order_info(self, create_order_info):
        """Sets the create_order_info of this UserOrder.


        :param create_order_info: The create_order_info of this UserOrder.  # noqa: E501
        :type: UserOrderCreateOrderInfo
        """

        self._create_order_info = create_order_info

    @property
    def fill_order_info(self):
        """Gets the fill_order_info of this UserOrder.  # noqa: E501


        :return: The fill_order_info of this UserOrder.  # noqa: E501
        :rtype: InlineResponse20056
        """
        return self._fill_order_info

    @fill_order_info.setter
    def fill_order_info(self, fill_order_info):
        """Sets the fill_order_info of this UserOrder.


        :param fill_order_info: The fill_order_info of this UserOrder.  # noqa: E501
        :type: InlineResponse20056
        """

        self._fill_order_info = fill_order_info

    @property
    def cancel_order_info(self):
        """Gets the cancel_order_info of this UserOrder.  # noqa: E501


        :return: The cancel_order_info of this UserOrder.  # noqa: E501
        :rtype: UserOrderCancelOrderInfo
        """
        return self._cancel_order_info

    @cancel_order_info.setter
    def cancel_order_info(self, cancel_order_info):
        """Sets the cancel_order_info of this UserOrder.


        :param cancel_order_info: The cancel_order_info of this UserOrder.  # noqa: E501
        :type: UserOrderCancelOrderInfo
        """

        self._cancel_order_info = cancel_order_info

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
        if issubclass(UserOrder, dict):
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
        if not isinstance(other, UserOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
