# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.categories_all_of_embedded_items_inner import CategoriesAllOfEmbeddedItemsInner

class TestCategoriesAllOfEmbeddedItemsInner(unittest.TestCase):
    """CategoriesAllOfEmbeddedItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CategoriesAllOfEmbeddedItemsInner:
        """Test CategoriesAllOfEmbeddedItemsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CategoriesAllOfEmbeddedItemsInner`
        """
        model = CategoriesAllOfEmbeddedItemsInner()
        if include_optional:
            return CategoriesAllOfEmbeddedItemsInner(
                links = openapi_client.models.products_all_of__embedded_items_inner_all_of__links.Products_allOf__embedded_items_inner_allOf__links(
                    self = openapi_client.models.products_all_of__embedded_items_inner_all_of__links_self.Products_allOf__embedded_items_inner_allOf__links_self(
                        href = '', ), ),
                code = '',
                parent = 'null',
                updated = '',
                position = 56,
                labels = openapi_client.models.categories_all_of__embedded_items_inner_all_of_labels.Categories_allOf__embedded_items_inner_allOf_labels(
                    locale_code = '', ),
                values = openapi_client.models.categories_all_of__embedded_items_inner_all_of_values.Categories_allOf__embedded_items_inner_allOf_values(
                    attribute_code|attribute_uuid|channel_code|locale_code = [
                        openapi_client.models.categories_all_of__embedded_items_inner_all_of_values_attribute_code_attribute_uuid_channel_code_locale_code_inner.Categories_allOf__embedded_items_inner_allOf_values_attributeCode_attributeUuid_channelCode_localeCode_inner(
                            data = openapi_client.models.data.data(), 
                            type = '', 
                            locale = '', 
                            channel = '', 
                            attribute_code = '', )
                        ], )
            )
        else:
            return CategoriesAllOfEmbeddedItemsInner(
                code = '',
        )
        """

    def testCategoriesAllOfEmbeddedItemsInner(self):
        """Test CategoriesAllOfEmbeddedItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
