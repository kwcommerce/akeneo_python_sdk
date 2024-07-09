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
from openapi_client.models.measurement_families_get_list200_response_units_unit_code_convert_from_standard_inner import MeasurementFamiliesGetList200ResponseUnitsUnitCodeConvertFromStandardInner
from openapi_client.models.measurement_families_get_list200_response_units_unit_code_labels import MeasurementFamiliesGetList200ResponseUnitsUnitCodeLabels
from typing import Optional, Set
from typing_extensions import Self

class MeasurementFamiliesGetList200ResponseUnitsUnitCode(BaseModel):
    """
    MeasurementFamiliesGetList200ResponseUnitsUnitCode
    """ # noqa: E501
    code: Optional[StrictStr] = Field(default=None, description="Measurement unit code. More details <a href='/concepts/target-market-settings.html#focus-on-the-units'>here</a>.")
    labels: Optional[MeasurementFamiliesGetList200ResponseUnitsUnitCodeLabels] = None
    convert_from_standard: Optional[List[MeasurementFamiliesGetList200ResponseUnitsUnitCodeConvertFromStandardInner]] = Field(default=None, description="Calculation to convert the unit from the standard unit. More details <a href='/concepts/target-market-settings.html#focus-on-the-units'>here</a>.")
    symbol: Optional[StrictStr] = Field(default=None, description="Measurement unit symbol. More details <a href='/concepts/target-market-settings.html#focus-on-the-units'>here</a>.")
    __properties: ClassVar[List[str]] = ["code", "labels", "convert_from_standard", "symbol"]

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
        """Create an instance of MeasurementFamiliesGetList200ResponseUnitsUnitCode from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in convert_from_standard (list)
        _items = []
        if self.convert_from_standard:
            for _item in self.convert_from_standard:
                if _item:
                    _items.append(_item.to_dict())
            _dict['convert_from_standard'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MeasurementFamiliesGetList200ResponseUnitsUnitCode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "labels": MeasurementFamiliesGetList200ResponseUnitsUnitCodeLabels.from_dict(obj["labels"]) if obj.get("labels") is not None else None,
            "convert_from_standard": [MeasurementFamiliesGetList200ResponseUnitsUnitCodeConvertFromStandardInner.from_dict(_item) for _item in obj["convert_from_standard"]] if obj.get("convert_from_standard") is not None else None,
            "symbol": obj.get("symbol")
        })
        return _obj


