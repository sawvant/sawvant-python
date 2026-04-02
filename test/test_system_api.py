# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.api.system_api import SystemApi


class TestSystemApi(unittest.TestCase):
    """SystemApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SystemApi()

    def tearDown(self) -> None:
        pass

    def test_get_health(self) -> None:
        """Test case for get_health

        Health check
        """
        pass

    def test_list_tiers(self) -> None:
        """Test case for list_tiers

        List available subscription tiers
        """
        pass


if __name__ == '__main__':
    unittest.main()
