# coding: utf-8

"""
Sawvant Cutting Optimization API — Python SDK

File generated from our OpenAPI spec; DO NOT EDIT.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ErrorCode(str, Enum):
    """
    Stable, machine-readable error code. New codes may be added.
    """

    """
    allowed enum values
    """
    INVALID_BODY = 'INVALID_BODY'
    BODY_TOO_LARGE = 'BODY_TOO_LARGE'
    INVALID_JSON = 'INVALID_JSON'
    INVALID_STRATEGY = 'INVALID_STRATEGY'
    PARTS_EMPTY = 'PARTS_EMPTY'
    SHEETS_EMPTY = 'SHEETS_EMPTY'
    TOO_MANY_PARTS = 'TOO_MANY_PARTS'
    TOO_MANY_SHEETS = 'TOO_MANY_SHEETS'
    VALIDATION_FAILED = 'VALIDATION_FAILED'
    INFEASIBLE = 'INFEASIBLE'
    INTERNAL_ERROR = 'INTERNAL_ERROR'
    SERVICE_UNAVAILABLE = 'SERVICE_UNAVAILABLE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ErrorCode from a JSON string"""
        return cls(json.loads(json_str))


