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


class InlineResponse20035Result(object):
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
        'activation_fee': 'str',
        'lock_coins_fee': 'str'
    }

    attribute_map = {
        'activation_fee': 'activation_fee',
        'lock_coins_fee': 'lock_coins_fee'
    }

    def __init__(self, activation_fee=None, lock_coins_fee=None):  # noqa: E501
        """InlineResponse20035Result - a model defined in Swagger"""  # noqa: E501

        self._activation_fee = None
        self._lock_coins_fee = None
        self.discriminator = None

        if activation_fee is not None:
            self.activation_fee = activation_fee
        if lock_coins_fee is not None:
            self.lock_coins_fee = lock_coins_fee

    @property
    def activation_fee(self):
        """Gets the activation_fee of this InlineResponse20035Result.  # noqa: E501


        :return: The activation_fee of this InlineResponse20035Result.  # noqa: E501
        :rtype: str
        """
        return self._activation_fee

    @activation_fee.setter
    def activation_fee(self, activation_fee):
        """Sets the activation_fee of this InlineResponse20035Result.


        :param activation_fee: The activation_fee of this InlineResponse20035Result.  # noqa: E501
        :type: str
        """

        self._activation_fee = activation_fee

    @property
    def lock_coins_fee(self):
        """Gets the lock_coins_fee of this InlineResponse20035Result.  # noqa: E501


        :return: The lock_coins_fee of this InlineResponse20035Result.  # noqa: E501
        :rtype: str
        """
        return self._lock_coins_fee

    @lock_coins_fee.setter
    def lock_coins_fee(self, lock_coins_fee):
        """Sets the lock_coins_fee of this InlineResponse20035Result.


        :param lock_coins_fee: The lock_coins_fee of this InlineResponse20035Result.  # noqa: E501
        :type: str
        """

        self._lock_coins_fee = lock_coins_fee

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
        if issubclass(InlineResponse20035Result, dict):
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
        if not isinstance(other, InlineResponse20035Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
