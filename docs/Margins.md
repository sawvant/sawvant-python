# Margins


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top** | **float** | mm trim per side | [optional] [default to 0]
**bottom** | **float** |  | [optional] [default to 0]
**left** | **float** |  | [optional] [default to 0]
**right** | **float** |  | [optional] [default to 0]

## Example

```python
from sawvant.models.margins import Margins

# TODO update the JSON string below
json = "{}"
# create an instance of Margins from a JSON string
margins_instance = Margins.from_json(json)
# print the JSON string representation of the object
print(Margins.to_json())

# convert the object into a dict
margins_dict = margins_instance.to_dict()
# create an instance of Margins from a dict
margins_from_dict = Margins.from_dict(margins_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


