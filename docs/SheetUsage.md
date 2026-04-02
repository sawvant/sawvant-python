# SheetUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sheet_id** | **str** |  | 
**article_number** | **str** | Article/SKU reference (from request, if provided) | [optional] 
**quantity** | **int** | Number of this sheet type consumed | 
**yield_percent** | **float** | Yield percentage for this sheet type | 

## Example

```python
from sawvant.models.sheet_usage import SheetUsage

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUsage from a JSON string
sheet_usage_instance = SheetUsage.from_json(json)
# print the JSON string representation of the object
print(SheetUsage.to_json())

# convert the object into a dict
sheet_usage_dict = sheet_usage_instance.to_dict()
# create an instance of SheetUsage from a dict
sheet_usage_from_dict = SheetUsage.from_dict(sheet_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


