# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.categories_all_of_embedded_items_inner_all_of_values import CategoriesAllOfEmbeddedItemsInnerAllOfValues

class TestCategoriesAllOfEmbeddedItemsInnerAllOfValues(unittest.TestCase):
    """CategoriesAllOfEmbeddedItemsInnerAllOfValues unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CategoriesAllOfEmbeddedItemsInnerAllOfValues:
        """Test CategoriesAllOfEmbeddedItemsInnerAllOfValues
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CategoriesAllOfEmbeddedItemsInnerAllOfValues`
        """
        model = CategoriesAllOfEmbeddedItemsInnerAllOfValues()
        if include_optional:
            return CategoriesAllOfEmbeddedItemsInnerAllOfValues(
                attribute_code_attribute_uuid_channel_code_locale_code = [
                    openapi_client.models.categories_all_of__embedded_items_inner_all_of_values_attribute_code_attribute_uuid_channel_code_locale_code_inner.Categories_allOf__embedded_items_inner_allOf_values_attributeCode_attributeUuid_channelCode_localeCode_inner(
                        data = openapi_client.models.data.data(), 
                        type = '', 
                        locale = '', 
                        channel = '', 
                        attribute_code = '', )
                    ]
            )
        else:
            return CategoriesAllOfEmbeddedItemsInnerAllOfValues(
        )
        """

    def testCategoriesAllOfEmbeddedItemsInnerAllOfValues(self):
        """Test CategoriesAllOfEmbeddedItemsInnerAllOfValues"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()