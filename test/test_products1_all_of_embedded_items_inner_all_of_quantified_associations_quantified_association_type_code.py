# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.products1_all_of_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code import Products1AllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode

class TestProducts1AllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode(unittest.TestCase):
    """Products1AllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Products1AllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode:
        """Test Products1AllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Products1AllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode`
        """
        model = Products1AllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode()
        if include_optional:
            return Products1AllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode(
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
            return Products1AllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode(
        )
        """

    def testProducts1AllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode(self):
        """Test Products1AllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
