# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.reference_entities_all_of_embedded_items_inner import ReferenceEntitiesAllOfEmbeddedItemsInner

class TestReferenceEntitiesAllOfEmbeddedItemsInner(unittest.TestCase):
    """ReferenceEntitiesAllOfEmbeddedItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReferenceEntitiesAllOfEmbeddedItemsInner:
        """Test ReferenceEntitiesAllOfEmbeddedItemsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReferenceEntitiesAllOfEmbeddedItemsInner`
        """
        model = ReferenceEntitiesAllOfEmbeddedItemsInner()
        if include_optional:
            return ReferenceEntitiesAllOfEmbeddedItemsInner(
                links = openapi_client.models.reference_entities_all_of__embedded_items_inner_all_of__links.Reference_Entities_allOf__embedded_items_inner_allOf__links(
                    self = openapi_client.models.products_all_of__embedded_items_inner_all_of__links_self.Products_allOf__embedded_items_inner_allOf__links_self(
                        href = '', ), 
                    image_download = openapi_client.models.reference_entities_all_of__embedded_items_inner_all_of__links_image_download.Reference_Entities_allOf__embedded_items_inner_allOf__links_image_download(
                        href = '', ), ),
                code = '',
                labels = openapi_client.models.reference_entities_all_of__embedded_items_inner_all_of_labels.Reference_Entities_allOf__embedded_items_inner_allOf_labels(
                    locale_code = '', ),
                image = 'null'
            )
        else:
            return ReferenceEntitiesAllOfEmbeddedItemsInner(
                code = '',
        )
        """

    def testReferenceEntitiesAllOfEmbeddedItemsInner(self):
        """Test ReferenceEntitiesAllOfEmbeddedItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
