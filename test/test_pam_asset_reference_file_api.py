# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.pam_asset_reference_file_api import PAMAssetReferenceFileApi


class TestPAMAssetReferenceFileApi(unittest.TestCase):
    """PAMAssetReferenceFileApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PAMAssetReferenceFileApi()

    def tearDown(self) -> None:
        pass

    def test_get_reference_files_channel_code_locale_code_download(self) -> None:
        """Test case for get_reference_files_channel_code_locale_code_download

        Download a reference file
        """
        pass

    def test_get_reference_files_locale_code(self) -> None:
        """Test case for get_reference_files_locale_code

        Get a reference file
        """
        pass

    def test_post_reference_files_locale_code(self) -> None:
        """Test case for post_reference_files_locale_code

        Upload a new reference file
        """
        pass


if __name__ == '__main__':
    unittest.main()