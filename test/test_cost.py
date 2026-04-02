# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.cost import Cost

class TestCost(unittest.TestCase):
    """Cost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Cost:
        """Test Cost
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Cost`
        """
        model = Cost()
        if include_optional:
            return Cost(
                setup_cost = 1.337,
                cutting_cost = 1.337,
                stacking_cost = 1.337,
                rotation_cost = 1.337,
                cycle_cost = 1.337,
                total_cost = 1.337
            )
        else:
            return Cost(
                setup_cost = 1.337,
                cutting_cost = 1.337,
                stacking_cost = 1.337,
                rotation_cost = 1.337,
                cycle_cost = 1.337,
                total_cost = 1.337,
        )
        """

    def testCost(self):
        """Test Cost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
