# Placement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_id** | **str** |  | 
**sheet_id** | **str** | Which sheet type this part is placed on | 
**x** | **float** | mm from the top-left of the usable area, along the sheet&#39;s length axis. x + width never exceeds the usable length. | 
**y** | **float** | mm from the top-left of the usable area, along the sheet&#39;s width axis. y + height never exceeds the usable width. | 
**width** | **float** | Post-edge-banding dimension along the sheet&#39;s length axis | 
**height** | **float** | Post-edge-banding dimension along the sheet&#39;s width axis | 
**rotated** | **bool** | True when the part&#39;s length runs along the sheet&#39;s width axis, so width is the part&#39;s width and height is its length. | 
**grain** | [**GrainDirection**](GrainDirection.md) |  | 

## Example

```python
from sawvant.models.placement import Placement

# TODO update the JSON string below
json = "{}"
# create an instance of Placement from a JSON string
placement_instance = Placement.from_json(json)
# print the JSON string representation of the object
print(Placement.to_json())

# convert the object into a dict
placement_dict = placement_instance.to_dict()
# create an instance of Placement from a dict
placement_from_dict = Placement.from_dict(placement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


