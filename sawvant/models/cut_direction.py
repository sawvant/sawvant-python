# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CutDirection(str, Enum):
    """
    CutDirection
    """

    """
    allowed enum values
    """
    DEFAULT = 'default'
    RIP = 'rip'
    CROSS = 'cross'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CutDirection from a JSON string"""
        return cls(json.loads(json_str))


