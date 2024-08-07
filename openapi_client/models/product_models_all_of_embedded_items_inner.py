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
from openapi_client.models.product_models_all_of_embedded_items_inner_all_of_associations import ProductModelsAllOfEmbeddedItemsInnerAllOfAssociations
from openapi_client.models.product_models_all_of_embedded_items_inner_all_of_metadata import ProductModelsAllOfEmbeddedItemsInnerAllOfMetadata
from openapi_client.models.product_models_all_of_embedded_items_inner_all_of_quantified_associations import ProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociations
from openapi_client.models.product_models_all_of_embedded_items_inner_all_of_values import ProductModelsAllOfEmbeddedItemsInnerAllOfValues
from openapi_client.models.products_all_of_embedded_items_inner_all_of_links import ProductsAllOfEmbeddedItemsInnerAllOfLinks
from typing import Optional, Set
from typing_extensions import Self

class ProductModelsAllOfEmbeddedItemsInner(BaseModel):
    """
    ProductModelsAllOfEmbeddedItemsInner
    """ # noqa: E501
    links: Optional[ProductsAllOfEmbeddedItemsInnerAllOfLinks] = Field(default=None, alias="_links")
    code: StrictStr = Field(description="Product model code")
    family: Optional[StrictStr] = Field(default=None, description="<a href='api-reference.html#Family'>Family</a> code  from which the product inherits its attributes and attributes requirements (since the 3.2)")
    family_variant: StrictStr = Field(description="Family variant code from which the product model inherits its attributes and variant attributes")
    parent: Optional[StrictStr] = Field(default=None, description="Code of the parent <a href='api-reference.html#Productmodel'>product model</a>. This parent can be modified since the 2.3.")
    categories: Optional[List[StrictStr]] = Field(default=None, description="Codes of the <a href='api-reference.html#Category'>categories</a> in which the product model is categorized")
    values: Optional[ProductModelsAllOfEmbeddedItemsInnerAllOfValues] = None
    associations: Optional[ProductModelsAllOfEmbeddedItemsInnerAllOfAssociations] = None
    quantified_associations: Optional[ProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociations] = None
    created: Optional[StrictStr] = Field(default=None, description="Date of creation")
    updated: Optional[StrictStr] = Field(default=None, description="Date of the last update")
    metadata: Optional[ProductModelsAllOfEmbeddedItemsInnerAllOfMetadata] = None
    quality_scores: Optional[Dict[str, Any]] = Field(default=None, description="Product model quality scores for each channel/locale combination (<strong>only available since the 7.0 version</strong> and when the \"with_quality_scores\" query parameter is set to \"true\")")
    __properties: ClassVar[List[str]] = ["_links", "code", "family", "family_variant", "parent", "categories", "values", "associations", "quantified_associations", "created", "updated", "metadata", "quality_scores"]

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
        """Create an instance of ProductModelsAllOfEmbeddedItemsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of values
        if self.values:
            _dict['values'] = self.values.to_dict()
        # override the default output from pydantic by calling `to_dict()` of associations
        if self.associations:
            _dict['associations'] = self.associations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quantified_associations
        if self.quantified_associations:
            _dict['quantified_associations'] = self.quantified_associations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProductModelsAllOfEmbeddedItemsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_links": ProductsAllOfEmbeddedItemsInnerAllOfLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "code": obj.get("code"),
            "family": obj.get("family"),
            "family_variant": obj.get("family_variant"),
            "parent": obj.get("parent"),
            "categories": obj.get("categories"),
            "values": ProductModelsAllOfEmbeddedItemsInnerAllOfValues.from_dict(obj["values"]) if obj.get("values") is not None else None,
            "associations": ProductModelsAllOfEmbeddedItemsInnerAllOfAssociations.from_dict(obj["associations"]) if obj.get("associations") is not None else None,
            "quantified_associations": ProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociations.from_dict(obj["quantified_associations"]) if obj.get("quantified_associations") is not None else None,
            "created": obj.get("created"),
            "updated": obj.get("updated"),
            "metadata": ProductModelsAllOfEmbeddedItemsInnerAllOfMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "quality_scores": obj.get("quality_scores")
        })
        return _obj


