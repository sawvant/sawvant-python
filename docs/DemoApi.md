# sawvant.DemoApi

All URIs are relative to *https://api.sawvant.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_demo_optimization**](DemoApi.md#create_demo_optimization) | **POST** /v1/demo/optimize | Run a small optimization without an API key


# **create_demo_optimization**
> DemoOptimizeResponse create_demo_optimization(optimize_request)

Run a small optimization without an API key

Public endpoint behind the playground on sawvant.com. No API key or
account needed. Runs the fast strategy synchronously and returns the
result together with an SVG cutting plan per layout, so there is no
job to poll.

Limits: at most 30 part types, a total part quantity of 100, 3 sheet
types and a 64 KB request body. `strategy` must be omitted or `fast`;
`cost_tariffs` is ignored. Each client IP may make 10 requests per
minute and 100 per day. The input is not stored.

Browsers may only call this endpoint from sawvant.com.


### Example


```python
import sawvant
from sawvant.models.demo_optimize_response import DemoOptimizeResponse
from sawvant.models.optimize_request import OptimizeRequest
from sawvant.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sawvant.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sawvant.Configuration(
    host = "https://api.sawvant.com"
)


# Enter a context with an instance of the API client
with sawvant.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sawvant.DemoApi(api_client)
    optimize_request = {"parts":[{"id":"side","length":720,"width":560,"quantity":2,"grain":"length"},{"id":"shelf","length":564,"width":540,"quantity":3,"grain":"none"},{"id":"door","length":716,"width":396,"quantity":2,"grain":"length"}],"sheets":[{"id":"oak-18","length":2800,"width":2070,"quantity":0,"grain":"length"}],"machine":{"blade_thickness":3.2,"max_levels":3,"cut_direction":"default"}} # OptimizeRequest | 

    try:
        # Run a small optimization without an API key
        api_response = api_instance.create_demo_optimization(optimize_request)
        print("The response of DemoApi->create_demo_optimization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemoApi->create_demo_optimization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optimize_request** | [**OptimizeRequest**](OptimizeRequest.md)|  | 

### Return type

[**DemoOptimizeResponse**](DemoOptimizeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Optimization result with an SVG per layout |  -  |
**400** | Malformed JSON or a field that fails validation |  -  |
**413** | Request body larger than 64 KB |  -  |
**422** | Over a demo limit (&#x60;DEMO_LIMIT_EXCEEDED&#x60;) or infeasible input such as a part larger than every sheet (&#x60;INFEASIBLE&#x60;)  |  -  |
**429** | Too many demo requests from this IP. See &#x60;Retry-After&#x60;. |  * Retry-After - Seconds to wait before retrying <br>  |
**500** | Unexpected server error (&#x60;INTERNAL_ERROR&#x60;) |  -  |
**503** | Too many demo runs in progress, or the server was too busy to finish the solve in time (&#x60;DEMO_BUSY&#x60;). Retry after a few seconds. |  * Retry-After - Seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

