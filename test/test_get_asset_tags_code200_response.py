# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_asset_tags_code200_response import GetAssetTagsCode200Response

class TestGetAssetTagsCode200Response(unittest.TestCase):
    """GetAssetTagsCode200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAssetTagsCode200Response:
        """Test GetAssetTagsCode200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAssetTagsCode200Response`
        """
        model = GetAssetTagsCode200Response()
        if include_optional:
            return GetAssetTagsCode200Response(
                code = ''
            )
        else:
            return GetAssetTagsCode200Response(
                code = '',
        )
        """

    def testGetAssetTagsCode200Response(self):
        """Test GetAssetTagsCode200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()