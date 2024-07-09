# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.product_models_all_of_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code import ProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode

class TestProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode(unittest.TestCase):
    """ProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode:
        """Test ProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode`
        """
        model = ProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode()
        if include_optional:
            return ProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode(
                products = [
                    openapi_client.models.products_1_all_of__embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_products_inner.Products_1_allOf__embedded_items_inner_allOf_quantified_associations_quantifiedAssociationTypeCode_products_inner(
                        identifier = '', 
                        quantity = 56, )
                    ],
                product_models = [
                    openapi_client.models.products_all_of__embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_product_models_inner.Products_allOf__embedded_items_inner_allOf_quantified_associations_quantifiedAssociationTypeCode_product_models_inner(
                        code = '', 
                        quantity = 56, )
                    ]
            )
        else:
            return ProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode(
        )
        """

    def testProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode(self):
        """Test ProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()