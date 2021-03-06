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


class TxQueryResult(object):
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
        'logs': 'str',
        'gas_wanted': 'str',
        'gas_used': 'str',
        'tags': 'list[KVPair]'
    }

    attribute_map = {
        'logs': 'logs',
        'gas_wanted': 'gas_wanted',
        'gas_used': 'gas_used',
        'tags': 'tags'
    }

    def __init__(self, logs=None, gas_wanted=None, gas_used=None, tags=None):  # noqa: E501
        """TxQueryResult - a model defined in Swagger"""  # noqa: E501

        self._logs = None
        self._gas_wanted = None
        self._gas_used = None
        self._tags = None
        self.discriminator = None

        if logs is not None:
            self.logs = logs
        if gas_wanted is not None:
            self.gas_wanted = gas_wanted
        if gas_used is not None:
            self.gas_used = gas_used
        if tags is not None:
            self.tags = tags

    @property
    def logs(self):
        """Gets the logs of this TxQueryResult.  # noqa: E501


        :return: The logs of this TxQueryResult.  # noqa: E501
        :rtype: str
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this TxQueryResult.


        :param logs: The logs of this TxQueryResult.  # noqa: E501
        :type: str
        """

        self._logs = logs

    @property
    def gas_wanted(self):
        """Gets the gas_wanted of this TxQueryResult.  # noqa: E501


        :return: The gas_wanted of this TxQueryResult.  # noqa: E501
        :rtype: str
        """
        return self._gas_wanted

    @gas_wanted.setter
    def gas_wanted(self, gas_wanted):
        """Sets the gas_wanted of this TxQueryResult.


        :param gas_wanted: The gas_wanted of this TxQueryResult.  # noqa: E501
        :type: str
        """

        self._gas_wanted = gas_wanted

    @property
    def gas_used(self):
        """Gets the gas_used of this TxQueryResult.  # noqa: E501


        :return: The gas_used of this TxQueryResult.  # noqa: E501
        :rtype: str
        """
        return self._gas_used

    @gas_used.setter
    def gas_used(self, gas_used):
        """Sets the gas_used of this TxQueryResult.


        :param gas_used: The gas_used of this TxQueryResult.  # noqa: E501
        :type: str
        """

        self._gas_used = gas_used

    @property
    def tags(self):
        """Gets the tags of this TxQueryResult.  # noqa: E501


        :return: The tags of this TxQueryResult.  # noqa: E501
        :rtype: list[KVPair]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TxQueryResult.


        :param tags: The tags of this TxQueryResult.  # noqa: E501
        :type: list[KVPair]
        """

        self._tags = tags

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
        if issubclass(TxQueryResult, dict):
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
        if not isinstance(other, TxQueryResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
