# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.error_by_line import ErrorByLine

class TestErrorByLine(unittest.TestCase):
    """ErrorByLine unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorByLine:
        """Test ErrorByLine
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorByLine`
        """
        model = ErrorByLine()
        if include_optional:
            return ErrorByLine(
                line = 56,
                identifier = '',
                code = '',
                status_code = 56,
                message = ''
            )
        else:
            return ErrorByLine(
        )
        """

    def testErrorByLine(self):
        """Test ErrorByLine"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()