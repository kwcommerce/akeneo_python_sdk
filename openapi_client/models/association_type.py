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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.association_types_all_of_embedded_items_inner_all_of_labels import AssociationTypesAllOfEmbeddedItemsInnerAllOfLabels
from typing import Optional, Set
from typing_extensions import Self

class AssociationType(BaseModel):
    """
    AssociationType
    """ # noqa: E501
    code: StrictStr = Field(description="Association type code")
    labels: Optional[AssociationTypesAllOfEmbeddedItemsInnerAllOfLabels] = None
    is_quantified: Optional[StrictBool] = Field(default=False, description="When true, the association is a quantified association (Only available in the PIM Serenity version.)")
    is_two_way: Optional[StrictBool] = Field(default=False, description="When true, the association is a two-way association (Only available in the PIM Serenity version.)")
    __properties: ClassVar[List[str]] = ["code", "labels", "is_quantified", "is_two_way"]

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
        """Create an instance of AssociationType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of labels
        if self.labels:
            _dict['labels'] = self.labels.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssociationType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "labels": AssociationTypesAllOfEmbeddedItemsInnerAllOfLabels.from_dict(obj["labels"]) if obj.get("labels") is not None else None,
            "is_quantified": obj.get("is_quantified") if obj.get("is_quantified") is not None else False,
            "is_two_way": obj.get("is_two_way") if obj.get("is_two_way") is not None else False
        })
        return _obj


