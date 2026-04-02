# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.optimize_request import OptimizeRequest

class TestOptimizeRequest(unittest.TestCase):
    """OptimizeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OptimizeRequest:
        """Test OptimizeRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OptimizeRequest`
        """
        model = OptimizeRequest()
        if include_optional:
            return OptimizeRequest(
                parts = [
                    sawvant.models.part.Part(
                        id = '', 
                        length = 1.337, 
                        width = 1.337, 
                        quantity = 1, 
                        grain = 'none', 
                        edge_banding = sawvant.models.edge_correction.EdgeCorrection(
                            top = 1.337, 
                            bottom = 1.337, 
                            left = 1.337, 
                            right = 1.337, ), )
                    ],
                sheets = [
                    sawvant.models.sheet.Sheet(
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
                        article_number = '', )
                    ],
                machine = sawvant.models.machine.Machine(
                    blade_thickness = 1.337, 
                    max_levels = 1, 
                    max_stack_height = 1.337, 
                    cut_direction = 'default', ),
                strategy = 'fast',
                cost_tariffs = sawvant.models.cost_tariffs.CostTariffs(
                    setup_cost = 1.337, 
                    cost_per_meter = 1.337, 
                    cost_per_rotation = 1.337, 
                    cost_per_stack = 1.337, 
                    cost_per_cycle = 1.337, )
            )
        else:
            return OptimizeRequest(
                parts = [
                    sawvant.models.part.Part(
                        id = '', 
                        length = 1.337, 
                        width = 1.337, 
                        quantity = 1, 
                        grain = 'none', 
                        edge_banding = sawvant.models.edge_correction.EdgeCorrection(
                            top = 1.337, 
                            bottom = 1.337, 
                            left = 1.337, 
                            right = 1.337, ), )
                    ],
                sheets = [
                    sawvant.models.sheet.Sheet(
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
                        article_number = '', )
                    ],
                machine = sawvant.models.machine.Machine(
                    blade_thickness = 1.337, 
                    max_levels = 1, 
                    max_stack_height = 1.337, 
                    cut_direction = 'default', ),
        )
        """

    def testOptimizeRequest(self):
        """Test OptimizeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
