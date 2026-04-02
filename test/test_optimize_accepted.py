# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.optimize_accepted import OptimizeAccepted

class TestOptimizeAccepted(unittest.TestCase):
    """OptimizeAccepted unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OptimizeAccepted:
        """Test OptimizeAccepted
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OptimizeAccepted`
        """
        model = OptimizeAccepted()
        if include_optional:
            return OptimizeAccepted(
                job_id = '',
                status = 'pending',
                poll_url = '/v1/jobs/550e8400-e29b-41d4-a716-446655440000',
                stream_url = '/v1/jobs/550e8400-e29b-41d4-a716-446655440000/stream'
            )
        else:
            return OptimizeAccepted(
                job_id = '',
                status = 'pending',
                poll_url = '/v1/jobs/550e8400-e29b-41d4-a716-446655440000',
                stream_url = '/v1/jobs/550e8400-e29b-41d4-a716-446655440000/stream',
        )
        """

    def testOptimizeAccepted(self):
        """Test OptimizeAccepted"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
