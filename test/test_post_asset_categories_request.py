# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.post_asset_categories_request import PostAssetCategoriesRequest

class TestPostAssetCategoriesRequest(unittest.TestCase):
    """PostAssetCategoriesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostAssetCategoriesRequest:
        """Test PostAssetCategoriesRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostAssetCategoriesRequest`
        """
        model = PostAssetCategoriesRequest()
        if include_optional:
            return PostAssetCategoriesRequest(
                code = '',
                parent = 'null',
                labels = openapi_client.models.pam_asset_categories_all_of__embedded_items_inner_all_of_labels.PAM_Asset_Categories_allOf__embedded_items_inner_allOf_labels(
                    locale_code = '', )
            )
        else:
            return PostAssetCategoriesRequest(
                code = '',
        )
        """

    def testPostAssetCategoriesRequest(self):
        """Test PostAssetCategoriesRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
