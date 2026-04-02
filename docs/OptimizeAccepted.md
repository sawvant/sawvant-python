# OptimizeAccepted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**status** | **str** |  | 
**poll_url** | **str** |  | 
**stream_url** | **str** |  | 

## Example

```python
from sawvant.models.optimize_accepted import OptimizeAccepted

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizeAccepted from a JSON string
optimize_accepted_instance = OptimizeAccepted.from_json(json)
# print the JSON string representation of the object
print(OptimizeAccepted.to_json())

# convert the object into a dict
optimize_accepted_dict = optimize_accepted_instance.to_dict()
# create an instance of OptimizeAccepted from a dict
optimize_accepted_from_dict = OptimizeAccepted.from_dict(optimize_accepted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


