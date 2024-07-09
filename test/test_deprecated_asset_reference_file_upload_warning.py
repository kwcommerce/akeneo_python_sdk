# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.deprecated_asset_reference_file_upload_warning import DeprecatedAssetReferenceFileUploadWarning

class TestDeprecatedAssetReferenceFileUploadWarning(unittest.TestCase):
    """DeprecatedAssetReferenceFileUploadWarning unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeprecatedAssetReferenceFileUploadWarning:
        """Test DeprecatedAssetReferenceFileUploadWarning
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeprecatedAssetReferenceFileUploadWarning`
        """
        model = DeprecatedAssetReferenceFileUploadWarning()
        if include_optional:
            return DeprecatedAssetReferenceFileUploadWarning(
                message = '',
                errors = [
                    openapi_client.models.post_reference_files__locale_code__201_response_errors_inner.post_reference_files__locale_code__201_response_errors_inner(
                        channel = '', 
                        locale = '', 
                        message = '', )
                    ]
            )
        else:
            return DeprecatedAssetReferenceFileUploadWarning(
        )
        """

    def testDeprecatedAssetReferenceFileUploadWarning(self):
        """Test DeprecatedAssetReferenceFileUploadWarning"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
