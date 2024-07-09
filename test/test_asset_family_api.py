# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.asset_family_api import AssetFamilyApi


class TestAssetFamilyApi(unittest.TestCase):
    """AssetFamilyApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AssetFamilyApi()

    def tearDown(self) -> None:
        pass

    def test_get_asset_families(self) -> None:
        """Test case for get_asset_families

        Get list of asset families
        """
        pass

    def test_get_asset_family_code(self) -> None:
        """Test case for get_asset_family_code

        Get an asset family
        """
        pass

    def test_patch_asset_family_code(self) -> None:
        """Test case for patch_asset_family_code

        Update/create an asset family
        """
        pass


if __name__ == '__main__':
    unittest.main()
