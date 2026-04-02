# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.rate_limit_error import RateLimitError

class TestRateLimitError(unittest.TestCase):
    """RateLimitError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RateLimitError:
        """Test RateLimitError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RateLimitError`
        """
        model = RateLimitError()
        if include_optional:
            return RateLimitError(
                error = 'rate limit exceeded',
                limit = 56,
                remaining = 56,
                strategy = 'fast'
            )
        else:
            return RateLimitError(
                error = 'rate limit exceeded',
                limit = 56,
                remaining = 56,
                strategy = 'fast',
        )
        """

    def testRateLimitError(self):
        """Test RateLimitError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
