# DemoLayout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sheet_id** | **str** |  | 
**quantity** | **int** | Number of identical sheets using this layout pattern | 
**placements** | [**List[Placement]**](Placement.md) |  | 
**svg** | **str** | Cutting plan of this layout as a standalone SVG document | 

## Example

```python
from sawvant.models.demo_layout import DemoLayout

# TODO update the JSON string below
json = "{}"
# create an instance of DemoLayout from a JSON string
demo_layout_instance = DemoLayout.from_json(json)
# print the JSON string representation of the object
print(DemoLayout.to_json())

# convert the object into a dict
demo_layout_dict = demo_layout_instance.to_dict()
# create an instance of DemoLayout from a dict
demo_layout_from_dict = DemoLayout.from_dict(demo_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


