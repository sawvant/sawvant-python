# Sawvant Python SDK

The official Python client for the [Sawvant](https://sawvant.com) Cutting Optimization API.

- API version: 1.0.0
- Package version: 0.1.0
- Requires Python 3.8+

## Installation

```sh
pip install sawvant
```

## Quick Start

```python
import time

import sawvant
from sawvant import (
    CutDirection,
    GrainDirection,
    JobsApi,
    Machine,
    OptimizationApi,
    OptimizeRequest,
    Part,
    Sheet,
)

configuration = sawvant.Configuration(
    host='https://api.sawvant.com',
    api_key={'apiKey': 'sk_your_api_key_here'},
)

with sawvant.ApiClient(configuration) as client:
    optimization = OptimizationApi(client)
    jobs = JobsApi(client)

    # Submit an optimization job. Sizes are in mm.
    request = OptimizeRequest(
        sheets=[
            Sheet(id='board', length=2800, width=2070, quantity=10, grain=GrainDirection.NONE),
        ],
        parts=[
            Part(id='panel-a', length=600, width=400, quantity=10, grain=GrainDirection.NONE),
            Part(id='panel-b', length=300, width=200, quantity=20, grain=GrainDirection.NONE),
        ],
        machine=Machine(blade_thickness=4.4, max_levels=3, cut_direction=CutDirection.DEFAULT),
    )

    job = optimization.create_optimization(request)
    print('Job created:', job.job_id)

    # Poll for results
    result = jobs.get_job(job.job_id)
    while result.status in ('pending', 'running'):
        time.sleep(1)
        result = jobs.get_job(job.job_id)

    if result.status == 'completed':
        print('Optimization complete:', result.result)
    else:
        print('Job failed:', result.error)
```

## SSE Streaming

Stream real-time progress events as the job runs with `sawvant.streaming.stream_job`. The helper uses `httpx`, so install the SDK with the `streaming` extra:

```sh
pip install "sawvant[streaming]"
```

Then stream the events, passing the `job_id` that `create_optimization` returned:

```python
from sawvant.streaming import stream_job

job_id = '550e8400-e29b-41d4-a716-446655440000'

for event in stream_job(job_id, 'sk_your_api_key_here'):
    if event.type == 'progress':
        print('Progress:', event.data['progress'])
    elif event.type == 'completed':
        print('Done:', event.data['result'])
        break
    elif event.type == 'failed':
        print('Failed:', event.data.get('error'))
        break
```

`stream_job` also accepts `base_url` (default `https://api.sawvant.com`) and `timeout` in seconds. `event.data` is a plain dict with the job fields.

When a `completed` event arrives, the SDK fetches the full job via `GET /v1/jobs/{id}` and puts it in the event, so `event.data['result']` holds the complete result. The server leaves the result out of stream events to keep them small. Other events are passed on as received.

## Configuration

```python
import os

import sawvant

configuration = sawvant.Configuration(
    host='https://api.sawvant.com',
    api_key={'apiKey': os.environ['SAWVANT_API_KEY']},
    retries=3,
)
```

| Option | Description |
|--------|-------------|
| `host` | API base URL (default: `https://api.sawvant.com`) |
| `api_key` | Dictionary with an `apiKey` entry holding your `sk_...` key |
| `retries` | Number of retries for failed requests |

Every API method also takes `_request_timeout` in seconds, for example `jobs.get_job(job_id, _request_timeout=30)`.

## API Reference

All endpoints are relative to `https://api.sawvant.com`.

| Class | Method | HTTP | Path | Description |
|-------|--------|------|------|-------------|
| `OptimizationApi` | `create_optimization` | POST | `/v1/optimize` | Submit a new cutting optimization job |
| `OptimizationApi` | `create_batch_optimization` | POST | `/v1/optimize/batch` | Submit several optimization jobs at once |
| `JobsApi` | `get_job` | GET | `/v1/jobs/{id}` | Retrieve job status and result |
| `JobsApi` | `get_job_diagram_svg` | GET | `/v1/jobs/{id}/diagram` | Cutting diagram as SVG |
| `JobsApi` | `get_job_diagram_pdf` | GET | `/v1/jobs/{id}/diagram.pdf` | Cutting diagram as PDF |
| `stream_job` (from `sawvant.streaming`) | | GET | `/v1/jobs/{id}/stream` | Stream job progress via SSE |
| `SystemApi` | `get_health` | GET | `/health` | Health check (no auth required) |
| `SystemApi` | `list_tiers` | GET | `/v1/tiers` | List subscription tiers (no auth required) |

## License

Apache-2.0. See [LICENSE](LICENSE).
