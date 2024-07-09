# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.app_catalog_list import AppCatalogList

class TestAppCatalogList(unittest.TestCase):
    """AppCatalogList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppCatalogList:
        """Test AppCatalogList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppCatalogList`
        """
        model = AppCatalogList()
        if include_optional:
            return AppCatalogList(
                links = openapi_client.models.products_all_of__embedded_items_inner_all_of__links.Products_allOf__embedded_items_inner_allOf__links(
                    self = openapi_client.models.products_all_of__embedded_items_inner_all_of__links_self.Products_allOf__embedded_items_inner_allOf__links_self(
                        href = '', ), ),
                id = '',
                name = '',
                enabled = True,
                managed_currencies = [
                    ''
                    ],
                managed_locales = [
                    ''
                    ]
            )
        else:
            return AppCatalogList(
        )
        """

    def testAppCatalogList(self):
        """Test AppCatalogList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()