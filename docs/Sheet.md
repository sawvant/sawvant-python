# Sheet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**length** | **float** | Length in mm | 
**width** | **float** | Width in mm | 
**quantity** | **int** | 0 &#x3D; unlimited | 
**grain** | [**GrainDirection**](GrainDirection.md) |  | 
**is_offcut** | **bool** | Offcut sheets are prioritized by the solver | [optional] [default to False]
**trim_margins** | [**Margins**](Margins.md) |  | [optional] 
**article_number** | **str** | Optional article/SKU reference for this sheet type | [optional] 

## Example

```python
from sawvant.models.sheet import Sheet

# TODO update the JSON string below
json = "{}"
# create an instance of Sheet from a JSON string
sheet_instance = Sheet.from_json(json)
# print the JSON string representation of the object
print(Sheet.to_json())

# convert the object into a dict
sheet_dict = sheet_instance.to_dict()
# create an instance of Sheet from a dict
sheet_from_dict = Sheet.from_dict(sheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


