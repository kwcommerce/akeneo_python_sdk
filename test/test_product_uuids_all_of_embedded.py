# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.product_uuids_all_of_embedded import ProductUuidsAllOfEmbedded

class TestProductUuidsAllOfEmbedded(unittest.TestCase):
    """ProductUuidsAllOfEmbedded unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductUuidsAllOfEmbedded:
        """Test ProductUuidsAllOfEmbedded
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductUuidsAllOfEmbedded`
        """
        model = ProductUuidsAllOfEmbedded()
        if include_optional:
            return ProductUuidsAllOfEmbedded(
                items = [
                    ''
                    ]
            )
        else:
            return ProductUuidsAllOfEmbedded(
        )
        """

    def testProductUuidsAllOfEmbedded(self):
        """Test ProductUuidsAllOfEmbedded"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()