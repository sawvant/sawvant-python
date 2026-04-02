# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.sheet import Sheet

class TestSheet(unittest.TestCase):
    """Sheet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Sheet:
        """Test Sheet
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Sheet`
        """
        model = Sheet()
        if include_optional:
            return Sheet(
                id = '',
                length = 1.337,
                width = 1.337,
                quantity = 0,
                grain = 'none',
                is_offcut = True,
                trim_margins = sawvant.models.margins.Margins(
                    top = 1.337, 
                    bottom = 1.337, 
                    left = 1.337, 
                    right = 1.337, ),
                article_number = ''
            )
        else:
            return Sheet(
                id = '',
                length = 1.337,
                width = 1.337,
                quantity = 0,
                grain = 'none',
        )
        """

    def testSheet(self):
        """Test Sheet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
