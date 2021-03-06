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


class CommentRef(object):
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
        'id': 'str',
        'reward_target': 'str',
        'reward_token': 'str',
        'reward_amount': 'str',
        'attitudes': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'reward_target': 'reward_target',
        'reward_token': 'reward_token',
        'reward_amount': 'reward_amount',
        'attitudes': 'attitudes'
    }

    def __init__(self, id=None, reward_target=None, reward_token=None, reward_amount=None, attitudes=None):  # noqa: E501
        """CommentRef - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._reward_target = None
        self._reward_token = None
        self._reward_amount = None
        self._attitudes = None
        self.discriminator = None

        self.id = id
        self.reward_target = reward_target
        self.reward_token = reward_token
        self.reward_amount = reward_amount
        self.attitudes = attitudes

    @property
    def id(self):
        """Gets the id of this CommentRef.  # noqa: E501


        :return: The id of this CommentRef.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CommentRef.


        :param id: The id of this CommentRef.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def reward_target(self):
        """Gets the reward_target of this CommentRef.  # noqa: E501


        :return: The reward_target of this CommentRef.  # noqa: E501
        :rtype: str
        """
        return self._reward_target

    @reward_target.setter
    def reward_target(self, reward_target):
        """Sets the reward_target of this CommentRef.


        :param reward_target: The reward_target of this CommentRef.  # noqa: E501
        :type: str
        """
        if reward_target is None:
            raise ValueError("Invalid value for `reward_target`, must not be `None`")  # noqa: E501

        self._reward_target = reward_target

    @property
    def reward_token(self):
        """Gets the reward_token of this CommentRef.  # noqa: E501


        :return: The reward_token of this CommentRef.  # noqa: E501
        :rtype: str
        """
        return self._reward_token

    @reward_token.setter
    def reward_token(self, reward_token):
        """Sets the reward_token of this CommentRef.


        :param reward_token: The reward_token of this CommentRef.  # noqa: E501
        :type: str
        """
        if reward_token is None:
            raise ValueError("Invalid value for `reward_token`, must not be `None`")  # noqa: E501

        self._reward_token = reward_token

    @property
    def reward_amount(self):
        """Gets the reward_amount of this CommentRef.  # noqa: E501


        :return: The reward_amount of this CommentRef.  # noqa: E501
        :rtype: str
        """
        return self._reward_amount

    @reward_amount.setter
    def reward_amount(self, reward_amount):
        """Sets the reward_amount of this CommentRef.


        :param reward_amount: The reward_amount of this CommentRef.  # noqa: E501
        :type: str
        """
        if reward_amount is None:
            raise ValueError("Invalid value for `reward_amount`, must not be `None`")  # noqa: E501

        self._reward_amount = reward_amount

    @property
    def attitudes(self):
        """Gets the attitudes of this CommentRef.  # noqa: E501


        :return: The attitudes of this CommentRef.  # noqa: E501
        :rtype: list[int]
        """
        return self._attitudes

    @attitudes.setter
    def attitudes(self, attitudes):
        """Sets the attitudes of this CommentRef.


        :param attitudes: The attitudes of this CommentRef.  # noqa: E501
        :type: list[int]
        """
        if attitudes is None:
            raise ValueError("Invalid value for `attitudes`, must not be `None`")  # noqa: E501

        self._attitudes = attitudes

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
        if issubclass(CommentRef, dict):
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
        if not isinstance(other, CommentRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
