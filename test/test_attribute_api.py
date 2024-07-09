# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.attribute_api import AttributeApi


class TestAttributeApi(unittest.TestCase):
    """AttributeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AttributeApi()

    def tearDown(self) -> None:
        pass

    def test_get_attributes(self) -> None:
        """Test case for get_attributes

        Get list of attributes
        """
        pass

    def test_get_attributes_code(self) -> None:
        """Test case for get_attributes_code

        Get an attribute
        """
        pass

    def test_patch_attributes(self) -> None:
        """Test case for patch_attributes

        Update/create several attributes
        """
        pass

    def test_patch_attributes_code(self) -> None:
        """Test case for patch_attributes_code

        Update/create an attribute
        """
        pass

    def test_post_attributes(self) -> None:
        """Test case for post_attributes

        Create a new attribute
        """
        pass


if __name__ == '__main__':
    unittest.main()
