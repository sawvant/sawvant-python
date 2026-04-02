# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.placement import Placement

class TestPlacement(unittest.TestCase):
    """Placement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Placement:
        """Test Placement
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Placement`
        """
        model = Placement()
        if include_optional:
            return Placement(
                part_id = '',
                sheet_id = '',
                x = 1.337,
                y = 1.337,
                width = 1.337,
                height = 1.337,
                rotated = True,
                grain = 'none'
            )
        else:
            return Placement(
                part_id = '',
                sheet_id = '',
                x = 1.337,
                y = 1.337,
                width = 1.337,
                height = 1.337,
                rotated = True,
                grain = 'none',
        )
        """

    def testPlacement(self):
        """Test Placement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
