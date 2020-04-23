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


class InlineResponse2004Result(object):
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
        'address': 'str',
        'coins': 'list[Coin]',
        'locked_coins': 'list[LockedCoin]',
        'frozen_coins': 'list[Coin]',
        'public_key': 'PublicKey',
        'account_number': 'str',
        'sequence': 'str',
        'memo_required': 'bool',
        'referee': 'str',
        'referee_change_time': 'str'
    }

    attribute_map = {
        'address': 'address',
        'coins': 'coins',
        'locked_coins': 'locked_coins',
        'frozen_coins': 'frozen_coins',
        'public_key': 'public_key',
        'account_number': 'account_number',
        'sequence': 'sequence',
        'memo_required': 'memo_required',
        'referee': 'referee',
        'referee_change_time': 'referee_change_time'
    }

    def __init__(self, address=None, coins=None, locked_coins=None, frozen_coins=None, public_key=None, account_number=None, sequence=None, memo_required=None, referee=None, referee_change_time=None):  # noqa: E501
        """InlineResponse2004Result - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._coins = None
        self._locked_coins = None
        self._frozen_coins = None
        self._public_key = None
        self._account_number = None
        self._sequence = None
        self._memo_required = None
        self._referee = None
        self._referee_change_time = None
        self.discriminator = None

        self.address = address
        self.coins = coins
        self.locked_coins = locked_coins
        self.frozen_coins = frozen_coins
        self.public_key = public_key
        self.account_number = account_number
        self.sequence = sequence
        self.memo_required = memo_required
        self.referee = referee
        self.referee_change_time = referee_change_time

    @property
    def address(self):
        """Gets the address of this InlineResponse2004Result.  # noqa: E501


        :return: The address of this InlineResponse2004Result.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this InlineResponse2004Result.


        :param address: The address of this InlineResponse2004Result.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def coins(self):
        """Gets the coins of this InlineResponse2004Result.  # noqa: E501


        :return: The coins of this InlineResponse2004Result.  # noqa: E501
        :rtype: list[Coin]
        """
        return self._coins

    @coins.setter
    def coins(self, coins):
        """Sets the coins of this InlineResponse2004Result.


        :param coins: The coins of this InlineResponse2004Result.  # noqa: E501
        :type: list[Coin]
        """
        if coins is None:
            raise ValueError("Invalid value for `coins`, must not be `None`")  # noqa: E501

        self._coins = coins

    @property
    def locked_coins(self):
        """Gets the locked_coins of this InlineResponse2004Result.  # noqa: E501


        :return: The locked_coins of this InlineResponse2004Result.  # noqa: E501
        :rtype: list[LockedCoin]
        """
        return self._locked_coins

    @locked_coins.setter
    def locked_coins(self, locked_coins):
        """Sets the locked_coins of this InlineResponse2004Result.


        :param locked_coins: The locked_coins of this InlineResponse2004Result.  # noqa: E501
        :type: list[LockedCoin]
        """
        if locked_coins is None:
            raise ValueError("Invalid value for `locked_coins`, must not be `None`")  # noqa: E501

        self._locked_coins = locked_coins

    @property
    def frozen_coins(self):
        """Gets the frozen_coins of this InlineResponse2004Result.  # noqa: E501


        :return: The frozen_coins of this InlineResponse2004Result.  # noqa: E501
        :rtype: list[Coin]
        """
        return self._frozen_coins

    @frozen_coins.setter
    def frozen_coins(self, frozen_coins):
        """Sets the frozen_coins of this InlineResponse2004Result.


        :param frozen_coins: The frozen_coins of this InlineResponse2004Result.  # noqa: E501
        :type: list[Coin]
        """
        if frozen_coins is None:
            raise ValueError("Invalid value for `frozen_coins`, must not be `None`")  # noqa: E501

        self._frozen_coins = frozen_coins

    @property
    def public_key(self):
        """Gets the public_key of this InlineResponse2004Result.  # noqa: E501


        :return: The public_key of this InlineResponse2004Result.  # noqa: E501
        :rtype: PublicKey
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this InlineResponse2004Result.


        :param public_key: The public_key of this InlineResponse2004Result.  # noqa: E501
        :type: PublicKey
        """
        if public_key is None:
            raise ValueError("Invalid value for `public_key`, must not be `None`")  # noqa: E501

        self._public_key = public_key

    @property
    def account_number(self):
        """Gets the account_number of this InlineResponse2004Result.  # noqa: E501


        :return: The account_number of this InlineResponse2004Result.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this InlineResponse2004Result.


        :param account_number: The account_number of this InlineResponse2004Result.  # noqa: E501
        :type: str
        """
        if account_number is None:
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501

        self._account_number = account_number

    @property
    def sequence(self):
        """Gets the sequence of this InlineResponse2004Result.  # noqa: E501


        :return: The sequence of this InlineResponse2004Result.  # noqa: E501
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this InlineResponse2004Result.


        :param sequence: The sequence of this InlineResponse2004Result.  # noqa: E501
        :type: str
        """
        if sequence is None:
            raise ValueError("Invalid value for `sequence`, must not be `None`")  # noqa: E501

        self._sequence = sequence

    @property
    def memo_required(self):
        """Gets the memo_required of this InlineResponse2004Result.  # noqa: E501


        :return: The memo_required of this InlineResponse2004Result.  # noqa: E501
        :rtype: bool
        """
        return self._memo_required

    @memo_required.setter
    def memo_required(self, memo_required):
        """Sets the memo_required of this InlineResponse2004Result.


        :param memo_required: The memo_required of this InlineResponse2004Result.  # noqa: E501
        :type: bool
        """
        if memo_required is None:
            raise ValueError("Invalid value for `memo_required`, must not be `None`")  # noqa: E501

        self._memo_required = memo_required

    @property
    def referee(self):
        """Gets the referee of this InlineResponse2004Result.  # noqa: E501


        :return: The referee of this InlineResponse2004Result.  # noqa: E501
        :rtype: str
        """
        return self._referee

    @referee.setter
    def referee(self, referee):
        """Sets the referee of this InlineResponse2004Result.


        :param referee: The referee of this InlineResponse2004Result.  # noqa: E501
        :type: str
        """
        if referee is None:
            raise ValueError("Invalid value for `referee`, must not be `None`")  # noqa: E501

        self._referee = referee

    @property
    def referee_change_time(self):
        """Gets the referee_change_time of this InlineResponse2004Result.  # noqa: E501


        :return: The referee_change_time of this InlineResponse2004Result.  # noqa: E501
        :rtype: str
        """
        return self._referee_change_time

    @referee_change_time.setter
    def referee_change_time(self, referee_change_time):
        """Sets the referee_change_time of this InlineResponse2004Result.


        :param referee_change_time: The referee_change_time of this InlineResponse2004Result.  # noqa: E501
        :type: str
        """
        if referee_change_time is None:
            raise ValueError("Invalid value for `referee_change_time`, must not be `None`")  # noqa: E501

        self._referee_change_time = referee_change_time

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
        if issubclass(InlineResponse2004Result, dict):
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
        if not isinstance(other, InlineResponse2004Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
