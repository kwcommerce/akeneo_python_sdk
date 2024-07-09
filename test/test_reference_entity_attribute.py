# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.reference_entity_attribute import ReferenceEntityAttribute

class TestReferenceEntityAttribute(unittest.TestCase):
    """ReferenceEntityAttribute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReferenceEntityAttribute:
        """Test ReferenceEntityAttribute
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReferenceEntityAttribute`
        """
        model = ReferenceEntityAttribute()
        if include_optional:
            return ReferenceEntityAttribute(
                code = '',
                labels = openapi_client.models.attributes_all_of__embedded_items_inner_all_of_labels.Attributes_allOf__embedded_items_inner_allOf_labels(
                    locale_code = '', ),
                type = 'text',
                value_per_locale = True,
                value_per_channel = True,
                is_required_for_completeness = True,
                max_characters = 56,
                is_textarea = True,
                is_rich_text_editor = True,
                validation_rule = 'none',
                validation_regexp = 'null',
                allowed_extensions = [
                    ''
                    ],
                max_file_size = 'null',
                reference_entity_code = 'null',
                decimals_allowed = True,
                min_value = 'null',
                max_value = 'null'
            )
        else:
            return ReferenceEntityAttribute(
                code = '',
                type = 'text',
        )
        """

    def testReferenceEntityAttribute(self):
        """Test ReferenceEntityAttribute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
