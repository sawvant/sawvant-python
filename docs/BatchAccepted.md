# BatchAccepted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** |  | 
**job_ids** | **List[str]** |  | 
**total** | **int** | Number of jobs in the request | 
**created** | **int** | Number of jobs successfully enqueued | 
**results** | [**List[BatchJobResult]**](BatchJobResult.md) | Present only when one or more jobs failed to enqueue | [optional] 

## Example

```python
from sawvant.models.batch_accepted import BatchAccepted

# TODO update the JSON string below
json = "{}"
# create an instance of BatchAccepted from a JSON string
batch_accepted_instance = BatchAccepted.from_json(json)
# print the JSON string representation of the object
print(BatchAccepted.to_json())

# convert the object into a dict
batch_accepted_dict = batch_accepted_instance.to_dict()
# create an instance of BatchAccepted from a dict
batch_accepted_from_dict = BatchAccepted.from_dict(batch_accepted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


