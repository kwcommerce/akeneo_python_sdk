# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.measure_family_list_all_of_units import MeasureFamilyListAllOfUnits

class TestMeasureFamilyListAllOfUnits(unittest.TestCase):
    """MeasureFamilyListAllOfUnits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MeasureFamilyListAllOfUnits:
        """Test MeasureFamilyListAllOfUnits
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MeasureFamilyListAllOfUnits`
        """
        model = MeasureFamilyListAllOfUnits()
        if include_optional:
            return MeasureFamilyListAllOfUnits(
                code = '',
                convert = openapi_client.models.measure_family_list_all_of_convert.MeasureFamilyList_allOf_convert(),
                symbol = ''
            )
        else:
            return MeasureFamilyListAllOfUnits(
        )
        """

    def testMeasureFamilyListAllOfUnits(self):
        """Test MeasureFamilyListAllOfUnits"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
