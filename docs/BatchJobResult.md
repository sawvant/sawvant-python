# BatchJobResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Position of this job in the request array | 
**job_id** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from sawvant.models.batch_job_result import BatchJobResult

# TODO update the JSON string below
json = "{}"
# create an instance of BatchJobResult from a JSON string
batch_job_result_instance = BatchJobResult.from_json(json)
# print the JSON string representation of the object
print(BatchJobResult.to_json())

# convert the object into a dict
batch_job_result_dict = batch_job_result_instance.to_dict()
# create an instance of BatchJobResult from a dict
batch_job_result_from_dict = BatchJobResult.from_dict(batch_job_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


