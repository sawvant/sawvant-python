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
from sawvant.models.edge_correction import EdgeCorrection
from sawvant.models.grain_direction import GrainDirection
from typing import Optional, Set
from typing_extensions import Self

class Part(BaseModel):
    """
    Part
    """ # noqa: E501
    id: StrictStr
    length: Union[StrictFloat, StrictInt] = Field(description="Length in mm")
    width: Union[StrictFloat, StrictInt] = Field(description="Width in mm")
    quantity: Annotated[int, Field(strict=True, ge=1)]
    grain: GrainDirection
    edge_banding: Optional[EdgeCorrection] = None
    __properties: ClassVar[List[str]] = ["id", "length", "width", "quantity", "grain", "edge_banding"]

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
        """Create an instance of Part from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of edge_banding
        if self.edge_banding:
            _dict['edge_banding'] = self.edge_banding.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Part from a dict"""
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
            "edge_banding": EdgeCorrection.from_dict(obj["edge_banding"]) if obj.get("edge_banding") is not None else None
        })
        return _obj


