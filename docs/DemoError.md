# DemoError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**DemoErrorError**](DemoErrorError.md) |  | 

## Example

```python
from sawvant.models.demo_error import DemoError

# TODO update the JSON string below
json = "{}"
# create an instance of DemoError from a JSON string
demo_error_instance = DemoError.from_json(json)
# print the JSON string representation of the object
print(DemoError.to_json())

# convert the object into a dict
demo_error_dict = demo_error_instance.to_dict()
# create an instance of DemoError from a dict
demo_error_from_dict = DemoError.from_dict(demo_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


