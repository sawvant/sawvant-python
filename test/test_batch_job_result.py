# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.batch_job_result import BatchJobResult

class TestBatchJobResult(unittest.TestCase):
    """BatchJobResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BatchJobResult:
        """Test BatchJobResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BatchJobResult`
        """
        model = BatchJobResult()
        if include_optional:
            return BatchJobResult(
                index = 56,
                job_id = '',
                error = ''
            )
        else:
            return BatchJobResult(
                index = 56,
        )
        """

    def testBatchJobResult(self):
        """Test BatchJobResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
