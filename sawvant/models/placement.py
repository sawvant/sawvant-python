# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from sawvant.models.grain_direction import GrainDirection
from typing import Optional, Set
from typing_extensions import Self

class Placement(BaseModel):
    """
    Placement
    """ # noqa: E501
    part_id: StrictStr
    sheet_id: StrictStr = Field(description="Which sheet type this part is placed on")
    x: Union[StrictFloat, StrictInt] = Field(description="mm from top-left of usable area")
    y: Union[StrictFloat, StrictInt] = Field(description="mm from top-left of usable area")
    width: Union[StrictFloat, StrictInt] = Field(description="Post-edge-banding dimension")
    height: Union[StrictFloat, StrictInt] = Field(description="Post-edge-banding dimension")
    rotated: StrictBool
    grain: GrainDirection
    __properties: ClassVar[List[str]] = ["part_id", "sheet_id", "x", "y", "width", "height", "rotated", "grain"]

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
        """Create an instance of Placement from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Placement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "part_id": obj.get("part_id"),
            "sheet_id": obj.get("sheet_id"),
            "x": obj.get("x"),
            "y": obj.get("y"),
            "width": obj.get("width"),
            "height": obj.get("height"),
            "rotated": obj.get("rotated"),
            "grain": obj.get("grain")
        })
        return _obj


