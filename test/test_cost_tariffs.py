# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.cost_tariffs import CostTariffs

class TestCostTariffs(unittest.TestCase):
    """CostTariffs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CostTariffs:
        """Test CostTariffs
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CostTariffs`
        """
        model = CostTariffs()
        if include_optional:
            return CostTariffs(
                setup_cost = 1.337,
                cost_per_meter = 1.337,
                cost_per_rotation = 1.337,
                cost_per_stack = 1.337,
                cost_per_cycle = 1.337
            )
        else:
            return CostTariffs(
        )
        """

    def testCostTariffs(self):
        """Test CostTariffs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
