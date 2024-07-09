# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.post_media_files_request import PostMediaFilesRequest

class TestPostMediaFilesRequest(unittest.TestCase):
    """PostMediaFilesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostMediaFilesRequest:
        """Test PostMediaFilesRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostMediaFilesRequest`
        """
        model = PostMediaFilesRequest()
        if include_optional:
            return PostMediaFilesRequest(
                product = '',
                product_model = '',
                file = bytes(b'blah')
            )
        else:
            return PostMediaFilesRequest(
                file = bytes(b'blah'),
        )
        """

    def testPostMediaFilesRequest(self):
        """Test PostMediaFilesRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()