# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.measurement_families_get_list200_response_units_unit_code_labels import MeasurementFamiliesGetList200ResponseUnitsUnitCodeLabels

class TestMeasurementFamiliesGetList200ResponseUnitsUnitCodeLabels(unittest.TestCase):
    """MeasurementFamiliesGetList200ResponseUnitsUnitCodeLabels unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MeasurementFamiliesGetList200ResponseUnitsUnitCodeLabels:
        """Test MeasurementFamiliesGetList200ResponseUnitsUnitCodeLabels
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MeasurementFamiliesGetList200ResponseUnitsUnitCodeLabels`
        """
        model = MeasurementFamiliesGetList200ResponseUnitsUnitCodeLabels()
        if include_optional:
            return MeasurementFamiliesGetList200ResponseUnitsUnitCodeLabels(
                locale_code = ''
            )
        else:
            return MeasurementFamiliesGetList200ResponseUnitsUnitCodeLabels(
        )
        """

    def testMeasurementFamiliesGetList200ResponseUnitsUnitCodeLabels(self):
        """Test MeasurementFamiliesGetList200ResponseUnitsUnitCodeLabels"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
