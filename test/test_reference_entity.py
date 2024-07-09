# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.reference_entity import ReferenceEntity

class TestReferenceEntity(unittest.TestCase):
    """ReferenceEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReferenceEntity:
        """Test ReferenceEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReferenceEntity`
        """
        model = ReferenceEntity()
        if include_optional:
            return ReferenceEntity(
                links = openapi_client.models.get_reference_entities__code__200_response_all_of__links.get_reference_entities__code__200_response_allOf__links(
                    image_download = openapi_client.models.reference_entities_all_of__embedded_items_inner_all_of__links_image_download.Reference_Entities_allOf__embedded_items_inner_allOf__links_image_download(
                        href = '', ), ),
                code = '',
                labels = openapi_client.models.reference_entities_all_of__embedded_items_inner_all_of_labels.Reference_Entities_allOf__embedded_items_inner_allOf_labels(
                    locale_code = '', ),
                image = 'null'
            )
        else:
            return ReferenceEntity(
                code = '',
        )
        """

    def testReferenceEntity(self):
        """Test ReferenceEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
