# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.reference_entities_all_of_embedded import ReferenceEntitiesAllOfEmbedded

class TestReferenceEntitiesAllOfEmbedded(unittest.TestCase):
    """ReferenceEntitiesAllOfEmbedded unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReferenceEntitiesAllOfEmbedded:
        """Test ReferenceEntitiesAllOfEmbedded
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReferenceEntitiesAllOfEmbedded`
        """
        model = ReferenceEntitiesAllOfEmbedded()
        if include_optional:
            return ReferenceEntitiesAllOfEmbedded(
                items = [
                    openapi_client.models.reference_entities_all_of__embedded_items_inner.Reference_Entities_allOf__embedded_items_inner()
                    ]
            )
        else:
            return ReferenceEntitiesAllOfEmbedded(
        )
        """

    def testReferenceEntitiesAllOfEmbedded(self):
        """Test ReferenceEntitiesAllOfEmbedded"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
