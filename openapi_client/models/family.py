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
from openapi_client.models.families_all_of_embedded_items_inner_all_of_attribute_requirements import FamiliesAllOfEmbeddedItemsInnerAllOfAttributeRequirements
from openapi_client.models.families_all_of_embedded_items_inner_all_of_labels import FamiliesAllOfEmbeddedItemsInnerAllOfLabels
from typing import Optional, Set
from typing_extensions import Self

class Family(BaseModel):
    """
    Family
    """ # noqa: E501
    code: StrictStr = Field(description="Family code")
    attribute_as_label: StrictStr = Field(description="Attribute code used as label")
    attribute_as_image: Optional[StrictStr] = Field(default='null', description="Attribute code used as the main picture in the user interface (only since v2.0)")
    attributes: Optional[List[StrictStr]] = Field(default=None, description="Attributes codes that compose the family")
    attribute_requirements: Optional[FamiliesAllOfEmbeddedItemsInnerAllOfAttributeRequirements] = None
    labels: Optional[FamiliesAllOfEmbeddedItemsInnerAllOfLabels] = None
    __properties: ClassVar[List[str]] = ["code", "attribute_as_label", "attribute_as_image", "attributes", "attribute_requirements", "labels"]

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
        """Create an instance of Family from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of attribute_requirements
        if self.attribute_requirements:
            _dict['attribute_requirements'] = self.attribute_requirements.to_dict()
        # override the default output from pydantic by calling `to_dict()` of labels
        if self.labels:
            _dict['labels'] = self.labels.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Family from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "attribute_as_label": obj.get("attribute_as_label"),
            "attribute_as_image": obj.get("attribute_as_image") if obj.get("attribute_as_image") is not None else 'null',
            "attributes": obj.get("attributes"),
            "attribute_requirements": FamiliesAllOfEmbeddedItemsInnerAllOfAttributeRequirements.from_dict(obj["attribute_requirements"]) if obj.get("attribute_requirements") is not None else None,
            "labels": FamiliesAllOfEmbeddedItemsInnerAllOfLabels.from_dict(obj["labels"]) if obj.get("labels") is not None else None
        })
        return _obj


