# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.asset_family_list import AssetFamilyList

class TestAssetFamilyList(unittest.TestCase):
    """AssetFamilyList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssetFamilyList:
        """Test AssetFamilyList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AssetFamilyList`
        """
        model = AssetFamilyList()
        if include_optional:
            return AssetFamilyList(
                links = openapi_client.models.products_all_of__embedded_items_inner_all_of__links.Products_allOf__embedded_items_inner_allOf__links(
                    self = openapi_client.models.products_all_of__embedded_items_inner_all_of__links_self.Products_allOf__embedded_items_inner_allOf__links_self(
                        href = '', ), ),
                code = '',
                labels = openapi_client.models.asset_families_all_of__embedded_items_inner_all_of_labels.Asset_families_allOf__embedded_items_inner_allOf_labels(
                    locale_code = '', ),
                attribute_as_main_media = 'First media file or media link attribute that was created',
                naming_convention = openapi_client.models.asset_family_list_all_of_naming_convention.AssetFamilyList_allOf_naming_convention(
                    source = openapi_client.models.asset_family_list_all_of_naming_convention_source.AssetFamilyList_allOf_naming_convention_source(), 
                    pattern = '', 
                    abort_asset_creation_on_error = True, ),
                product_link_rules = [
                    openapi_client.models.asset_families_all_of__embedded_items_inner_all_of_product_link_rules_inner.Asset_families_allOf__embedded_items_inner_allOf_product_link_rules_inner(
                        product_selections = [
                            openapi_client.models.asset_families_all_of__embedded_items_inner_all_of_product_link_rules_inner_product_selections_inner.Asset_families_allOf__embedded_items_inner_allOf_product_link_rules_inner_product_selections_inner(
                                field = '', 
                                operator = '', 
                                value = '', 
                                locale = '', 
                                channel = '', )
                            ], 
                        assign_assets_to = [
                            openapi_client.models.asset_families_all_of__embedded_items_inner_all_of_product_link_rules_inner_assign_assets_to_inner.Asset_families_allOf__embedded_items_inner_allOf_product_link_rules_inner_assign_assets_to_inner(
                                attribute = '', 
                                locale = '', 
                                channel = '', 
                                mode = '', )
                            ], )
                    ],
                transformations = [
                    openapi_client.models.asset_families_all_of__embedded_items_inner_all_of_transformations_inner.Asset_families_allOf__embedded_items_inner_allOf_transformations_inner(
                        label = '', 
                        filename_suffix = '', 
                        filename_prefix = '', 
                        source = openapi_client.models.asset_families_all_of__embedded_items_inner_all_of_transformations_inner_source.Asset_families_allOf__embedded_items_inner_allOf_transformations_inner_source(
                            attribute = '', 
                            channel = '', 
                            locale = '', ), 
                        target = openapi_client.models.asset_families_all_of__embedded_items_inner_all_of_transformations_inner_target.Asset_families_allOf__embedded_items_inner_allOf_transformations_inner_target(
                            attribute = '', 
                            channel = '', 
                            locale = '', ), 
                        operations = openapi_client.models.asset_families_all_of__embedded_items_inner_all_of_transformations_inner_operations.Asset_families_allOf__embedded_items_inner_allOf_transformations_inner_operations(
                            type = '', 
                            parameters = openapi_client.models.asset_families_all_of__embedded_items_inner_all_of_transformations_inner_operations_parameters.Asset_families_allOf__embedded_items_inner_allOf_transformations_inner_operations_parameters(
                                colorspace = '', 
                                width = 56, 
                                height = 56, 
                                ratio = 56, 
                                resolution_unit = '', 
                                resolution_x = 56, 
                                resolution_y = 56, 
                                quality = 56, ), ), )
                    ]
            )
        else:
            return AssetFamilyList(
                code = '',
        )
        """

    def testAssetFamilyList(self):
        """Test AssetFamilyList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()