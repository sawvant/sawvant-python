# Machine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blade_thickness** | **float** | Kerf width in mm | 
**max_levels** | **int** | Cut pattern complexity (1-3) | 
**max_stack_height** | **float** | Maximum stack height in mm for batch cutting | [optional] 
**cut_direction** | [**CutDirection**](CutDirection.md) |  | 

## Example

```python
from sawvant.models.machine import Machine

# TODO update the JSON string below
json = "{}"
# create an instance of Machine from a JSON string
machine_instance = Machine.from_json(json)
# print the JSON string representation of the object
print(Machine.to_json())

# convert the object into a dict
machine_dict = machine_instance.to_dict()
# create an instance of Machine from a dict
machine_from_dict = Machine.from_dict(machine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


