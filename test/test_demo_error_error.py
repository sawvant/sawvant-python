# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.demo_error_error import DemoErrorError

class TestDemoErrorError(unittest.TestCase):
    """DemoErrorError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DemoErrorError:
        """Test DemoErrorError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DemoErrorError`
        """
        model = DemoErrorError()
        if include_optional:
            return DemoErrorError(
                code = 'DEMO_LIMIT_EXCEEDED',
                message = 'too many part types: the demo allows at most 30, got 42'
            )
        else:
            return DemoErrorError(
                code = 'DEMO_LIMIT_EXCEEDED',
                message = 'too many part types: the demo allows at most 30, got 42',
        )
        """

    def testDemoErrorError(self):
        """Test DemoErrorError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
