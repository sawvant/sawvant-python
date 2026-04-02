# Part


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**length** | **float** | Length in mm | 
**width** | **float** | Width in mm | 
**quantity** | **int** |  | 
**grain** | [**GrainDirection**](GrainDirection.md) |  | 
**edge_banding** | [**EdgeCorrection**](EdgeCorrection.md) |  | [optional] 

## Example

```python
from sawvant.models.part import Part

# TODO update the JSON string below
json = "{}"
# create an instance of Part from a JSON string
part_instance = Part.from_json(json)
# print the JSON string representation of the object
print(Part.to_json())

# convert the object into a dict
part_dict = part_instance.to_dict()
# create an instance of Part from a dict
part_from_dict = Part.from_dict(part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


