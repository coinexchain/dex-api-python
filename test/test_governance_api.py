# coding: utf-8

"""
    CET-Lite for CoinEx Chain

    A REST interface for state queries, transaction generation and broadcasting.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.governance_api import GovernanceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestGovernanceApi(unittest.TestCase):
    """GovernanceApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.governance_api.GovernanceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deposit_to_proposal(self):
        """Test case for deposit_to_proposal

        Deposit tokens to a proposal  # noqa: E501
        """
        pass

    def test_get_deposit_by_addr(self):
        """Test case for get_deposit_by_addr

        Query deposit  # noqa: E501
        """
        pass

    def test_get_deposit_parameters(self):
        """Test case for get_deposit_parameters

        Query governance deposit parameters  # noqa: E501
        """
        pass

    def test_get_deposits(self):
        """Test case for get_deposits

        Query deposits  # noqa: E501
        """
        pass

    def test_get_proposal_by_id(self):
        """Test case for get_proposal_by_id

        Query a proposal  # noqa: E501
        """
        pass

    def test_get_proposals(self):
        """Test case for get_proposals

        Query proposals  # noqa: E501
        """
        pass

    def test_get_proposer(self):
        """Test case for get_proposer

        Query proposer  # noqa: E501
        """
        pass

    def test_get_tally(self):
        """Test case for get_tally

        Get a proposal's tally result at the current time  # noqa: E501
        """
        pass

    def test_get_tallying_parameters(self):
        """Test case for get_tallying_parameters

        Query governance tally parameters  # noqa: E501
        """
        pass

    def test_get_voter_by_addr(self):
        """Test case for get_voter_by_addr

        Query vote  # noqa: E501
        """
        pass

    def test_get_voters(self):
        """Test case for get_voters

        Query voters  # noqa: E501
        """
        pass

    def test_get_voting_parameters(self):
        """Test case for get_voting_parameters

        Query governance voting parameters  # noqa: E501
        """
        pass

    def test_submit_community_pool_spend_proposal(self):
        """Test case for submit_community_pool_spend_proposal

        Generate a community pool spend proposal transaction  # noqa: E501
        """
        pass

    def test_submit_parameter_change_proposal(self):
        """Test case for submit_parameter_change_proposal

        Generate a parameter change proposal transaction  # noqa: E501
        """
        pass

    def test_submit_proposal(self):
        """Test case for submit_proposal

        Submit a proposal  # noqa: E501
        """
        pass

    def test_vote_proposal(self):
        """Test case for vote_proposal

        Vote a proposal  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
