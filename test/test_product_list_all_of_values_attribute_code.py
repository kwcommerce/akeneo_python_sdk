# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.product_list_all_of_values_attribute_code import ProductListAllOfValuesAttributeCode

class TestProductListAllOfValuesAttributeCode(unittest.TestCase):
    """ProductListAllOfValuesAttributeCode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductListAllOfValuesAttributeCode:
        """Test ProductListAllOfValuesAttributeCode
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductListAllOfValuesAttributeCode`
        """
        model = ProductListAllOfValuesAttributeCode()
        if include_optional:
            return ProductListAllOfValuesAttributeCode(
                scope = '',
                locale = '',
                data = openapi_client.models.product_list_all_of_values_data.ProductList_allOf_values_data(),
                linked_data = openapi_client.models.product_list_all_of_values_linked_data.ProductList_allOf_values_linked_data(
                    attribute = '', 
                    code = '', 
                    labels = openapi_client.models.product_list_all_of_values_linked_data_labels.ProductList_allOf_values_linked_data_labels(), ),
                attribute_type = '',
                reference_data_name = ''
            )
        else:
            return ProductListAllOfValuesAttributeCode(
        )
        """

    def testProductListAllOfValuesAttributeCode(self):
        """Test ProductListAllOfValuesAttributeCode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
