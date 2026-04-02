# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.edge_correction import EdgeCorrection

class TestEdgeCorrection(unittest.TestCase):
    """EdgeCorrection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EdgeCorrection:
        """Test EdgeCorrection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EdgeCorrection`
        """
        model = EdgeCorrection()
        if include_optional:
            return EdgeCorrection(
                top = 1.337,
                bottom = 1.337,
                left = 1.337,
                right = 1.337
            )
        else:
            return EdgeCorrection(
        )
        """

    def testEdgeCorrection(self):
        """Test EdgeCorrection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
