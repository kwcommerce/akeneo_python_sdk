# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.media_files_all_of_embedded_items_inner_all_of_links import MediaFilesAllOfEmbeddedItemsInnerAllOfLinks

class TestMediaFilesAllOfEmbeddedItemsInnerAllOfLinks(unittest.TestCase):
    """MediaFilesAllOfEmbeddedItemsInnerAllOfLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MediaFilesAllOfEmbeddedItemsInnerAllOfLinks:
        """Test MediaFilesAllOfEmbeddedItemsInnerAllOfLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MediaFilesAllOfEmbeddedItemsInnerAllOfLinks`
        """
        model = MediaFilesAllOfEmbeddedItemsInnerAllOfLinks()
        if include_optional:
            return MediaFilesAllOfEmbeddedItemsInnerAllOfLinks(
                var_self = openapi_client.models.media_files_all_of__embedded_items_inner_all_of__links_self.MediaFiles_allOf__embedded_items_inner_allOf__links_self(
                    href = '', ),
                download = openapi_client.models.media_files_all_of__embedded_items_inner_all_of__links_download.MediaFiles_allOf__embedded_items_inner_allOf__links_download(
                    href = '', )
            )
        else:
            return MediaFilesAllOfEmbeddedItemsInnerAllOfLinks(
        )
        """

    def testMediaFilesAllOfEmbeddedItemsInnerAllOfLinks(self):
        """Test MediaFilesAllOfEmbeddedItemsInnerAllOfLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
