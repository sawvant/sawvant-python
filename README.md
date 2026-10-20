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
import sawvant
from sawvant.api import optimize_api
from sawvant.model.optimize_request import OptimizeRequest
from sawvant.model.sheet import Sheet
from sawvant.model.part import Part

configuration = sawvant.Configuration(
    host='https://api.sawvant.com',
    api_key={'ApiKeyAuth': 'sk_your_api_key_here'},
)

with sawvant.ApiClient(configuration) as client:
    api = optimize_api.OptimizeApi(client)

    # Submit an optimization job
    request = OptimizeRequest(
        sheets=[
            Sheet(width=2440, height=1220, quantity=5),
        ],
        parts=[
            Part(width=600, height=400, quantity=10, label='Panel A'),
            Part(width=300, height=200, quantity=20, label='Panel B'),
        ],
    )

    job = api.create_optimization(optimize_request=request)
    print('Job created:', job.id)

    # Poll for results
    import time
    from sawvant.api import jobs_api

    jobs = jobs_api.JobsApi(client)
    result = jobs.get_job(id=job.id)

    while result.status in ('pending', 'running'):
        time.sleep(1)
        result = jobs.get_job(id=job.id)

    if result.status == 'completed':
        print('Optimization complete:', result.result)
    else:
        print('Job failed:', result.status)
```

## SSE Streaming

Stream real-time progress events as the job runs with `sawvant.streaming.stream_job`. The helper uses `httpx`, so install the SDK with the `streaming` extra:

```sh
pip install "sawvant[streaming]"
```

Then stream the events:

```python
from sawvant.streaming import stream_job

for event in stream_job(job.job_id, 'sk_your_api_key_here'):
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
configuration = sawvant.Configuration(
    host='https://api.sawvant.com',
    api_key={'ApiKeyAuth': 'sk_your_api_key_here'},
)

# Optional: set a custom timeout (seconds)
configuration.timeout = 30
```

| Option | Description |
|--------|-------------|
| `host` | API base URL (default: `https://api.sawvant.com`) |
| `api_key` | Dictionary with `ApiKeyAuth` key containing your `sk_...` token |
| `timeout` | Request timeout in seconds |

## API Reference

All endpoints are relative to `https://api.sawvant.com`.

| Method | HTTP | Path | Description |
|--------|------|------|-------------|
| `create_optimization` | POST | `/v1/optimize` | Submit a new cutting optimization job |
| `get_job` | GET | `/v1/jobs/{id}` | Retrieve job status and result |
| `stream_job` | GET | `/v1/jobs/{id}/stream` | Stream job progress via SSE |
| `get_health` | GET | `/health` | Health check (no auth required) |

## License

MIT
