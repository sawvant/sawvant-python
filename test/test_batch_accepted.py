# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.batch_accepted import BatchAccepted

class TestBatchAccepted(unittest.TestCase):
    """BatchAccepted unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BatchAccepted:
        """Test BatchAccepted
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BatchAccepted`
        """
        model = BatchAccepted()
        if include_optional:
            return BatchAccepted(
                batch_id = '',
                job_ids = [
                    ''
                    ],
                total = 56,
                created = 56,
                results = [
                    sawvant.models.batch_job_result.BatchJobResult(
                        index = 56, 
                        job_id = '', 
                        error = '', )
                    ]
            )
        else:
            return BatchAccepted(
                batch_id = '',
                job_ids = [
                    ''
                    ],
                total = 56,
                created = 56,
        )
        """

    def testBatchAccepted(self):
        """Test BatchAccepted"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
