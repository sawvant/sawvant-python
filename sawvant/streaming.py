"""SSE streaming client for Sawvant job progress."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Generator, Optional

import httpx


@dataclass
class StreamEvent:
    type: str  # "progress", "completed", "failed", "error"
    data: dict


def _fetch_job(job_id: str, api_key: str, base_url: str, timeout: Optional[float]) -> dict:
    """Fetch the full job result via the REST API.

    SSE events don't include the full result to avoid buffer overflow;
    fetch via REST instead.
    """
    url = f"{base_url}/v1/jobs/{job_id}"
    headers = {
        "X-API-Key": api_key,
        "Accept": "application/json",
    }
    response = httpx.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.json()


def stream_job(
    job_id: str,
    api_key: str,
    base_url: str = "https://api.sawvant.com",
    timeout: Optional[float] = None,
) -> Generator[StreamEvent, None, None]:
    """Stream job progress via Server-Sent Events.

    When a "completed" event is received, the full job result is fetched
    via the GET /v1/jobs/{id} REST endpoint. SSE events don't include the
    full result to avoid buffer overflow; the REST call retrieves the
    complete response.

    Usage:
        for event in stream_job("job-uuid", "sk_xxx"):
            print(event.type, event.data["status"])
    """
    url = f"{base_url}/v1/jobs/{job_id}/stream"
    headers = {
        "X-API-Key": api_key,
        "Accept": "text/event-stream",
    }

    with httpx.stream("GET", url, headers=headers, timeout=timeout) as response:
        response.raise_for_status()

        current_event = ""
        for line in response.iter_lines():
            if line.startswith("event:"):
                current_event = line[6:].strip()
            elif line.startswith("data:"):
                data = json.loads(line[5:].strip())

                if current_event == "completed":
                    # SSE events don't include the full result to avoid
                    # buffer overflow; fetch via REST instead.
                    data = _fetch_job(job_id, api_key, base_url, timeout)

                yield StreamEvent(type=current_event, data=data)
