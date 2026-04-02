# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.sheet_usage import SheetUsage

class TestSheetUsage(unittest.TestCase):
    """SheetUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SheetUsage:
        """Test SheetUsage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SheetUsage`
        """
        model = SheetUsage()
        if include_optional:
            return SheetUsage(
                sheet_id = '',
                article_number = '',
                quantity = 56,
                yield_percent = 0
            )
        else:
            return SheetUsage(
                sheet_id = '',
                quantity = 56,
                yield_percent = 0,
        )
        """

    def testSheetUsage(self):
        """Test SheetUsage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
