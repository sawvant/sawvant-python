# sawvant.OptimizationApi

All URIs are relative to *https://api.sawvant.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_optimization**](OptimizationApi.md#create_optimization) | **POST** /v1/optimize | Submit a cutting optimization job


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
    optimize_request = sawvant.OptimizeRequest() # OptimizeRequest | 

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
**400** | Invalid request (malformed JSON, missing fields, validation error) |  -  |
**401** | Missing or invalid API key |  -  |
**403** | API key revoked |  -  |
**422** | Request is valid but infeasible (e.g. part larger than all sheets) |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

