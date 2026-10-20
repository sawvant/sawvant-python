# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


import unittest

from sawvant.models.api_error import ApiError

class TestApiError(unittest.TestCase):
    """ApiError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiError:
        """Test ApiError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiError`
        """
        model = ApiError()
        if include_optional:
            return ApiError(
                error = sawvant.models.api_error_body.ApiErrorBody(
                    code = 'INVALID_BODY', 
                    message = '', 
                    details = [
                        sawvant.models.field_error.FieldError(
                            field = 'parts[2].width', 
                            reason = 'must be greater than zero', )
                        ], )
            )
        else:
            return ApiError(
                error = sawvant.models.api_error_body.ApiErrorBody(
                    code = 'INVALID_BODY', 
                    message = '', 
                    details = [
                        sawvant.models.field_error.FieldError(
                            field = 'parts[2].width', 
                            reason = 'must be greater than zero', )
                        ], ),
        )
        """

    def testApiError(self):
        """Test ApiError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
