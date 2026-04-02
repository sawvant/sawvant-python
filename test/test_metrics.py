# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.metrics import Metrics

class TestMetrics(unittest.TestCase):
    """Metrics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Metrics:
        """Test Metrics
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Metrics`
        """
        model = Metrics()
        if include_optional:
            return Metrics(
                total_cut_length = 1.337,
                total_cuts = 56,
                total_rotations = 56,
                total_stacks = 56,
                cut_cycles = 56
            )
        else:
            return Metrics(
                total_cut_length = 1.337,
                total_cuts = 56,
                total_rotations = 56,
                total_stacks = 56,
                cut_cycles = 56,
        )
        """

    def testMetrics(self):
        """Test Metrics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
