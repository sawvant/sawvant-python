# FieldError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | JSON path of the field, e.g. &#x60;parts[2].width&#x60; or &#x60;machine.max_levels&#x60;. For &#x60;INVALID_JSON&#x60; the path has no array index (&#x60;parts.width&#x60;).  | 
**reason** | **str** |  | 

## Example

```python
from sawvant.models.field_error import FieldError

# TODO update the JSON string below
json = "{}"
# create an instance of FieldError from a JSON string
field_error_instance = FieldError.from_json(json)
# print the JSON string representation of the object
print(FieldError.to_json())

# convert the object into a dict
field_error_dict = field_error_instance.to_dict()
# create an instance of FieldError from a dict
field_error_from_dict = FieldError.from_dict(field_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


