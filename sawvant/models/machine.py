# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from sawvant.models.cut_direction import CutDirection
from typing import Optional, Set
from typing_extensions import Self

class Machine(BaseModel):
    """
    Machine
    """ # noqa: E501
    blade_thickness: Union[StrictFloat, StrictInt] = Field(description="Kerf width in mm")
    max_levels: Annotated[int, Field(le=3, strict=True, ge=1)] = Field(description="Cut pattern complexity (1-3)")
    max_stack_height: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Maximum stack height in mm for batch cutting")
    cut_direction: CutDirection
    __properties: ClassVar[List[str]] = ["blade_thickness", "max_levels", "max_stack_height", "cut_direction"]

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
        """Create an instance of Machine from a JSON string"""
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
        """Create an instance of Machine from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "blade_thickness": obj.get("blade_thickness"),
            "max_levels": obj.get("max_levels"),
            "max_stack_height": obj.get("max_stack_height"),
            "cut_direction": obj.get("cut_direction")
        })
        return _obj


