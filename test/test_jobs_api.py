# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.api.jobs_api import JobsApi


class TestJobsApi(unittest.TestCase):
    """JobsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = JobsApi()

    def tearDown(self) -> None:
        pass

    def test_get_job(self) -> None:
        """Test case for get_job

        Get job status
        """
        pass

    def test_get_job_diagram_pdf(self) -> None:
        """Test case for get_job_diagram_pdf

        Render a cutting plan as PDF
        """
        pass

    def test_get_job_diagram_svg(self) -> None:
        """Test case for get_job_diagram_svg

        Render a cutting plan as SVG
        """
        pass

    def test_stream_job(self) -> None:
        """Test case for stream_job

        Stream job progress via SSE
        """
        pass


if __name__ == '__main__':
    unittest.main()
