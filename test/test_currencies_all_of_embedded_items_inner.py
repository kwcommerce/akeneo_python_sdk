# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.currencies_all_of_embedded_items_inner import CurrenciesAllOfEmbeddedItemsInner

class TestCurrenciesAllOfEmbeddedItemsInner(unittest.TestCase):
    """CurrenciesAllOfEmbeddedItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CurrenciesAllOfEmbeddedItemsInner:
        """Test CurrenciesAllOfEmbeddedItemsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CurrenciesAllOfEmbeddedItemsInner`
        """
        model = CurrenciesAllOfEmbeddedItemsInner()
        if include_optional:
            return CurrenciesAllOfEmbeddedItemsInner(
                links = openapi_client.models.products_all_of__embedded_items_inner_all_of__links.Products_allOf__embedded_items_inner_allOf__links(
                    self = openapi_client.models.products_all_of__embedded_items_inner_all_of__links_self.Products_allOf__embedded_items_inner_allOf__links_self(
                        href = '', ), ),
                code = '',
                enabled = True,
                label = ''
            )
        else:
            return CurrenciesAllOfEmbeddedItemsInner(
                code = '',
        )
        """

    def testCurrenciesAllOfEmbeddedItemsInner(self):
        """Test CurrenciesAllOfEmbeddedItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
