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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.attributes_all_of_embedded_items_inner_all_of_group_labels import AttributesAllOfEmbeddedItemsInnerAllOfGroupLabels
from openapi_client.models.attributes_all_of_embedded_items_inner_all_of_labels import AttributesAllOfEmbeddedItemsInnerAllOfLabels
from openapi_client.models.attributes_all_of_embedded_items_inner_all_of_table_configuration_inner import AttributesAllOfEmbeddedItemsInnerAllOfTableConfigurationInner
from openapi_client.models.products_all_of_embedded_items_inner_all_of_links import ProductsAllOfEmbeddedItemsInnerAllOfLinks
from typing import Optional, Set
from typing_extensions import Self

class AttributeList(BaseModel):
    """
    AttributeList
    """ # noqa: E501
    links: Optional[ProductsAllOfEmbeddedItemsInnerAllOfLinks] = Field(default=None, alias="_links")
    code: StrictStr = Field(description="Attribute code")
    type: StrictStr = Field(description="Attribute type. See <a href='/concepts/catalog-structure.html#attribute'>type</a> section for more details.")
    labels: Optional[AttributesAllOfEmbeddedItemsInnerAllOfLabels] = None
    group: StrictStr = Field(description="Attribute group")
    group_labels: Optional[AttributesAllOfEmbeddedItemsInnerAllOfGroupLabels] = None
    sort_order: Optional[StrictInt] = Field(default=None, description="Order of the attribute in its group")
    localizable: Optional[StrictBool] = Field(default=False, description="Whether the attribute is localizable, i.e. can have one value by locale")
    scopable: Optional[StrictBool] = Field(default=False, description="Whether the attribute is scopable, i.e. can have one value by channel")
    available_locales: Optional[List[StrictStr]] = Field(default=None, description="To make the attribute locale specfic, specify here for which locales it is specific")
    unique: Optional[StrictBool] = Field(default=None, description="Whether two values for the attribute cannot be the same")
    useable_as_grid_filter: Optional[StrictBool] = Field(default=None, description="Whether the attribute can be used as a filter for the product grid in the PIM user interface")
    max_characters: Optional[StrictInt] = Field(default=None, description="Number maximum of characters allowed for the value of the attribute when the attribute type is `pim_catalog_text`, `pim_catalog_textarea` or `pim_catalog_identifier`")
    validation_rule: Optional[StrictStr] = Field(default=None, description="Validation rule type used to validate any attribute value when the attribute type is `pim_catalog_text` or `pim_catalog_identifier`")
    validation_regexp: Optional[StrictStr] = Field(default=None, description="Regexp expression used to validate any attribute value when the attribute type is `pim_catalog_text` or `pim_catalog_identifier`")
    wysiwyg_enabled: Optional[StrictBool] = Field(default=None, description="Whether the WYSIWYG interface is shown when the attribute type is `pim_catalog_textarea`")
    number_min: Optional[StrictStr] = Field(default=None, description="Minimum integer value allowed when the attribute type is `pim_catalog_metric`, `pim_catalog_price` or `pim_catalog_number`")
    number_max: Optional[StrictStr] = Field(default=None, description="Maximum integer value allowed when the attribute type is `pim_catalog_metric`, `pim_catalog_price` or `pim_catalog_number`")
    decimals_allowed: Optional[StrictBool] = Field(default=None, description="Whether decimals are allowed when the attribute type is `pim_catalog_metric`, `pim_catalog_price` or `pim_catalog_number`")
    negative_allowed: Optional[StrictBool] = Field(default=None, description="Whether negative values are allowed when the attribute type is `pim_catalog_metric` or `pim_catalog_number`")
    metric_family: Optional[StrictStr] = Field(default=None, description="Metric family when the attribute type is `pim_catalog_metric`")
    default_metric_unit: Optional[StrictStr] = Field(default=None, description="Default metric unit when the attribute type is `pim_catalog_metric`")
    date_min: Optional[datetime] = Field(default=None, description="Minimum date allowed when the attribute type is `pim_catalog_date`")
    date_max: Optional[datetime] = Field(default=None, description="Maximum date allowed when the attribute type is `pim_catalog_date`")
    allowed_extensions: Optional[List[StrictStr]] = Field(default=None, description="Extensions allowed when the attribute type is `pim_catalog_file` or `pim_catalog_image`")
    max_file_size: Optional[StrictStr] = Field(default=None, description="Max file size in MB when the attribute type is `pim_catalog_file` or `pim_catalog_image`")
    reference_data_name: Optional[StrictStr] = Field(default=None, description="Reference entity code when the attribute type is `akeneo_reference_entity` or `akeneo_reference_entity_collection` OR Asset family code when the attribute type is `pim_catalog_asset_collection`")
    default_value: Optional[StrictBool] = Field(default=None, description="Default value for a Yes/No attribute, applied when creating a new product or product model (only available since the 5.0)")
    table_configuration: Optional[List[AttributesAllOfEmbeddedItemsInnerAllOfTableConfigurationInner]] = Field(default=None, description="Configuration of the Table attribute (columns)")
    is_main_identifier: Optional[StrictBool] = Field(default=None, description="Is this attribute main identifier when attribute type is `pim_catalog_identifier`")
    __properties: ClassVar[List[str]] = ["_links", "code", "type", "labels", "group", "group_labels", "sort_order", "localizable", "scopable", "available_locales", "unique", "useable_as_grid_filter", "max_characters", "validation_rule", "validation_regexp", "wysiwyg_enabled", "number_min", "number_max", "decimals_allowed", "negative_allowed", "metric_family", "default_metric_unit", "date_min", "date_max", "allowed_extensions", "max_file_size", "reference_data_name", "default_value", "table_configuration", "is_main_identifier"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['pim_catalog_identifier', 'pim_catalog_metric', 'pim_catalog_number', 'pim_catalog_reference_data_multi_select', 'pim_catalog_reference_data_simple_select', 'pim_catalog_simpleselect', 'pim_catalog_multiselect', 'pim_catalog_date', 'pim_catalog_textarea', 'pim_catalog_text', 'pim_catalog_file', 'pim_catalog_image', 'pim_catalog_price_collection', 'pim_catalog_boolean', 'akeneo_reference_entity', 'akeneo_reference_entity_collection', 'pim_catalog_asset_collection']):
            raise ValueError("must be one of enum values ('pim_catalog_identifier', 'pim_catalog_metric', 'pim_catalog_number', 'pim_catalog_reference_data_multi_select', 'pim_catalog_reference_data_simple_select', 'pim_catalog_simpleselect', 'pim_catalog_multiselect', 'pim_catalog_date', 'pim_catalog_textarea', 'pim_catalog_text', 'pim_catalog_file', 'pim_catalog_image', 'pim_catalog_price_collection', 'pim_catalog_boolean', 'akeneo_reference_entity', 'akeneo_reference_entity_collection', 'pim_catalog_asset_collection')")
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
        """Create an instance of AttributeList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of group_labels
        if self.group_labels:
            _dict['group_labels'] = self.group_labels.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in table_configuration (list)
        _items = []
        if self.table_configuration:
            for _item in self.table_configuration:
                if _item:
                    _items.append(_item.to_dict())
            _dict['table_configuration'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AttributeList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_links": ProductsAllOfEmbeddedItemsInnerAllOfLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "code": obj.get("code"),
            "type": obj.get("type"),
            "labels": AttributesAllOfEmbeddedItemsInnerAllOfLabels.from_dict(obj["labels"]) if obj.get("labels") is not None else None,
            "group": obj.get("group"),
            "group_labels": AttributesAllOfEmbeddedItemsInnerAllOfGroupLabels.from_dict(obj["group_labels"]) if obj.get("group_labels") is not None else None,
            "sort_order": obj.get("sort_order"),
            "localizable": obj.get("localizable") if obj.get("localizable") is not None else False,
            "scopable": obj.get("scopable") if obj.get("scopable") is not None else False,
            "available_locales": obj.get("available_locales"),
            "unique": obj.get("unique"),
            "useable_as_grid_filter": obj.get("useable_as_grid_filter"),
            "max_characters": obj.get("max_characters"),
            "validation_rule": obj.get("validation_rule"),
            "validation_regexp": obj.get("validation_regexp"),
            "wysiwyg_enabled": obj.get("wysiwyg_enabled"),
            "number_min": obj.get("number_min"),
            "number_max": obj.get("number_max"),
            "decimals_allowed": obj.get("decimals_allowed"),
            "negative_allowed": obj.get("negative_allowed"),
            "metric_family": obj.get("metric_family"),
            "default_metric_unit": obj.get("default_metric_unit"),
            "date_min": obj.get("date_min"),
            "date_max": obj.get("date_max"),
            "allowed_extensions": obj.get("allowed_extensions"),
            "max_file_size": obj.get("max_file_size"),
            "reference_data_name": obj.get("reference_data_name"),
            "default_value": obj.get("default_value"),
            "table_configuration": [AttributesAllOfEmbeddedItemsInnerAllOfTableConfigurationInner.from_dict(_item) for _item in obj["table_configuration"]] if obj.get("table_configuration") is not None else None,
            "is_main_identifier": obj.get("is_main_identifier")
        })
        return _obj


