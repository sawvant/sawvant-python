# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.machine import Machine

class TestMachine(unittest.TestCase):
    """Machine unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Machine:
        """Test Machine
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Machine`
        """
        model = Machine()
        if include_optional:
            return Machine(
                blade_thickness = 1.337,
                max_levels = 1,
                max_stack_height = 1.337,
                cut_direction = 'default'
            )
        else:
            return Machine(
                blade_thickness = 1.337,
                max_levels = 1,
                cut_direction = 'default',
        )
        """

    def testMachine(self):
        """Test Machine"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
