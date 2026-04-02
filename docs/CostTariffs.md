# CostTariffs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**setup_cost** | **float** | Fixed cost per job | [optional] 
**cost_per_meter** | **float** | Cost per meter of cut length | [optional] 
**cost_per_rotation** | **float** |  | [optional] 
**cost_per_stack** | **float** |  | [optional] 
**cost_per_cycle** | **float** |  | [optional] 

## Example

```python
from sawvant.models.cost_tariffs import CostTariffs

# TODO update the JSON string below
json = "{}"
# create an instance of CostTariffs from a JSON string
cost_tariffs_instance = CostTariffs.from_json(json)
# print the JSON string representation of the object
print(CostTariffs.to_json())

# convert the object into a dict
cost_tariffs_dict = cost_tariffs_instance.to_dict()
# create an instance of CostTariffs from a dict
cost_tariffs_from_dict = CostTariffs.from_dict(cost_tariffs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


