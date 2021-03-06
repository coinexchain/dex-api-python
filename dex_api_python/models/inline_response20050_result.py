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


class InlineResponse20050Result(object):
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
        'fee_for_alias_length_2': 'str',
        'fee_for_alias_length_3': 'str',
        'fee_for_alias_length_4': 'str',
        'fee_for_alias_length_5': 'str',
        'fee_for_alias_length_6': 'str',
        'fee_for_alias_length_7_or_higher': 'str',
        'max_alias_count': 'str'
    }

    attribute_map = {
        'fee_for_alias_length_2': 'fee_for_alias_length_2',
        'fee_for_alias_length_3': 'fee_for_alias_length_3',
        'fee_for_alias_length_4': 'fee_for_alias_length_4',
        'fee_for_alias_length_5': 'fee_for_alias_length_5',
        'fee_for_alias_length_6': 'fee_for_alias_length_6',
        'fee_for_alias_length_7_or_higher': 'fee_for_alias_length_7_or_higher',
        'max_alias_count': 'max_alias_count'
    }

    def __init__(self, fee_for_alias_length_2=None, fee_for_alias_length_3=None, fee_for_alias_length_4=None, fee_for_alias_length_5=None, fee_for_alias_length_6=None, fee_for_alias_length_7_or_higher=None, max_alias_count=None):  # noqa: E501
        """InlineResponse20050Result - a model defined in Swagger"""  # noqa: E501

        self._fee_for_alias_length_2 = None
        self._fee_for_alias_length_3 = None
        self._fee_for_alias_length_4 = None
        self._fee_for_alias_length_5 = None
        self._fee_for_alias_length_6 = None
        self._fee_for_alias_length_7_or_higher = None
        self._max_alias_count = None
        self.discriminator = None

        if fee_for_alias_length_2 is not None:
            self.fee_for_alias_length_2 = fee_for_alias_length_2
        if fee_for_alias_length_3 is not None:
            self.fee_for_alias_length_3 = fee_for_alias_length_3
        if fee_for_alias_length_4 is not None:
            self.fee_for_alias_length_4 = fee_for_alias_length_4
        if fee_for_alias_length_5 is not None:
            self.fee_for_alias_length_5 = fee_for_alias_length_5
        if fee_for_alias_length_6 is not None:
            self.fee_for_alias_length_6 = fee_for_alias_length_6
        if fee_for_alias_length_7_or_higher is not None:
            self.fee_for_alias_length_7_or_higher = fee_for_alias_length_7_or_higher
        if max_alias_count is not None:
            self.max_alias_count = max_alias_count

    @property
    def fee_for_alias_length_2(self):
        """Gets the fee_for_alias_length_2 of this InlineResponse20050Result.  # noqa: E501


        :return: The fee_for_alias_length_2 of this InlineResponse20050Result.  # noqa: E501
        :rtype: str
        """
        return self._fee_for_alias_length_2

    @fee_for_alias_length_2.setter
    def fee_for_alias_length_2(self, fee_for_alias_length_2):
        """Sets the fee_for_alias_length_2 of this InlineResponse20050Result.


        :param fee_for_alias_length_2: The fee_for_alias_length_2 of this InlineResponse20050Result.  # noqa: E501
        :type: str
        """

        self._fee_for_alias_length_2 = fee_for_alias_length_2

    @property
    def fee_for_alias_length_3(self):
        """Gets the fee_for_alias_length_3 of this InlineResponse20050Result.  # noqa: E501


        :return: The fee_for_alias_length_3 of this InlineResponse20050Result.  # noqa: E501
        :rtype: str
        """
        return self._fee_for_alias_length_3

    @fee_for_alias_length_3.setter
    def fee_for_alias_length_3(self, fee_for_alias_length_3):
        """Sets the fee_for_alias_length_3 of this InlineResponse20050Result.


        :param fee_for_alias_length_3: The fee_for_alias_length_3 of this InlineResponse20050Result.  # noqa: E501
        :type: str
        """

        self._fee_for_alias_length_3 = fee_for_alias_length_3

    @property
    def fee_for_alias_length_4(self):
        """Gets the fee_for_alias_length_4 of this InlineResponse20050Result.  # noqa: E501


        :return: The fee_for_alias_length_4 of this InlineResponse20050Result.  # noqa: E501
        :rtype: str
        """
        return self._fee_for_alias_length_4

    @fee_for_alias_length_4.setter
    def fee_for_alias_length_4(self, fee_for_alias_length_4):
        """Sets the fee_for_alias_length_4 of this InlineResponse20050Result.


        :param fee_for_alias_length_4: The fee_for_alias_length_4 of this InlineResponse20050Result.  # noqa: E501
        :type: str
        """

        self._fee_for_alias_length_4 = fee_for_alias_length_4

    @property
    def fee_for_alias_length_5(self):
        """Gets the fee_for_alias_length_5 of this InlineResponse20050Result.  # noqa: E501


        :return: The fee_for_alias_length_5 of this InlineResponse20050Result.  # noqa: E501
        :rtype: str
        """
        return self._fee_for_alias_length_5

    @fee_for_alias_length_5.setter
    def fee_for_alias_length_5(self, fee_for_alias_length_5):
        """Sets the fee_for_alias_length_5 of this InlineResponse20050Result.


        :param fee_for_alias_length_5: The fee_for_alias_length_5 of this InlineResponse20050Result.  # noqa: E501
        :type: str
        """

        self._fee_for_alias_length_5 = fee_for_alias_length_5

    @property
    def fee_for_alias_length_6(self):
        """Gets the fee_for_alias_length_6 of this InlineResponse20050Result.  # noqa: E501


        :return: The fee_for_alias_length_6 of this InlineResponse20050Result.  # noqa: E501
        :rtype: str
        """
        return self._fee_for_alias_length_6

    @fee_for_alias_length_6.setter
    def fee_for_alias_length_6(self, fee_for_alias_length_6):
        """Sets the fee_for_alias_length_6 of this InlineResponse20050Result.


        :param fee_for_alias_length_6: The fee_for_alias_length_6 of this InlineResponse20050Result.  # noqa: E501
        :type: str
        """

        self._fee_for_alias_length_6 = fee_for_alias_length_6

    @property
    def fee_for_alias_length_7_or_higher(self):
        """Gets the fee_for_alias_length_7_or_higher of this InlineResponse20050Result.  # noqa: E501


        :return: The fee_for_alias_length_7_or_higher of this InlineResponse20050Result.  # noqa: E501
        :rtype: str
        """
        return self._fee_for_alias_length_7_or_higher

    @fee_for_alias_length_7_or_higher.setter
    def fee_for_alias_length_7_or_higher(self, fee_for_alias_length_7_or_higher):
        """Sets the fee_for_alias_length_7_or_higher of this InlineResponse20050Result.


        :param fee_for_alias_length_7_or_higher: The fee_for_alias_length_7_or_higher of this InlineResponse20050Result.  # noqa: E501
        :type: str
        """

        self._fee_for_alias_length_7_or_higher = fee_for_alias_length_7_or_higher

    @property
    def max_alias_count(self):
        """Gets the max_alias_count of this InlineResponse20050Result.  # noqa: E501


        :return: The max_alias_count of this InlineResponse20050Result.  # noqa: E501
        :rtype: str
        """
        return self._max_alias_count

    @max_alias_count.setter
    def max_alias_count(self, max_alias_count):
        """Sets the max_alias_count of this InlineResponse20050Result.


        :param max_alias_count: The max_alias_count of this InlineResponse20050Result.  # noqa: E501
        :type: str
        """

        self._max_alias_count = max_alias_count

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
        if issubclass(InlineResponse20050Result, dict):
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
        if not isinstance(other, InlineResponse20050Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
