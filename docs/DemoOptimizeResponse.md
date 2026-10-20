# DemoOptimizeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layouts** | [**List[DemoLayout]**](DemoLayout.md) |  | 
**summary** | [**Summary**](Summary.md) |  | 
**metrics** | [**Metrics**](Metrics.md) |  | 

## Example

```python
from sawvant.models.demo_optimize_response import DemoOptimizeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DemoOptimizeResponse from a JSON string
demo_optimize_response_instance = DemoOptimizeResponse.from_json(json)
# print the JSON string representation of the object
print(DemoOptimizeResponse.to_json())

# convert the object into a dict
demo_optimize_response_dict = demo_optimize_response_instance.to_dict()
# create an instance of DemoOptimizeResponse from a dict
demo_optimize_response_from_dict = DemoOptimizeResponse.from_dict(demo_optimize_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


