# ChannelsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Channel code | 
**locales** | **List[str]** | Codes of activated locales for the channel | 
**currencies** | **List[str]** | Codes of activated currencies for the channel | 
**category_tree** | **str** | Code of the category tree linked to the channel | 
**conversion_units** | [**ChannelsAllOfEmbeddedItemsInnerAllOfConversionUnits**](ChannelsAllOfEmbeddedItemsInnerAllOfConversionUnits.md) |  | [optional] 
**labels** | [**ChannelsAllOfEmbeddedItemsInnerAllOfLabels**](ChannelsAllOfEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 

## Example

```python
from openapi_client.models.channels_post_request import ChannelsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelsPostRequest from a JSON string
channels_post_request_instance = ChannelsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ChannelsPostRequest.to_json())

# convert the object into a dict
channels_post_request_dict = channels_post_request_instance.to_dict()
# create an instance of ChannelsPostRequest from a dict
channels_post_request_from_dict = ChannelsPostRequest.from_dict(channels_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


