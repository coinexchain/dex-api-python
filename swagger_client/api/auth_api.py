# coding: utf-8

"""
    CET-Lite for CoinEx Chain

    A REST interface for state queries, transaction generation and broadcasting.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AuthApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_account(self, address, **kwargs):  # noqa: E501
        """Get the account information on blockchain  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Account address (required)
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_account_with_http_info(address, **kwargs)  # noqa: E501
        else:
            (data) = self.get_account_with_http_info(address, **kwargs)  # noqa: E501
            return data

    def get_account_with_http_info(self, address, **kwargs):  # noqa: E501
        """Get the account information on blockchain  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_account_with_http_info(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Account address (required)
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `get_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address' in params:
            path_params['address'] = params['address']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/accounts/{address}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_auth_params(self, **kwargs):  # noqa: E501
        """Get the current auth parameters  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_auth_params(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20034
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_auth_params_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_auth_params_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_auth_params_with_http_info(self, **kwargs):  # noqa: E501
        """Get the current auth parameters  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_auth_params_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20034
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_auth_params" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/parameters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20034',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_referee(self, address, referee, **kwargs):  # noqa: E501
        """Set referee for account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_referee(address, referee, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Account address in bech32 format (required)
        :param Referee referee: Referee (required)
        :return: StdTx
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_referee_with_http_info(address, referee, **kwargs)  # noqa: E501
        else:
            (data) = self.set_referee_with_http_info(address, referee, **kwargs)  # noqa: E501
            return data

    def set_referee_with_http_info(self, address, referee, **kwargs):  # noqa: E501
        """Set referee for account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_referee_with_http_info(address, referee, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Account address in bech32 format (required)
        :param Referee referee: Referee (required)
        :return: StdTx
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address', 'referee']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_referee" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `set_referee`")  # noqa: E501
        # verify the required parameter 'referee' is set
        if ('referee' not in params or
                params['referee'] is None):
            raise ValueError("Missing the required parameter `referee` when calling `set_referee`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address' in params:
            path_params['address'] = params['address']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'referee' in params:
            body_params = params['referee']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/accounts/{address}/referee', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StdTx',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
