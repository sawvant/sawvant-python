# TierDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**display_name** | **str** |  | 
**price_eur_cents** | **int** |  | 
**period** | **str** |  | [optional] 
**rate_limit_fast** | **int** | Maximum fast strategy requests per 24h sliding window | 
**rate_limit_thorough** | **int** | Maximum thorough strategy requests per 24h sliding window | 
**features** | **Dict[str, bool]** | Feature gates enabled for this tier | 

## Example

```python
from sawvant.models.tier_definition import TierDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of TierDefinition from a JSON string
tier_definition_instance = TierDefinition.from_json(json)
# print the JSON string representation of the object
print(TierDefinition.to_json())

# convert the object into a dict
tier_definition_dict = tier_definition_instance.to_dict()
# create an instance of TierDefinition from a dict
tier_definition_from_dict = TierDefinition.from_dict(tier_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


