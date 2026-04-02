# Layout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sheet_id** | **str** |  | 
**quantity** | **int** | Number of identical sheets using this layout pattern | 
**placements** | [**List[Placement]**](Placement.md) |  | 

## Example

```python
from sawvant.models.layout import Layout

# TODO update the JSON string below
json = "{}"
# create an instance of Layout from a JSON string
layout_instance = Layout.from_json(json)
# print the JSON string representation of the object
print(Layout.to_json())

# convert the object into a dict
layout_dict = layout_instance.to_dict()
# create an instance of Layout from a dict
layout_from_dict = Layout.from_dict(layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


