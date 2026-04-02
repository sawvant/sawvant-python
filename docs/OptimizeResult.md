# OptimizeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layouts** | [**List[Layout]**](Layout.md) |  | 
**summary** | [**Summary**](Summary.md) |  | 
**metrics** | [**Metrics**](Metrics.md) |  | [optional] 
**cost** | [**Cost**](Cost.md) |  | [optional] 

## Example

```python
from sawvant.models.optimize_result import OptimizeResult

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizeResult from a JSON string
optimize_result_instance = OptimizeResult.from_json(json)
# print the JSON string representation of the object
print(OptimizeResult.to_json())

# convert the object into a dict
optimize_result_dict = optimize_result_instance.to_dict()
# create an instance of OptimizeResult from a dict
optimize_result_from_dict = OptimizeResult.from_dict(optimize_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


