# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.measure_families_get200_response import MeasureFamiliesGet200Response

class TestMeasureFamiliesGet200Response(unittest.TestCase):
    """MeasureFamiliesGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MeasureFamiliesGet200Response:
        """Test MeasureFamiliesGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MeasureFamiliesGet200Response`
        """
        model = MeasureFamiliesGet200Response()
        if include_optional:
            return MeasureFamiliesGet200Response(
                code = '',
                standard = '',
                units = [
                    openapi_client.models.measure_families_all_of__embedded_items_inner_all_of_units_inner.Measure_Families_allOf__embedded_items_inner_allOf_units_inner(
                        code = '', 
                        convert = openapi_client.models.convert.convert(), 
                        symbol = '', )
                    ]
            )
        else:
            return MeasureFamiliesGet200Response(
                code = '',
        )
        """

    def testMeasureFamiliesGet200Response(self):
        """Test MeasureFamiliesGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()