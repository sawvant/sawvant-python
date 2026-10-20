# sawvant.JobsApi

All URIs are relative to *https://api.sawvant.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job**](JobsApi.md#get_job) | **GET** /v1/jobs/{id} | Get job status
[**get_job_diagram_pdf**](JobsApi.md#get_job_diagram_pdf) | **GET** /v1/jobs/{id}/diagram.pdf | Render a cutting plan as PDF
[**get_job_diagram_svg**](JobsApi.md#get_job_diagram_svg) | **GET** /v1/jobs/{id}/diagram | Render a cutting plan as SVG
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

# **get_job_diagram_pdf**
> bytearray get_job_diagram_pdf(id)

Render a cutting plan as PDF

Returns every sheet layout of a completed job as a printable PDF
cutting plan.


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
        # Render a cutting plan as PDF
        api_response = api_instance.get_job_diagram_pdf(id)
        print("The response of JobsApi->get_job_diagram_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_diagram_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job UUID | 

### Return type

**bytearray**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PDF cutting plan |  -  |
**400** | Invalid job ID |  -  |
**401** | Missing or invalid API key |  -  |
**404** | Job not found |  -  |
**422** | Job is not completed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_diagram_svg**
> str get_job_diagram_svg(id, sheet=sheet)

Render a cutting plan as SVG

Returns one sheet layout of a completed job as an SVG cutting plan with
dimensions and grain direction.


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
    sheet = 0 # int | Index into the job's `layouts` array (optional) (default to 0)

    try:
        # Render a cutting plan as SVG
        api_response = api_instance.get_job_diagram_svg(id, sheet=sheet)
        print("The response of JobsApi->get_job_diagram_svg:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_diagram_svg: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job UUID | 
 **sheet** | **int**| Index into the job&#39;s &#x60;layouts&#x60; array | [optional] [default to 0]

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/svg+xml, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SVG cutting plan |  -  |
**400** | Invalid job ID or sheet index |  -  |
**401** | Missing or invalid API key |  -  |
**404** | Job not found |  -  |
**422** | Job is not completed, or has no layouts |  -  |

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

