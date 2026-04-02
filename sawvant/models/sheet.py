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
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from sawvant.models.grain_direction import GrainDirection
from sawvant.models.margins import Margins
from typing import Optional, Set
from typing_extensions import Self

class Sheet(BaseModel):
    """
    Sheet
    """ # noqa: E501
    id: StrictStr
    length: Union[StrictFloat, StrictInt] = Field(description="Length in mm")
    width: Union[StrictFloat, StrictInt] = Field(description="Width in mm")
    quantity: Annotated[int, Field(strict=True, ge=0)] = Field(description="0 = unlimited")
    grain: GrainDirection
    is_offcut: Optional[StrictBool] = Field(default=False, description="Offcut sheets are prioritized by the solver")
    trim_margins: Optional[Margins] = None
    article_number: Optional[StrictStr] = Field(default=None, description="Optional article/SKU reference for this sheet type")
    __properties: ClassVar[List[str]] = ["id", "length", "width", "quantity", "grain", "is_offcut", "trim_margins", "article_number"]

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
        """Create an instance of Sheet from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of trim_margins
        if self.trim_margins:
            _dict['trim_margins'] = self.trim_margins.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Sheet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "length": obj.get("length"),
            "width": obj.get("width"),
            "quantity": obj.get("quantity"),
            "grain": obj.get("grain"),
            "is_offcut": obj.get("is_offcut") if obj.get("is_offcut") is not None else False,
            "trim_margins": Margins.from_dict(obj["trim_margins"]) if obj.get("trim_margins") is not None else None,
            "article_number": obj.get("article_number")
        })
        return _obj


