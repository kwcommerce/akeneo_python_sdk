# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.family_variants_all_of_embedded_items_inner_all_of_labels import FamilyVariantsAllOfEmbeddedItemsInnerAllOfLabels

class TestFamilyVariantsAllOfEmbeddedItemsInnerAllOfLabels(unittest.TestCase):
    """FamilyVariantsAllOfEmbeddedItemsInnerAllOfLabels unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FamilyVariantsAllOfEmbeddedItemsInnerAllOfLabels:
        """Test FamilyVariantsAllOfEmbeddedItemsInnerAllOfLabels
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FamilyVariantsAllOfEmbeddedItemsInnerAllOfLabels`
        """
        model = FamilyVariantsAllOfEmbeddedItemsInnerAllOfLabels()
        if include_optional:
            return FamilyVariantsAllOfEmbeddedItemsInnerAllOfLabels(
                locale_code = ''
            )
        else:
            return FamilyVariantsAllOfEmbeddedItemsInnerAllOfLabels(
        )
        """

    def testFamilyVariantsAllOfEmbeddedItemsInnerAllOfLabels(self):
        """Test FamilyVariantsAllOfEmbeddedItemsInnerAllOfLabels"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
