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


class PostTxBody(object):
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
        'amount': 'Coin',
        'unlock_time': 'str',
        'sender': 'str',
        'supervisor': 'str',
        'reward': 'str',
        'operation': 'int'
    }

    attribute_map = {
        'base_req': 'base_req',
        'amount': 'amount',
        'unlock_time': 'unlock_time',
        'sender': 'sender',
        'supervisor': 'supervisor',
        'reward': 'reward',
        'operation': 'operation'
    }

    def __init__(self, base_req=None, amount=None, unlock_time=None, sender=None, supervisor=None, reward=None, operation=None):  # noqa: E501
        """PostTxBody - a model defined in Swagger"""  # noqa: E501

        self._base_req = None
        self._amount = None
        self._unlock_time = None
        self._sender = None
        self._supervisor = None
        self._reward = None
        self._operation = None
        self.discriminator = None

        self.base_req = base_req
        self.amount = amount
        self.unlock_time = unlock_time
        if sender is not None:
            self.sender = sender
        if supervisor is not None:
            self.supervisor = supervisor
        if reward is not None:
            self.reward = reward
        self.operation = operation

    @property
    def base_req(self):
        """Gets the base_req of this PostTxBody.  # noqa: E501


        :return: The base_req of this PostTxBody.  # noqa: E501
        :rtype: BaseReq
        """
        return self._base_req

    @base_req.setter
    def base_req(self, base_req):
        """Sets the base_req of this PostTxBody.


        :param base_req: The base_req of this PostTxBody.  # noqa: E501
        :type: BaseReq
        """
        if base_req is None:
            raise ValueError("Invalid value for `base_req`, must not be `None`")  # noqa: E501

        self._base_req = base_req

    @property
    def amount(self):
        """Gets the amount of this PostTxBody.  # noqa: E501


        :return: The amount of this PostTxBody.  # noqa: E501
        :rtype: Coin
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PostTxBody.


        :param amount: The amount of this PostTxBody.  # noqa: E501
        :type: Coin
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def unlock_time(self):
        """Gets the unlock_time of this PostTxBody.  # noqa: E501


        :return: The unlock_time of this PostTxBody.  # noqa: E501
        :rtype: str
        """
        return self._unlock_time

    @unlock_time.setter
    def unlock_time(self, unlock_time):
        """Sets the unlock_time of this PostTxBody.


        :param unlock_time: The unlock_time of this PostTxBody.  # noqa: E501
        :type: str
        """
        if unlock_time is None:
            raise ValueError("Invalid value for `unlock_time`, must not be `None`")  # noqa: E501

        self._unlock_time = unlock_time

    @property
    def sender(self):
        """Gets the sender of this PostTxBody.  # noqa: E501

        The supervised amount sender's address (required when return or unlock-by-supervisor)  # noqa: E501

        :return: The sender of this PostTxBody.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this PostTxBody.

        The supervised amount sender's address (required when return or unlock-by-supervisor)  # noqa: E501

        :param sender: The sender of this PostTxBody.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def supervisor(self):
        """Gets the supervisor of this PostTxBody.  # noqa: E501

        The supervisor's address (required when create or unlock-by-sender if there is a supervisor)  # noqa: E501

        :return: The supervisor of this PostTxBody.  # noqa: E501
        :rtype: str
        """
        return self._supervisor

    @supervisor.setter
    def supervisor(self, supervisor):
        """Sets the supervisor of this PostTxBody.

        The supervisor's address (required when create or unlock-by-sender if there is a supervisor)  # noqa: E501

        :param supervisor: The supervisor of this PostTxBody.  # noqa: E501
        :type: str
        """

        self._supervisor = supervisor

    @property
    def reward(self):
        """Gets the reward of this PostTxBody.  # noqa: E501


        :return: The reward of this PostTxBody.  # noqa: E501
        :rtype: str
        """
        return self._reward

    @reward.setter
    def reward(self, reward):
        """Sets the reward of this PostTxBody.


        :param reward: The reward of this PostTxBody.  # noqa: E501
        :type: str
        """

        self._reward = reward

    @property
    def operation(self):
        """Gets the operation of this PostTxBody.  # noqa: E501

        Operation type (create: 0; return: 1; unlock-by-sender: 2; unlock-by-supervisor: 3)  # noqa: E501

        :return: The operation of this PostTxBody.  # noqa: E501
        :rtype: int
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this PostTxBody.

        Operation type (create: 0; return: 1; unlock-by-sender: 2; unlock-by-supervisor: 3)  # noqa: E501

        :param operation: The operation of this PostTxBody.  # noqa: E501
        :type: int
        """
        if operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501

        self._operation = operation

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
        if issubclass(PostTxBody, dict):
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
        if not isinstance(other, PostTxBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
