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
from openapi_client.models.pam_asset_categories_all_of_embedded_items_inner_all_of_labels import PAMAssetCategoriesAllOfEmbeddedItemsInnerAllOfLabels
from openapi_client.models.products_all_of_embedded_items_inner_all_of_links import ProductsAllOfEmbeddedItemsInnerAllOfLinks
from typing import Optional, Set
from typing_extensions import Self

class DeprecatedAssetCategoryList(BaseModel):
    """
    DeprecatedAssetCategoryList
    """ # noqa: E501
    links: Optional[ProductsAllOfEmbeddedItemsInnerAllOfLinks] = Field(default=None, alias="_links")
    code: StrictStr = Field(description="PAM asset category code")
    parent: Optional[StrictStr] = Field(default='null', description="PAM ssset category code of the parent's asset category")
    labels: Optional[PAMAssetCategoriesAllOfEmbeddedItemsInnerAllOfLabels] = None
    __properties: ClassVar[List[str]] = ["_links", "code", "parent", "labels"]

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
        """Create an instance of DeprecatedAssetCategoryList from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeprecatedAssetCategoryList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_links": ProductsAllOfEmbeddedItemsInnerAllOfLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "code": obj.get("code"),
            "parent": obj.get("parent") if obj.get("parent") is not None else 'null',
            "labels": PAMAssetCategoriesAllOfEmbeddedItemsInnerAllOfLabels.from_dict(obj["labels"]) if obj.get("labels") is not None else None
        })
        return _obj


