# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.demo_error import DemoError

class TestDemoError(unittest.TestCase):
    """DemoError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DemoError:
        """Test DemoError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DemoError`
        """
        model = DemoError()
        if include_optional:
            return DemoError(
                error = sawvant.models.demo_error_error.DemoError_error(
                    code = 'DEMO_LIMIT_EXCEEDED', 
                    message = 'too many part types: the demo allows at most 30, got 42', )
            )
        else:
            return DemoError(
                error = sawvant.models.demo_error_error.DemoError_error(
                    code = 'DEMO_LIMIT_EXCEEDED', 
                    message = 'too many part types: the demo allows at most 30, got 42', ),
        )
        """

    def testDemoError(self):
        """Test DemoError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
