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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.media_files_all_of_embedded_items_inner_all_of_links import MediaFilesAllOfEmbeddedItemsInnerAllOfLinks
from typing import Optional, Set
from typing_extensions import Self

class MediaFilesAllOfEmbeddedItemsInner(BaseModel):
    """
    MediaFilesAllOfEmbeddedItemsInner
    """ # noqa: E501
    links: Optional[MediaFilesAllOfEmbeddedItemsInnerAllOfLinks] = Field(default=None, alias="_links")
    code: Optional[StrictStr] = Field(default=None, description="Media file code")
    original_filename: Optional[StrictStr] = Field(default=None, description="Original filename of the media file")
    mime_type: Optional[StrictStr] = Field(default=None, description="Mime type of the media file")
    size: Optional[StrictInt] = Field(default=None, description="Size of the media file")
    extension: Optional[StrictStr] = Field(default=None, description="Extension of the media file")
    __properties: ClassVar[List[str]] = ["_links", "code", "original_filename", "mime_type", "size", "extension"]

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
        """Create an instance of MediaFilesAllOfEmbeddedItemsInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MediaFilesAllOfEmbeddedItemsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_links": MediaFilesAllOfEmbeddedItemsInnerAllOfLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "code": obj.get("code"),
            "original_filename": obj.get("original_filename"),
            "mime_type": obj.get("mime_type"),
            "size": obj.get("size"),
            "extension": obj.get("extension")
        })
        return _obj

