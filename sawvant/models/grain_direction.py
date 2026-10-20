# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class GrainDirection(str, Enum):
    """
    Which axis the grain runs along. On a part it is relative to the part's own length and width; on a sheet it is relative to the sheet's. A part may only be placed so that its grain ends up parallel to the sheet's. A sheet that omits the field is treated as having its grain along its length, so `length` and `width` on a part constrain rotation even when the sheet says nothing. Use `none` on the part for material without a grain, or `free_same` to let the solver choose one orientation and apply it to every instance of that part.
    """

    """
    allowed enum values
    """
    NONE = 'none'
    LENGTH = 'length'
    WIDTH = 'width'
    FREE_SAME = 'free_same'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GrainDirection from a JSON string"""
        return cls(json.loads(json_str))


