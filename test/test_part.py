# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.part import Part

class TestPart(unittest.TestCase):
    """Part unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Part:
        """Test Part
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Part`
        """
        model = Part()
        if include_optional:
            return Part(
                id = '',
                length = 1.337,
                width = 1.337,
                quantity = 1,
                grain = 'none',
                edge_banding = sawvant.models.edge_correction.EdgeCorrection(
                    top = 1.337, 
                    bottom = 1.337, 
                    left = 1.337, 
                    right = 1.337, )
            )
        else:
            return Part(
                id = '',
                length = 1.337,
                width = 1.337,
                quantity = 1,
                grain = 'none',
        )
        """

    def testPart(self):
        """Test Part"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
