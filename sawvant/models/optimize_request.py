# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from sawvant.models.cost_tariffs import CostTariffs
from sawvant.models.machine import Machine
from sawvant.models.part import Part
from sawvant.models.sheet import Sheet
from typing import Optional, Set
from typing_extensions import Self

class OptimizeRequest(BaseModel):
    """
    OptimizeRequest
    """ # noqa: E501
    parts: Annotated[List[Part], Field(min_length=1, max_length=5000)]
    sheets: Annotated[List[Sheet], Field(min_length=1, max_length=100)]
    machine: Machine
    strategy: Optional[StrictStr] = Field(default='fast', description="Solve strategy. \"fast\" runs all greedy solvers concurrently. \"thorough\" adds Gilmore-Gomory column generation for optimal patterns. Each strategy has its own rate limit quota. ")
    cost_tariffs: Optional[CostTariffs] = None
    __properties: ClassVar[List[str]] = ["parts", "sheets", "machine", "strategy", "cost_tariffs"]

    @field_validator('strategy')
    def strategy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['fast', 'thorough']):
            raise ValueError("must be one of enum values ('fast', 'thorough')")
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
        """Create an instance of OptimizeRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in parts (list)
        _items = []
        if self.parts:
            for _item_parts in self.parts:
                if _item_parts:
                    _items.append(_item_parts.to_dict())
            _dict['parts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sheets (list)
        _items = []
        if self.sheets:
            for _item_sheets in self.sheets:
                if _item_sheets:
                    _items.append(_item_sheets.to_dict())
            _dict['sheets'] = _items
        # override the default output from pydantic by calling `to_dict()` of machine
        if self.machine:
            _dict['machine'] = self.machine.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cost_tariffs
        if self.cost_tariffs:
            _dict['cost_tariffs'] = self.cost_tariffs.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OptimizeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "parts": [Part.from_dict(_item) for _item in obj["parts"]] if obj.get("parts") is not None else None,
            "sheets": [Sheet.from_dict(_item) for _item in obj["sheets"]] if obj.get("sheets") is not None else None,
            "machine": Machine.from_dict(obj["machine"]) if obj.get("machine") is not None else None,
            "strategy": obj.get("strategy") if obj.get("strategy") is not None else 'fast',
            "cost_tariffs": CostTariffs.from_dict(obj["cost_tariffs"]) if obj.get("cost_tariffs") is not None else None
        })
        return _obj


