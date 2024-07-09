# PatchFamiliesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Family code | 
**attribute_as_label** | **str** | Attribute code used as label | 
**attribute_as_image** | **str** | Attribute code used as the main picture in the user interface (only since v2.0) | [optional] [default to 'null']
**attributes** | **List[str]** | Attributes codes that compose the family | [optional] 
**attribute_requirements** | [**FamiliesAllOfEmbeddedItemsInnerAllOfAttributeRequirements**](FamiliesAllOfEmbeddedItemsInnerAllOfAttributeRequirements.md) |  | [optional] 
**labels** | [**FamiliesAllOfEmbeddedItemsInnerAllOfLabels**](FamiliesAllOfEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 

## Example

```python
from openapi_client.models.patch_families_request import PatchFamiliesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchFamiliesRequest from a JSON string
patch_families_request_instance = PatchFamiliesRequest.from_json(json)
# print the JSON string representation of the object
print(PatchFamiliesRequest.to_json())

# convert the object into a dict
patch_families_request_dict = patch_families_request_instance.to_dict()
# create an instance of PatchFamiliesRequest from a dict
patch_families_request_from_dict = PatchFamiliesRequest.from_dict(patch_families_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


