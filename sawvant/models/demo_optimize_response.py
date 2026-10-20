# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from sawvant.models.demo_layout import DemoLayout
from sawvant.models.metrics import Metrics
from sawvant.models.summary import Summary
from typing import Optional, Set
from typing_extensions import Self

class DemoOptimizeResponse(BaseModel):
    """
    DemoOptimizeResponse
    """ # noqa: E501
    layouts: List[DemoLayout]
    summary: Summary
    metrics: Metrics
    __properties: ClassVar[List[str]] = ["layouts", "summary", "metrics"]

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
        """Create an instance of DemoOptimizeResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in layouts (list)
        _items = []
        if self.layouts:
            for _item_layouts in self.layouts:
                if _item_layouts:
                    _items.append(_item_layouts.to_dict())
            _dict['layouts'] = _items
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metrics
        if self.metrics:
            _dict['metrics'] = self.metrics.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DemoOptimizeResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "layouts": [DemoLayout.from_dict(_item) for _item in obj["layouts"]] if obj.get("layouts") is not None else None,
            "summary": Summary.from_dict(obj["summary"]) if obj.get("summary") is not None else None,
            "metrics": Metrics.from_dict(obj["metrics"]) if obj.get("metrics") is not None else None
        })
        return _obj


