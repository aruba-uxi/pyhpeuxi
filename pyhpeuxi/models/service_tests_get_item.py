#
# Copyright 2025 Hewlett Packard Enterprise Development LP.
#

# coding: utf-8

"""
    HPE Aruba Networking UXI Configuration

    This document outlines the API contracts for HPE Aruba Networking UXI.

    The version of the OpenAPI document: 6.5.0
    Contact: support@capenetworks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ServiceTestsGetItem(BaseModel):
    """
    ServiceTestsGetItem
    """ # noqa: E501
    id: StrictStr = Field(description="The unique identifier of the service test")
    category: StrictStr = Field(description="The category of the service test")
    name: StrictStr = Field(description="The name of the service test")
    target: Optional[StrictStr]
    template: StrictStr = Field(description="The template of the service test")
    is_enabled: StrictBool = Field(description="Indicates if the service test is enabled", alias="isEnabled")
    type: StrictStr = Field(description="The type of the resource.")
    __properties: ClassVar[List[str]] = ["id", "category", "name", "target", "template", "isEnabled", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['networking-uxi/service-test']):
            raise ValueError("must be one of enum values ('networking-uxi/service-test')")
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
        """Create an instance of ServiceTestsGetItem from a JSON string"""
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
        # set to None if target (nullable) is None
        # and model_fields_set contains the field
        if self.target is None and "target" in self.model_fields_set:
            _dict['target'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceTestsGetItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "category": obj.get("category"),
            "name": obj.get("name"),
            "target": obj.get("target"),
            "template": obj.get("template"),
            "isEnabled": obj.get("isEnabled"),
            "type": obj.get("type")
        })
        return _obj


