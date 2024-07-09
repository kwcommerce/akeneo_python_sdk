# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.post_app_catalog201_response import PostAppCatalog201Response

class TestPostAppCatalog201Response(unittest.TestCase):
    """PostAppCatalog201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostAppCatalog201Response:
        """Test PostAppCatalog201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostAppCatalog201Response`
        """
        model = PostAppCatalog201Response()
        if include_optional:
            return PostAppCatalog201Response(
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
            return PostAppCatalog201Response(
        )
        """

    def testPostAppCatalog201Response(self):
        """Test PostAppCatalog201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
