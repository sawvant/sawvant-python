# sawvant.SystemApi

All URIs are relative to *https://api.sawvant.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health**](SystemApi.md#get_health) | **GET** /health | Health check
[**list_tiers**](SystemApi.md#list_tiers) | **GET** /v1/tiers | List available subscription tiers


# **get_health**
> HealthResponse get_health()

Health check

### Example


```python
import sawvant
from sawvant.models.health_response import HealthResponse
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
    api_instance = sawvant.SystemApi(api_client)

    try:
        # Health check
        api_response = api_instance.get_health()
        print("The response of SystemApi->get_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthResponse**](HealthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service is healthy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tiers**
> List[TierDefinition] list_tiers()

List available subscription tiers

Returns all available subscription tiers with their rate limits, pricing,
and feature gates. This is the single source of truth for tier configuration.


### Example


```python
import sawvant
from sawvant.models.tier_definition import TierDefinition
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
    api_instance = sawvant.SystemApi(api_client)

    try:
        # List available subscription tiers
        api_response = api_instance.list_tiers()
        print("The response of SystemApi->list_tiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->list_tiers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TierDefinition]**](TierDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tier definitions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

