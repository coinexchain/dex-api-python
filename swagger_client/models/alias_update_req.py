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


class AliasUpdateReq(object):
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
        'alias': 'str',
        'is_add': 'bool',
        'as_default': 'bool'
    }

    attribute_map = {
        'base_req': 'base_req',
        'alias': 'alias',
        'is_add': 'is_add',
        'as_default': 'as_default'
    }

    def __init__(self, base_req=None, alias=None, is_add=None, as_default=None):  # noqa: E501
        """AliasUpdateReq - a model defined in Swagger"""  # noqa: E501

        self._base_req = None
        self._alias = None
        self._is_add = None
        self._as_default = None
        self.discriminator = None

        if base_req is not None:
            self.base_req = base_req
        if alias is not None:
            self.alias = alias
        if is_add is not None:
            self.is_add = is_add
        if as_default is not None:
            self.as_default = as_default

    @property
    def base_req(self):
        """Gets the base_req of this AliasUpdateReq.  # noqa: E501


        :return: The base_req of this AliasUpdateReq.  # noqa: E501
        :rtype: BaseReq
        """
        return self._base_req

    @base_req.setter
    def base_req(self, base_req):
        """Sets the base_req of this AliasUpdateReq.


        :param base_req: The base_req of this AliasUpdateReq.  # noqa: E501
        :type: BaseReq
        """

        self._base_req = base_req

    @property
    def alias(self):
        """Gets the alias of this AliasUpdateReq.  # noqa: E501


        :return: The alias of this AliasUpdateReq.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this AliasUpdateReq.


        :param alias: The alias of this AliasUpdateReq.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def is_add(self):
        """Gets the is_add of this AliasUpdateReq.  # noqa: E501


        :return: The is_add of this AliasUpdateReq.  # noqa: E501
        :rtype: bool
        """
        return self._is_add

    @is_add.setter
    def is_add(self, is_add):
        """Sets the is_add of this AliasUpdateReq.


        :param is_add: The is_add of this AliasUpdateReq.  # noqa: E501
        :type: bool
        """

        self._is_add = is_add

    @property
    def as_default(self):
        """Gets the as_default of this AliasUpdateReq.  # noqa: E501


        :return: The as_default of this AliasUpdateReq.  # noqa: E501
        :rtype: bool
        """
        return self._as_default

    @as_default.setter
    def as_default(self, as_default):
        """Sets the as_default of this AliasUpdateReq.


        :param as_default: The as_default of this AliasUpdateReq.  # noqa: E501
        :type: bool
        """

        self._as_default = as_default

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
        if issubclass(AliasUpdateReq, dict):
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
        if not isinstance(other, AliasUpdateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
