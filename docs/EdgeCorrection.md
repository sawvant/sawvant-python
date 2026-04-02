# EdgeCorrection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top** | **float** | mm added for edge banding | [optional] [default to 0]
**bottom** | **float** |  | [optional] [default to 0]
**left** | **float** |  | [optional] [default to 0]
**right** | **float** |  | [optional] [default to 0]

## Example

```python
from sawvant.models.edge_correction import EdgeCorrection

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeCorrection from a JSON string
edge_correction_instance = EdgeCorrection.from_json(json)
# print the JSON string representation of the object
print(EdgeCorrection.to_json())

# convert the object into a dict
edge_correction_dict = edge_correction_instance.to_dict()
# create an instance of EdgeCorrection from a dict
edge_correction_from_dict = EdgeCorrection.from_dict(edge_correction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


