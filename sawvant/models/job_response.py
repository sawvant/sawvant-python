# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from sawvant.models.optimize_result import OptimizeResult
from typing import Optional, Set
from typing_extensions import Self

class JobResponse(BaseModel):
    """
    JobResponse
    """ # noqa: E501
    job_id: StrictStr
    status: StrictStr
    progress: Annotated[int, Field(le=100, strict=True, ge=0)]
    created_at: datetime
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    result: Optional[OptimizeResult] = None
    warnings: Optional[List[StrictStr]] = Field(default=None, description="E.g. unplaced part IDs")
    error: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["job_id", "status", "progress", "created_at", "started_at", "completed_at", "result", "warnings", "error"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['pending', 'running', 'completed', 'failed']):
            raise ValueError("must be one of enum values ('pending', 'running', 'completed', 'failed')")
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
        """Create an instance of JobResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of result
        if self.result:
            _dict['result'] = self.result.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JobResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "job_id": obj.get("job_id"),
            "status": obj.get("status"),
            "progress": obj.get("progress"),
            "created_at": obj.get("created_at"),
            "started_at": obj.get("started_at"),
            "completed_at": obj.get("completed_at"),
            "result": OptimizeResult.from_dict(obj["result"]) if obj.get("result") is not None else None,
            "warnings": obj.get("warnings"),
            "error": obj.get("error")
        })
        return _obj


