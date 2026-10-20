# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.demo_optimize_response import DemoOptimizeResponse

class TestDemoOptimizeResponse(unittest.TestCase):
    """DemoOptimizeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DemoOptimizeResponse:
        """Test DemoOptimizeResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DemoOptimizeResponse`
        """
        model = DemoOptimizeResponse()
        if include_optional:
            return DemoOptimizeResponse(
                layouts = [
                    sawvant.models.demo_layout.DemoLayout(
                        sheet_id = '', 
                        quantity = 56, 
                        placements = [
                            sawvant.models.placement.Placement(
                                part_id = '', 
                                sheet_id = '', 
                                x = 1.337, 
                                y = 1.337, 
                                width = 1.337, 
                                height = 1.337, 
                                rotated = True, 
                                grain = 'none', )
                            ], 
                        svg = '', )
                    ],
                summary = sawvant.models.summary.Summary(
                    total_sheets = 56, 
                    yield_percent = 0, 
                    waste_percent = 1.337, 
                    waste_area = 1.337, 
                    unplaced_parts = [
                        ''
                        ], 
                    sheets_used = [
                        sawvant.models.sheet_usage.SheetUsage(
                            sheet_id = '', 
                            article_number = '', 
                            quantity = 56, 
                            yield_percent = 0, )
                        ], ),
                metrics = sawvant.models.metrics.Metrics(
                    total_cut_length = 1.337, 
                    total_cuts = 56, 
                    total_rotations = 56, 
                    total_stacks = 56, 
                    cut_cycles = 56, )
            )
        else:
            return DemoOptimizeResponse(
                layouts = [
                    sawvant.models.demo_layout.DemoLayout(
                        sheet_id = '', 
                        quantity = 56, 
                        placements = [
                            sawvant.models.placement.Placement(
                                part_id = '', 
                                sheet_id = '', 
                                x = 1.337, 
                                y = 1.337, 
                                width = 1.337, 
                                height = 1.337, 
                                rotated = True, 
                                grain = 'none', )
                            ], 
                        svg = '', )
                    ],
                summary = sawvant.models.summary.Summary(
                    total_sheets = 56, 
                    yield_percent = 0, 
                    waste_percent = 1.337, 
                    waste_area = 1.337, 
                    unplaced_parts = [
                        ''
                        ], 
                    sheets_used = [
                        sawvant.models.sheet_usage.SheetUsage(
                            sheet_id = '', 
                            article_number = '', 
                            quantity = 56, 
                            yield_percent = 0, )
                        ], ),
                metrics = sawvant.models.metrics.Metrics(
                    total_cut_length = 1.337, 
                    total_cuts = 56, 
                    total_rotations = 56, 
                    total_stacks = 56, 
                    cut_cycles = 56, ),
        )
        """

    def testDemoOptimizeResponse(self):
        """Test DemoOptimizeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
