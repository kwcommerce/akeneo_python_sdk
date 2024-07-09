# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.product_media_file_api import ProductMediaFileApi


class TestProductMediaFileApi(unittest.TestCase):
    """ProductMediaFileApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProductMediaFileApi()

    def tearDown(self) -> None:
        pass

    def test_get_media_files(self) -> None:
        """Test case for get_media_files

        Get a list of product media files
        """
        pass

    def test_get_media_files_code(self) -> None:
        """Test case for get_media_files_code

        Get a product media file
        """
        pass

    def test_get_media_files_code_download(self) -> None:
        """Test case for get_media_files_code_download

        Download a product media file
        """
        pass

    def test_post_media_files(self) -> None:
        """Test case for post_media_files

        Create a new product media file
        """
        pass


if __name__ == '__main__':
    unittest.main()