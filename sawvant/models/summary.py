# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from sawvant.models.sheet_usage import SheetUsage
from typing import Optional, Set
from typing_extensions import Self

class Summary(BaseModel):
    """
    Summary
    """ # noqa: E501
    total_sheets: StrictInt
    yield_percent: Union[Annotated[float, Field(le=100, strict=True, ge=0)], Annotated[int, Field(le=100, strict=True, ge=0)]]
    waste_percent: Union[StrictFloat, StrictInt]
    waste_area: Union[StrictFloat, StrictInt] = Field(description="mm²")
    unplaced_parts: Optional[List[StrictStr]] = None
    sheets_used: List[SheetUsage]
    __properties: ClassVar[List[str]] = ["total_sheets", "yield_percent", "waste_percent", "waste_area", "unplaced_parts", "sheets_used"]

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
        """Create an instance of Summary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in sheets_used (list)
        _items = []
        if self.sheets_used:
            for _item_sheets_used in self.sheets_used:
                if _item_sheets_used:
                    _items.append(_item_sheets_used.to_dict())
            _dict['sheets_used'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Summary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "total_sheets": obj.get("total_sheets"),
            "yield_percent": obj.get("yield_percent"),
            "waste_percent": obj.get("waste_percent"),
            "waste_area": obj.get("waste_area"),
            "unplaced_parts": obj.get("unplaced_parts"),
            "sheets_used": [SheetUsage.from_dict(_item) for _item in obj["sheets_used"]] if obj.get("sheets_used") is not None else None
        })
        return _obj


