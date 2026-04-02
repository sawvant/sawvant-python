# sawvant.JobsApi

All URIs are relative to *https://api.sawvant.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job**](JobsApi.md#get_job) | **GET** /v1/jobs/{id} | Get job status
[**stream_job**](JobsApi.md#stream_job) | **GET** /v1/jobs/{id}/stream | Stream job progress via SSE


# **get_job**
> JobResponse get_job(id)

Get job status

Returns the current state of a job including progress, result, and errors.

### Example

* Api Key Authentication (apiKey):

```python
import sawvant
from sawvant.models.job_response import JobResponse
from sawvant.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sawvant.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sawvant.Configuration(
    host = "https://api.sawvant.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with sawvant.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sawvant.JobsApi(api_client)
    id = 'id_example' # str | Job UUID

    try:
        # Get job status
        api_response = api_instance.get_job(id)
        print("The response of JobsApi->get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job UUID | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job found |  -  |
**400** | Invalid job ID format |  -  |
**401** | Missing or invalid API key |  -  |
**404** | Job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_job**
> str stream_job(id)

Stream job progress via SSE

Server-Sent Events stream that emits `progress`, `completed`, or `failed` events.
The stream closes automatically when the job reaches a terminal state.

A `: heartbeat` comment is sent every 30 seconds to keep the connection alive
through proxies and load balancers. SSE clients ignore these automatically.


### Example

* Api Key Authentication (apiKey):

```python
import sawvant
from sawvant.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sawvant.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sawvant.Configuration(
    host = "https://api.sawvant.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with sawvant.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sawvant.JobsApi(api_client)
    id = 'id_example' # str | Job UUID

    try:
        # Stream job progress via SSE
        api_response = api_instance.stream_job(id)
        print("The response of JobsApi->stream_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->stream_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job UUID | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSE event stream |  -  |
**400** | Invalid job ID format |  -  |
**401** | Missing or invalid API key |  -  |
**404** | Job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

