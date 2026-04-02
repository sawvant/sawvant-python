# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.job_response import JobResponse

class TestJobResponse(unittest.TestCase):
    """JobResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobResponse:
        """Test JobResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobResponse`
        """
        model = JobResponse()
        if include_optional:
            return JobResponse(
                job_id = '',
                status = 'pending',
                progress = 0,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                completed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                result = sawvant.models.optimize_result.OptimizeResult(
                    layouts = [
                        sawvant.models.layout.Layout(
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
                                ], )
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
                    cost = sawvant.models.cost.Cost(
                        setup_cost = 1.337, 
                        cutting_cost = 1.337, 
                        stacking_cost = 1.337, 
                        rotation_cost = 1.337, 
                        cycle_cost = 1.337, 
                        total_cost = 1.337, ), ),
                warnings = [
                    ''
                    ],
                error = ''
            )
        else:
            return JobResponse(
                job_id = '',
                status = 'pending',
                progress = 0,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testJobResponse(self):
        """Test JobResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
