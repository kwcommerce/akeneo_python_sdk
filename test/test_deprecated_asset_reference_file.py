# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.deprecated_asset_reference_file import DeprecatedAssetReferenceFile

class TestDeprecatedAssetReferenceFile(unittest.TestCase):
    """DeprecatedAssetReferenceFile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeprecatedAssetReferenceFile:
        """Test DeprecatedAssetReferenceFile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeprecatedAssetReferenceFile`
        """
        model = DeprecatedAssetReferenceFile()
        if include_optional:
            return DeprecatedAssetReferenceFile(
                code = '',
                locale = '',
                link = openapi_client.models.get_reference_files__locale_code__200_response__link.get_reference_files__locale_code__200_response__link(
                    download = openapi_client.models.pam_assets_all_of__embedded_items_inner_all_of_reference_files_inner__link_download.PAM_Assets_allOf__embedded_items_inner_allOf_reference_files_inner__link_download(
                        href = '', ), )
            )
        else:
            return DeprecatedAssetReferenceFile(
        )
        """

    def testDeprecatedAssetReferenceFile(self):
        """Test DeprecatedAssetReferenceFile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()