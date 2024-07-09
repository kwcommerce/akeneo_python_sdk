# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.asset_families_all_of_embedded_items_inner_all_of_labels import AssetFamiliesAllOfEmbeddedItemsInnerAllOfLabels
from openapi_client.models.asset_families_all_of_embedded_items_inner_all_of_naming_convention import AssetFamiliesAllOfEmbeddedItemsInnerAllOfNamingConvention
from openapi_client.models.asset_families_all_of_embedded_items_inner_all_of_product_link_rules_inner import AssetFamiliesAllOfEmbeddedItemsInnerAllOfProductLinkRulesInner
from openapi_client.models.asset_families_all_of_embedded_items_inner_all_of_transformations_inner import AssetFamiliesAllOfEmbeddedItemsInnerAllOfTransformationsInner
from openapi_client.models.products_all_of_embedded_items_inner_all_of_links import ProductsAllOfEmbeddedItemsInnerAllOfLinks
from typing import Optional, Set
from typing_extensions import Self

class AssetFamiliesAllOfEmbeddedItemsInner(BaseModel):
    """
    AssetFamiliesAllOfEmbeddedItemsInner
    """ # noqa: E501
    links: Optional[ProductsAllOfEmbeddedItemsInnerAllOfLinks] = Field(default=None, alias="_links")
    code: StrictStr = Field(description="Asset family code")
    labels: Optional[AssetFamiliesAllOfEmbeddedItemsInnerAllOfLabels] = None
    attribute_as_main_media: Optional[StrictStr] = Field(default='First media file or media link attribute that was created', description="Attribute code that is used as the main media of the asset family.")
    naming_convention: Optional[AssetFamiliesAllOfEmbeddedItemsInnerAllOfNamingConvention] = None
    product_link_rules: Optional[List[AssetFamiliesAllOfEmbeddedItemsInnerAllOfProductLinkRulesInner]] = Field(default=None, description="The rules that will be run after the asset creation, in order to automatically link the assets of this family to a set of products. To understand the format of this property, see <a href='/concepts/asset-manager.html#focus-on-the-product-link-rule'>here</a>.")
    transformations: Optional[List[AssetFamiliesAllOfEmbeddedItemsInnerAllOfTransformationsInner]] = Field(default=None, description="The transformations to perform on source files in order to generate new files into your asset attributes (only available since v4.0). To understand the format of this property, see <a href='/concepts/asset-manager.html#focus-on-the-transformations'>here</a>.")
    __properties: ClassVar[List[str]] = ["_links", "code", "labels", "attribute_as_main_media", "naming_convention", "product_link_rules", "transformations"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AssetFamiliesAllOfEmbeddedItemsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of labels
        if self.labels:
            _dict['labels'] = self.labels.to_dict()
        # override the default output from pydantic by calling `to_dict()` of naming_convention
        if self.naming_convention:
            _dict['naming_convention'] = self.naming_convention.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in product_link_rules (list)
        _items = []
        if self.product_link_rules:
            for _item in self.product_link_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['product_link_rules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in transformations (list)
        _items = []
        if self.transformations:
            for _item in self.transformations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transformations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssetFamiliesAllOfEmbeddedItemsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_links": ProductsAllOfEmbeddedItemsInnerAllOfLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "code": obj.get("code"),
            "labels": AssetFamiliesAllOfEmbeddedItemsInnerAllOfLabels.from_dict(obj["labels"]) if obj.get("labels") is not None else None,
            "attribute_as_main_media": obj.get("attribute_as_main_media") if obj.get("attribute_as_main_media") is not None else 'First media file or media link attribute that was created',
            "naming_convention": AssetFamiliesAllOfEmbeddedItemsInnerAllOfNamingConvention.from_dict(obj["naming_convention"]) if obj.get("naming_convention") is not None else None,
            "product_link_rules": [AssetFamiliesAllOfEmbeddedItemsInnerAllOfProductLinkRulesInner.from_dict(_item) for _item in obj["product_link_rules"]] if obj.get("product_link_rules") is not None else None,
            "transformations": [AssetFamiliesAllOfEmbeddedItemsInnerAllOfTransformationsInner.from_dict(_item) for _item in obj["transformations"]] if obj.get("transformations") is not None else None
        })
        return _obj


