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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.asset_families_all_of_embedded_items_inner_all_of_transformations_inner_operations_parameters import AssetFamiliesAllOfEmbeddedItemsInnerAllOfTransformationsInnerOperationsParameters
from typing import Optional, Set
from typing_extensions import Self

class AssetFamiliesAllOfEmbeddedItemsInnerAllOfTransformationsInnerOperations(BaseModel):
    """
    The transformations that should be applied to your source file to generate the target file. More details <a href='/concepts/asset-manager.html#transformation-operations'>here</a>.
    """ # noqa: E501
    type: Optional[StrictStr] = None
    parameters: Optional[AssetFamiliesAllOfEmbeddedItemsInnerAllOfTransformationsInnerOperationsParameters] = None
    __properties: ClassVar[List[str]] = ["type", "parameters"]

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
        """Create an instance of AssetFamiliesAllOfEmbeddedItemsInnerAllOfTransformationsInnerOperations from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssetFamiliesAllOfEmbeddedItemsInnerAllOfTransformationsInnerOperations from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "parameters": AssetFamiliesAllOfEmbeddedItemsInnerAllOfTransformationsInnerOperationsParameters.from_dict(obj["parameters"]) if obj.get("parameters") is not None else None
        })
        return _obj


