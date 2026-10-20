# ApiErrorBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**ErrorCode**](ErrorCode.md) |  | 
**message** | **str** | Human-readable explanation. Do not parse it; use &#x60;code&#x60; and &#x60;details&#x60;. | 
**details** | [**List[FieldError]**](FieldError.md) |  | [optional] 

## Example

```python
from sawvant.models.api_error_body import ApiErrorBody

# TODO update the JSON string below
json = "{}"
# create an instance of ApiErrorBody from a JSON string
api_error_body_instance = ApiErrorBody.from_json(json)
# print the JSON string representation of the object
print(ApiErrorBody.to_json())

# convert the object into a dict
api_error_body_dict = api_error_body_instance.to_dict()
# create an instance of ApiErrorBody from a dict
api_error_body_from_dict = ApiErrorBody.from_dict(api_error_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


