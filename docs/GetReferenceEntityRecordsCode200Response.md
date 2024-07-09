# GetReferenceEntityRecordsCode200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of the record | 
**values** | [**ReferenceEntityRecordAllOfEmbeddedItemsInnerAllOfValues**](ReferenceEntityRecordAllOfEmbeddedItemsInnerAllOfValues.md) |  | [optional] 
**created** | **str** | Date of creation. | [optional] [default to 'null']
**updated** | **str** | Date of the last update. | [optional] [default to 'null']

## Example

```python
from openapi_client.models.get_reference_entity_records_code200_response import GetReferenceEntityRecordsCode200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetReferenceEntityRecordsCode200Response from a JSON string
get_reference_entity_records_code200_response_instance = GetReferenceEntityRecordsCode200Response.from_json(json)
# print the JSON string representation of the object
print(GetReferenceEntityRecordsCode200Response.to_json())

# convert the object into a dict
get_reference_entity_records_code200_response_dict = get_reference_entity_records_code200_response_instance.to_dict()
# create an instance of GetReferenceEntityRecordsCode200Response from a dict
get_reference_entity_records_code200_response_from_dict = GetReferenceEntityRecordsCode200Response.from_dict(get_reference_entity_records_code200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


