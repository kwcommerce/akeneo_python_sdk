# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.category_list_all_of_values import CategoryListAllOfValues

class TestCategoryListAllOfValues(unittest.TestCase):
    """CategoryListAllOfValues unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CategoryListAllOfValues:
        """Test CategoryListAllOfValues
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CategoryListAllOfValues`
        """
        model = CategoryListAllOfValues()
        if include_optional:
            return CategoryListAllOfValues(
                attribute_code_attribute_uuid_channel_code_locale_code = [
                    openapi_client.models.category_list_all_of_values_attribute_code_attribute_uuid_channel_code_locale_code.CategoryList_allOf_values_attributeCode_attributeUuid_channelCode_localeCode(
                        data = openapi_client.models.category_list_all_of_values_data.CategoryList_allOf_values_data(), 
                        type = '', 
                        locale = '', 
                        channel = '', 
                        attribute_code = '', )
                    ]
            )
        else:
            return CategoryListAllOfValues(
        )
        """

    def testCategoryListAllOfValues(self):
        """Test CategoryListAllOfValues"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
