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
from openapi_client.models.products1_all_of_embedded_items_inner_all_of_associations import Products1AllOfEmbeddedItemsInnerAllOfAssociations
from openapi_client.models.products1_all_of_embedded_items_inner_all_of_quantified_associations import Products1AllOfEmbeddedItemsInnerAllOfQuantifiedAssociations
from openapi_client.models.products_all_of_embedded_items_inner_all_of_completenesses_inner import ProductsAllOfEmbeddedItemsInnerAllOfCompletenessesInner
from openapi_client.models.products_all_of_embedded_items_inner_all_of_metadata import ProductsAllOfEmbeddedItemsInnerAllOfMetadata
from typing import Optional, Set
from typing_extensions import Self

class Product(BaseModel):
    """
    Product
    """ # noqa: E501
    uuid: Optional[StrictStr] = Field(default=None, description="Product UUID")
    identifier: StrictStr = Field(description="Product identifier, i.e. the value of the only `pim_catalog_identifier` attribute")
    enabled: Optional[StrictBool] = Field(default=True, description="Whether the product is enabled")
    family: Optional[StrictStr] = Field(default='null only in the case of a non variant product', description="<a href='api-reference.html#Family'>Family</a> code from which the product inherits its attributes and attributes requirements.")
    categories: Optional[List[StrictStr]] = Field(default=None, description="Codes of the <a href='api-reference.html#Category'>categories</a> in which the product is classified")
    groups: Optional[List[StrictStr]] = Field(default=None, description="Codes of the groups to which the product belong")
    parent: Optional[StrictStr] = Field(default='null', description="Code of the parent <a href='api-reference.html#Productmodel'>product model</a> when the product is a variant (only available since the 2.0). This parent can be modified since the 2.3.")
    values: Optional[Dict[str, List[Dict[str, Any]]]] = Field(default=None, description="Product attributes values, see <a href='/concepts/products.html#focus-on-the-product-values'>Product values</a> section for more details")
    associations: Optional[Products1AllOfEmbeddedItemsInnerAllOfAssociations] = None
    quantified_associations: Optional[Products1AllOfEmbeddedItemsInnerAllOfQuantifiedAssociations] = None
    created: Optional[StrictStr] = Field(default=None, description="Date of creation")
    updated: Optional[StrictStr] = Field(default=None, description="Date of the last update")
    metadata: Optional[ProductsAllOfEmbeddedItemsInnerAllOfMetadata] = None
    quality_scores: Optional[Dict[str, Any]] = Field(default=None, description="Product quality scores for each channel/locale combination (only available since the 5.0 and when the \"with_quality_scores\" query parameter is set to \"true\")")
    completenesses: Optional[List[ProductsAllOfEmbeddedItemsInnerAllOfCompletenessesInner]] = Field(default=None, description="Product completenesses for each channel/locale combination (only available since the 7.0 version, and when the \"with_completenesses\" query parameter is set to \"true\")")
    __properties: ClassVar[List[str]] = ["uuid", "identifier", "enabled", "family", "categories", "groups", "parent", "values", "associations", "quantified_associations", "created", "updated", "metadata", "quality_scores", "completenesses"]

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
        """Create an instance of Product from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of associations
        if self.associations:
            _dict['associations'] = self.associations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quantified_associations
        if self.quantified_associations:
            _dict['quantified_associations'] = self.quantified_associations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in completenesses (list)
        _items = []
        if self.completenesses:
            for _item in self.completenesses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['completenesses'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Product from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "identifier": obj.get("identifier"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else True,
            "family": obj.get("family") if obj.get("family") is not None else 'null only in the case of a non variant product',
            "categories": obj.get("categories"),
            "groups": obj.get("groups"),
            "parent": obj.get("parent") if obj.get("parent") is not None else 'null',
            "values": obj.get("values"),
            "associations": Products1AllOfEmbeddedItemsInnerAllOfAssociations.from_dict(obj["associations"]) if obj.get("associations") is not None else None,
            "quantified_associations": Products1AllOfEmbeddedItemsInnerAllOfQuantifiedAssociations.from_dict(obj["quantified_associations"]) if obj.get("quantified_associations") is not None else None,
            "created": obj.get("created"),
            "updated": obj.get("updated"),
            "metadata": ProductsAllOfEmbeddedItemsInnerAllOfMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "quality_scores": obj.get("quality_scores"),
            "completenesses": [ProductsAllOfEmbeddedItemsInnerAllOfCompletenessesInner.from_dict(_item) for _item in obj["completenesses"]] if obj.get("completenesses") is not None else None
        })
        return _obj


