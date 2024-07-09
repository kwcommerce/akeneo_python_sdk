# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.product_model import ProductModel

class TestProductModel(unittest.TestCase):
    """ProductModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductModel:
        """Test ProductModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductModel`
        """
        model = ProductModel()
        if include_optional:
            return ProductModel(
                code = '',
                family = '',
                family_variant = '',
                parent = 'null',
                categories = [
                    ''
                    ],
                values = openapi_client.models.product_models_all_of__embedded_items_inner_all_of_values.Product_Models_allOf__embedded_items_inner_allOf_values(
                    attribute_code = [
                        openapi_client.models.product_models_all_of__embedded_items_inner_all_of_values_attribute_code_inner.Product_Models_allOf__embedded_items_inner_allOf_values_attributeCode_inner(
                            scope = '', 
                            locale = '', 
                            data = openapi_client.models.data.data(), 
                            linked_data = openapi_client.models.product_models_all_of__embedded_items_inner_all_of_values_attribute_code_inner_linked_data.Product_Models_allOf__embedded_items_inner_allOf_values_attributeCode_inner_linked_data(
                                attribute = '', 
                                code = '', 
                                labels = openapi_client.models.labels.labels(), ), )
                        ], ),
                associations = openapi_client.models.product_models_all_of__embedded_items_inner_all_of_associations.Product_Models_allOf__embedded_items_inner_allOf_associations(
                    association_type_code = openapi_client.models.products_1_all_of__embedded_items_inner_all_of_associations_association_type_code.Products_1_allOf__embedded_items_inner_allOf_associations_associationTypeCode(
                        groups = [
                            ''
                            ], 
                        products = [
                            ''
                            ], 
                        product_models = [
                            ''
                            ], ), ),
                quantified_associations = openapi_client.models.product_models_all_of__embedded_items_inner_all_of_quantified_associations.Product_Models_allOf__embedded_items_inner_allOf_quantified_associations(
                    quantified_association_type_code = openapi_client.models.product_models_all_of__embedded_items_inner_all_of_quantified_associations_quantified_association_type_code.Product_Models_allOf__embedded_items_inner_allOf_quantified_associations_quantifiedAssociationTypeCode(
                        products = [
                            openapi_client.models.products_1_all_of__embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_products_inner.Products_1_allOf__embedded_items_inner_allOf_quantified_associations_quantifiedAssociationTypeCode_products_inner(
                                identifier = '', 
                                quantity = 56, )
                            ], 
                        product_models = [
                            openapi_client.models.products_all_of__embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_product_models_inner.Products_allOf__embedded_items_inner_allOf_quantified_associations_quantifiedAssociationTypeCode_product_models_inner(
                                code = '', 
                                quantity = 56, )
                            ], ), ),
                created = '',
                updated = '',
                metadata = openapi_client.models.product_models_all_of__embedded_items_inner_all_of_metadata.Product_Models_allOf__embedded_items_inner_allOf_metadata(
                    workflow_status = 'read_only', ),
                quality_scores = None
            )
        else:
            return ProductModel(
                code = '',
                family_variant = '',
        )
        """

    def testProductModel(self):
        """Test ProductModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
