# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sawvant.models.batch_job_result import BatchJobResult
from typing import Optional, Set
from typing_extensions import Self

class BatchAccepted(BaseModel):
    """
    BatchAccepted
    """ # noqa: E501
    batch_id: StrictStr
    job_ids: List[StrictStr]
    total: StrictInt = Field(description="Number of jobs in the request")
    created: StrictInt = Field(description="Number of jobs successfully enqueued")
    results: Optional[List[BatchJobResult]] = Field(default=None, description="Present only when one or more jobs failed to enqueue")
    __properties: ClassVar[List[str]] = ["batch_id", "job_ids", "total", "created", "results"]

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
        """Create an instance of BatchAccepted from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item_results in self.results:
                if _item_results:
                    _items.append(_item_results.to_dict())
            _dict['results'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BatchAccepted from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "batch_id": obj.get("batch_id"),
            "job_ids": obj.get("job_ids"),
            "total": obj.get("total"),
            "created": obj.get("created"),
            "results": [BatchJobResult.from_dict(_item) for _item in obj["results"]] if obj.get("results") is not None else None
        })
        return _obj


