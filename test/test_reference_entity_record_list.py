# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.reference_entity_record_list import ReferenceEntityRecordList

class TestReferenceEntityRecordList(unittest.TestCase):
    """ReferenceEntityRecordList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReferenceEntityRecordList:
        """Test ReferenceEntityRecordList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReferenceEntityRecordList`
        """
        model = ReferenceEntityRecordList()
        if include_optional:
            return ReferenceEntityRecordList(
                links = openapi_client.models.products_all_of__embedded_items_inner_all_of__links.Products_allOf__embedded_items_inner_allOf__links(
                    self = openapi_client.models.products_all_of__embedded_items_inner_all_of__links_self.Products_allOf__embedded_items_inner_allOf__links_self(
                        href = '', ), ),
                code = '',
                values = openapi_client.models.reference_entity_record_list_all_of_values.ReferenceEntityRecordList_allOf_values(
                    attribute_code = [
                        openapi_client.models.reference_entity_record_list_all_of_values_attribute_code.ReferenceEntityRecordList_allOf_values_attributeCode(
                            channel = '', 
                            locale = '', 
                            data = openapi_client.models.reference_entity_record_list_all_of_values_data.ReferenceEntityRecordList_allOf_values_data(), )
                        ], ),
                created = 'null',
                updated = 'null'
            )
        else:
            return ReferenceEntityRecordList(
                code = '',
        )
        """

    def testReferenceEntityRecordList(self):
        """Test ReferenceEntityRecordList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
