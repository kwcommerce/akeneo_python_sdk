# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.products_all_of_embedded_items_inner_all_of_values_value_inner_linked_data import ProductsAllOfEmbeddedItemsInnerAllOfValuesValueInnerLinkedData

class TestProductsAllOfEmbeddedItemsInnerAllOfValuesValueInnerLinkedData(unittest.TestCase):
    """ProductsAllOfEmbeddedItemsInnerAllOfValuesValueInnerLinkedData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductsAllOfEmbeddedItemsInnerAllOfValuesValueInnerLinkedData:
        """Test ProductsAllOfEmbeddedItemsInnerAllOfValuesValueInnerLinkedData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductsAllOfEmbeddedItemsInnerAllOfValuesValueInnerLinkedData`
        """
        model = ProductsAllOfEmbeddedItemsInnerAllOfValuesValueInnerLinkedData()
        if include_optional:
            return ProductsAllOfEmbeddedItemsInnerAllOfValuesValueInnerLinkedData(
                attribute = '',
                code = '',
                labels = openapi_client.models.labels.labels()
            )
        else:
            return ProductsAllOfEmbeddedItemsInnerAllOfValuesValueInnerLinkedData(
        )
        """

    def testProductsAllOfEmbeddedItemsInnerAllOfValuesValueInnerLinkedData(self):
        """Test ProductsAllOfEmbeddedItemsInnerAllOfValuesValueInnerLinkedData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
