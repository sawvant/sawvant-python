# sawvant.OptimizationApi

All URIs are relative to *https://api.sawvant.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_batch_optimization**](OptimizationApi.md#create_batch_optimization) | **POST** /v1/optimize/batch | Submit multiple cutting optimization jobs
[**create_optimization**](OptimizationApi.md#create_optimization) | **POST** /v1/optimize | Submit a cutting optimization job


# **create_batch_optimization**
> BatchAccepted create_batch_optimization(batch_request)

Submit multiple cutting optimization jobs

Enqueues an array of optimization requests as individual jobs and returns
their IDs immediately. Poll or stream each job separately.

Maximum 50 fast jobs or 10 thorough jobs per batch. Requires a tier with
the `batch` feature.


### Example

* Api Key Authentication (apiKey):

```python
import sawvant
from sawvant.models.batch_accepted import BatchAccepted
from sawvant.models.batch_request import BatchRequest
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
    api_instance = sawvant.OptimizationApi(api_client)
    batch_request = sawvant.BatchRequest() # BatchRequest | 

    try:
        # Submit multiple cutting optimization jobs
        api_response = api_instance.create_batch_optimization(batch_request)
        print("The response of OptimizationApi->create_batch_optimization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationApi->create_batch_optimization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_request** | [**BatchRequest**](BatchRequest.md)|  | 

### Return type

[**BatchAccepted**](BatchAccepted.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Batch accepted; jobs queued |  -  |
**400** | Invalid request (malformed JSON, empty batch, batch too large) |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Tier does not include batch optimization |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_optimization**
> OptimizeAccepted create_optimization(optimize_request)

Submit a cutting optimization job

Validates the request synchronously, then enqueues the job for async processing.
Returns 202 with a job ID and URLs for polling/streaming.


### Example

* Api Key Authentication (apiKey):

```python
import sawvant
from sawvant.models.optimize_accepted import OptimizeAccepted
from sawvant.models.optimize_request import OptimizeRequest
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
    api_instance = sawvant.OptimizationApi(api_client)
    optimize_request = {"parts":[{"id":"shelf","length":600,"width":400,"quantity":8,"grain":"none"},{"id":"bracket","length":300,"width":200,"quantity":4,"grain":"none"}],"sheets":[{"id":"mdf-18","length":2440,"width":1220,"quantity":0,"grain":"none"}],"machine":{"blade_thickness":3.2,"max_levels":3,"cut_direction":"default"}} # OptimizeRequest | 

    try:
        # Submit a cutting optimization job
        api_response = api_instance.create_optimization(optimize_request)
        print("The response of OptimizationApi->create_optimization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationApi->create_optimization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optimize_request** | [**OptimizeRequest**](OptimizeRequest.md)|  | 

### Return type

[**OptimizeAccepted**](OptimizeAccepted.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Job accepted and queued |  -  |
**400** | Invalid request. &#x60;error.code&#x60; says what is wrong: &#x60;INVALID_BODY&#x60;, &#x60;BODY_TOO_LARGE&#x60;, &#x60;INVALID_JSON&#x60;, &#x60;INVALID_STRATEGY&#x60;, &#x60;PARTS_EMPTY&#x60;, &#x60;SHEETS_EMPTY&#x60;, &#x60;TOO_MANY_PARTS&#x60;, &#x60;TOO_MANY_SHEETS&#x60; or &#x60;VALIDATION_FAILED&#x60;. For &#x60;INVALID_JSON&#x60; and &#x60;VALIDATION_FAILED&#x60;, &#x60;error.details&#x60; names the offending field.  |  -  |
**401** | Missing or invalid API key |  -  |
**403** | API key revoked |  -  |
**422** | Request is valid but infeasible (&#x60;INFEASIBLE&#x60;): one or more parts do not fit on any sheet. &#x60;error.details&#x60; has one entry per part.  |  -  |
**500** | Internal error (&#x60;INTERNAL_ERROR&#x60;) |  -  |
**503** | Rate limiting is temporarily unavailable (&#x60;SERVICE_UNAVAILABLE&#x60;) |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

