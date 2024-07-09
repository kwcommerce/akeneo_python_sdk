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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.attributes_all_of_embedded_items_inner_all_of_labels import AttributesAllOfEmbeddedItemsInnerAllOfLabels
from typing import Optional, Set
from typing_extensions import Self

class GetAssetFamiliesCodeAttributes200ResponseInner(BaseModel):
    """
    GetAssetFamiliesCodeAttributes200ResponseInner
    """ # noqa: E501
    code: StrictStr = Field(description="Attribute code")
    labels: Optional[AttributesAllOfEmbeddedItemsInnerAllOfLabels] = None
    type: StrictStr = Field(description="Attribute type. See <a href='/concepts/asset-manager.html#asset-attribute'>type</a> section for more details.")
    value_per_locale: Optional[StrictBool] = Field(default=False, description="Whether the attribute is localizable, i.e. can have one value by locale")
    value_per_channel: Optional[StrictBool] = Field(default=False, description="Whether the attribute is scopable, i.e. can have one value by channel")
    is_required_for_completeness: Optional[StrictBool] = Field(default=False, description="Whether the attribute should be part of the record's completeness calculation")
    is_read_only: Optional[StrictBool] = Field(default=False, description="Whether the attribute should be in read only mode only in the UI, but you can still update it with the API")
    max_characters: Optional[StrictInt] = Field(default=None, description="Maximum number of characters allowed for the value of the attribute when the attribute type is `text`")
    is_textarea: Optional[StrictBool] = Field(default=False, description="Whether the UI should display a text area instead of a simple field when the attribute type is `text`")
    is_rich_text_editor: Optional[StrictBool] = Field(default=None, description="Whether the UI should display a rich text editor instead of a simple text area when the attribute type is `text`")
    validation_rule: Optional[StrictStr] = Field(default='none', description="Validation rule type used to validate the attribute value when the attribute type is `text`")
    validation_regexp: Optional[StrictStr] = Field(default='null', description="Regexp expression used to validate the attribute value when the attribute type is `text`")
    allowed_extensions: Optional[List[StrictStr]] = Field(default=None, description="Extensions allowed when the attribute type is `media_file`")
    max_file_size: Optional[StrictStr] = Field(default='null', description="Max file size in MB when the attribute type is `media_file`")
    decimals_allowed: Optional[StrictBool] = Field(default=False, description="Whether decimals are allowed when the attribute type is `number`")
    min_value: Optional[StrictStr] = Field(default='null', description="Minimum value allowed when the attribute type is `number`")
    max_value: Optional[StrictStr] = Field(default='null', description="Maximum value allowed when the attribute type is `number`")
    media_type: StrictStr = Field(description="For the `media_link` attribute type, it is the type of the media behind the url, to allow its preview in the PIM. For the `media_file` attribute type, it is the type of the file.")
    prefix: Optional[StrictStr] = Field(default='null', description="Prefix of the `media_link` attribute type. The common url root that prefixes the link to the media")
    suffix: Optional[StrictStr] = Field(default='null', description="Suffix of the `media_link` attribute type. The common url suffix for the media")
    reference_entity: Optional[StrictStr] = Field(default='null', description="Reference entity code for the `record` attribute type (see <a href='/api-reference.html#Referenceentity'>Reference entity</a>).")
    __properties: ClassVar[List[str]] = ["code", "labels", "type", "value_per_locale", "value_per_channel", "is_required_for_completeness", "is_read_only", "max_characters", "is_textarea", "is_rich_text_editor", "validation_rule", "validation_regexp", "allowed_extensions", "max_file_size", "decimals_allowed", "min_value", "max_value", "media_type", "prefix", "suffix", "reference_entity"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['text', 'media_link', 'number', 'media_file', 'single_option', 'multiple_options', 'boolean', 'date', 'record']):
            raise ValueError("must be one of enum values ('text', 'media_link', 'number', 'media_file', 'single_option', 'multiple_options', 'boolean', 'date', 'record')")
        return value

    @field_validator('validation_rule')
    def validation_rule_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['email', 'url', 'regexp', 'none']):
            raise ValueError("must be one of enum values ('email', 'url', 'regexp', 'none')")
        return value

    @field_validator('media_type')
    def media_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['image', 'pdf', 'youtube', 'vimeo', 'other']):
            raise ValueError("must be one of enum values ('image', 'pdf', 'youtube', 'vimeo', 'other')")
        return value

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
        """Create an instance of GetAssetFamiliesCodeAttributes200ResponseInner from a JSON string"""
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
        """Create an instance of GetAssetFamiliesCodeAttributes200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "labels": AttributesAllOfEmbeddedItemsInnerAllOfLabels.from_dict(obj["labels"]) if obj.get("labels") is not None else None,
            "type": obj.get("type"),
            "value_per_locale": obj.get("value_per_locale") if obj.get("value_per_locale") is not None else False,
            "value_per_channel": obj.get("value_per_channel") if obj.get("value_per_channel") is not None else False,
            "is_required_for_completeness": obj.get("is_required_for_completeness") if obj.get("is_required_for_completeness") is not None else False,
            "is_read_only": obj.get("is_read_only") if obj.get("is_read_only") is not None else False,
            "max_characters": obj.get("max_characters"),
            "is_textarea": obj.get("is_textarea") if obj.get("is_textarea") is not None else False,
            "is_rich_text_editor": obj.get("is_rich_text_editor"),
            "validation_rule": obj.get("validation_rule") if obj.get("validation_rule") is not None else 'none',
            "validation_regexp": obj.get("validation_regexp") if obj.get("validation_regexp") is not None else 'null',
            "allowed_extensions": obj.get("allowed_extensions"),
            "max_file_size": obj.get("max_file_size") if obj.get("max_file_size") is not None else 'null',
            "decimals_allowed": obj.get("decimals_allowed") if obj.get("decimals_allowed") is not None else False,
            "min_value": obj.get("min_value") if obj.get("min_value") is not None else 'null',
            "max_value": obj.get("max_value") if obj.get("max_value") is not None else 'null',
            "media_type": obj.get("media_type"),
            "prefix": obj.get("prefix") if obj.get("prefix") is not None else 'null',
            "suffix": obj.get("suffix") if obj.get("suffix") is not None else 'null',
            "reference_entity": obj.get("reference_entity") if obj.get("reference_entity") is not None else 'null'
        })
        return _obj


