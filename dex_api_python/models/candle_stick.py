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


class CandleStick(object):
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
        'open': 'str',
        'close': 'str',
        'high': 'str',
        'low': 'str',
        'total': 'str',
        'unix_time': 'int',
        'time_span': 'int',
        'market': 'str'
    }

    attribute_map = {
        'open': 'open',
        'close': 'close',
        'high': 'high',
        'low': 'low',
        'total': 'total',
        'unix_time': 'unix_time',
        'time_span': 'time_span',
        'market': 'market'
    }

    def __init__(self, open=None, close=None, high=None, low=None, total=None, unix_time=None, time_span=None, market=None):  # noqa: E501
        """CandleStick - a model defined in Swagger"""  # noqa: E501

        self._open = None
        self._close = None
        self._high = None
        self._low = None
        self._total = None
        self._unix_time = None
        self._time_span = None
        self._market = None
        self.discriminator = None

        if open is not None:
            self.open = open
        if close is not None:
            self.close = close
        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        if total is not None:
            self.total = total
        if unix_time is not None:
            self.unix_time = unix_time
        if time_span is not None:
            self.time_span = time_span
        if market is not None:
            self.market = market

    @property
    def open(self):
        """Gets the open of this CandleStick.  # noqa: E501

        open price  # noqa: E501

        :return: The open of this CandleStick.  # noqa: E501
        :rtype: str
        """
        return self._open

    @open.setter
    def open(self, open):
        """Sets the open of this CandleStick.

        open price  # noqa: E501

        :param open: The open of this CandleStick.  # noqa: E501
        :type: str
        """

        self._open = open

    @property
    def close(self):
        """Gets the close of this CandleStick.  # noqa: E501

        close price  # noqa: E501

        :return: The close of this CandleStick.  # noqa: E501
        :rtype: str
        """
        return self._close

    @close.setter
    def close(self, close):
        """Sets the close of this CandleStick.

        close price  # noqa: E501

        :param close: The close of this CandleStick.  # noqa: E501
        :type: str
        """

        self._close = close

    @property
    def high(self):
        """Gets the high of this CandleStick.  # noqa: E501

        high price  # noqa: E501

        :return: The high of this CandleStick.  # noqa: E501
        :rtype: str
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this CandleStick.

        high price  # noqa: E501

        :param high: The high of this CandleStick.  # noqa: E501
        :type: str
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this CandleStick.  # noqa: E501

        low price  # noqa: E501

        :return: The low of this CandleStick.  # noqa: E501
        :rtype: str
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this CandleStick.

        low price  # noqa: E501

        :param low: The low of this CandleStick.  # noqa: E501
        :type: str
        """

        self._low = low

    @property
    def total(self):
        """Gets the total of this CandleStick.  # noqa: E501

        total deal  # noqa: E501

        :return: The total of this CandleStick.  # noqa: E501
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CandleStick.

        total deal  # noqa: E501

        :param total: The total of this CandleStick.  # noqa: E501
        :type: str
        """

        self._total = total

    @property
    def unix_time(self):
        """Gets the unix_time of this CandleStick.  # noqa: E501

        ending unix time  # noqa: E501

        :return: The unix_time of this CandleStick.  # noqa: E501
        :rtype: int
        """
        return self._unix_time

    @unix_time.setter
    def unix_time(self, unix_time):
        """Sets the unix_time of this CandleStick.

        ending unix time  # noqa: E501

        :param unix_time: The unix_time of this CandleStick.  # noqa: E501
        :type: int
        """

        self._unix_time = unix_time

    @property
    def time_span(self):
        """Gets the time_span of this CandleStick.  # noqa: E501

        Minute:16/Hour:32/Day:48  # noqa: E501

        :return: The time_span of this CandleStick.  # noqa: E501
        :rtype: int
        """
        return self._time_span

    @time_span.setter
    def time_span(self, time_span):
        """Sets the time_span of this CandleStick.

        Minute:16/Hour:32/Day:48  # noqa: E501

        :param time_span: The time_span of this CandleStick.  # noqa: E501
        :type: int
        """

        self._time_span = time_span

    @property
    def market(self):
        """Gets the market of this CandleStick.  # noqa: E501


        :return: The market of this CandleStick.  # noqa: E501
        :rtype: str
        """
        return self._market

    @market.setter
    def market(self, market):
        """Sets the market of this CandleStick.


        :param market: The market of this CandleStick.  # noqa: E501
        :type: str
        """

        self._market = market

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
        if issubclass(CandleStick, dict):
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
        if not isinstance(other, CandleStick):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
