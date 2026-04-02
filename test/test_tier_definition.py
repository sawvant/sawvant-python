# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.tier_definition import TierDefinition

class TestTierDefinition(unittest.TestCase):
    """TierDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TierDefinition:
        """Test TierDefinition
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TierDefinition`
        """
        model = TierDefinition()
        if include_optional:
            return TierDefinition(
                name = 'pro',
                display_name = 'Pro',
                price_eur_cents = 3900,
                period = 'month',
                rate_limit_fast = 100,
                rate_limit_thorough = 20,
                features = {sse=true, thorough=true, metrics=true, cost=true}
            )
        else:
            return TierDefinition(
                name = 'pro',
                display_name = 'Pro',
                price_eur_cents = 3900,
                rate_limit_fast = 100,
                rate_limit_thorough = 20,
                features = {sse=true, thorough=true, metrics=true, cost=true},
        )
        """

    def testTierDefinition(self):
        """Test TierDefinition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
