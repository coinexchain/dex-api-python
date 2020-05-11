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


class UnbondingDelegationPair(object):
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
        'delegator_address': 'str',
        'validator_address': 'str',
        'entries': 'list[UnbondingEntries]'
    }

    attribute_map = {
        'delegator_address': 'delegator_address',
        'validator_address': 'validator_address',
        'entries': 'entries'
    }

    def __init__(self, delegator_address=None, validator_address=None, entries=None):  # noqa: E501
        """UnbondingDelegationPair - a model defined in Swagger"""  # noqa: E501

        self._delegator_address = None
        self._validator_address = None
        self._entries = None
        self.discriminator = None

        self.delegator_address = delegator_address
        self.validator_address = validator_address
        self.entries = entries

    @property
    def delegator_address(self):
        """Gets the delegator_address of this UnbondingDelegationPair.  # noqa: E501


        :return: The delegator_address of this UnbondingDelegationPair.  # noqa: E501
        :rtype: str
        """
        return self._delegator_address

    @delegator_address.setter
    def delegator_address(self, delegator_address):
        """Sets the delegator_address of this UnbondingDelegationPair.


        :param delegator_address: The delegator_address of this UnbondingDelegationPair.  # noqa: E501
        :type: str
        """
        if delegator_address is None:
            raise ValueError("Invalid value for `delegator_address`, must not be `None`")  # noqa: E501

        self._delegator_address = delegator_address

    @property
    def validator_address(self):
        """Gets the validator_address of this UnbondingDelegationPair.  # noqa: E501


        :return: The validator_address of this UnbondingDelegationPair.  # noqa: E501
        :rtype: str
        """
        return self._validator_address

    @validator_address.setter
    def validator_address(self, validator_address):
        """Sets the validator_address of this UnbondingDelegationPair.


        :param validator_address: The validator_address of this UnbondingDelegationPair.  # noqa: E501
        :type: str
        """
        if validator_address is None:
            raise ValueError("Invalid value for `validator_address`, must not be `None`")  # noqa: E501

        self._validator_address = validator_address

    @property
    def entries(self):
        """Gets the entries of this UnbondingDelegationPair.  # noqa: E501


        :return: The entries of this UnbondingDelegationPair.  # noqa: E501
        :rtype: list[UnbondingEntries]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this UnbondingDelegationPair.


        :param entries: The entries of this UnbondingDelegationPair.  # noqa: E501
        :type: list[UnbondingEntries]
        """
        if entries is None:
            raise ValueError("Invalid value for `entries`, must not be `None`")  # noqa: E501

        self._entries = entries

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
        if issubclass(UnbondingDelegationPair, dict):
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
        if not isinstance(other, UnbondingDelegationPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other