# OptimizeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parts** | [**List[Part]**](Part.md) |  | 
**sheets** | [**List[Sheet]**](Sheet.md) |  | 
**machine** | [**Machine**](Machine.md) |  | 
**strategy** | **str** | Solve strategy. \&quot;fast\&quot; runs all greedy solvers concurrently. \&quot;thorough\&quot; adds Gilmore-Gomory column generation for optimal patterns. Each strategy has its own rate limit quota.  | [optional] [default to 'fast']
**cost_tariffs** | [**CostTariffs**](CostTariffs.md) |  | [optional] 

## Example

```python
from sawvant.models.optimize_request import OptimizeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizeRequest from a JSON string
optimize_request_instance = OptimizeRequest.from_json(json)
# print the JSON string representation of the object
print(OptimizeRequest.to_json())

# convert the object into a dict
optimize_request_dict = optimize_request_instance.to_dict()
# create an instance of OptimizeRequest from a dict
optimize_request_from_dict = OptimizeRequest.from_dict(optimize_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


