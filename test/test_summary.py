# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.summary import Summary

class TestSummary(unittest.TestCase):
    """Summary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Summary:
        """Test Summary
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Summary`
        """
        model = Summary()
        if include_optional:
            return Summary(
                total_sheets = 56,
                yield_percent = 0,
                waste_percent = 1.337,
                waste_area = 1.337,
                unplaced_parts = [
                    ''
                    ],
                sheets_used = [
                    sawvant.models.sheet_usage.SheetUsage(
                        sheet_id = '', 
                        article_number = '', 
                        quantity = 56, 
                        yield_percent = 0, )
                    ]
            )
        else:
            return Summary(
                total_sheets = 56,
                yield_percent = 0,
                waste_percent = 1.337,
                waste_area = 1.337,
                sheets_used = [
                    sawvant.models.sheet_usage.SheetUsage(
                        sheet_id = '', 
                        article_number = '', 
                        quantity = 56, 
                        yield_percent = 0, )
                    ],
        )
        """

    def testSummary(self):
        """Test Summary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
