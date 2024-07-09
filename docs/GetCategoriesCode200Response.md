# GetCategoriesCode200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Category code | 
**parent** | **str** | Category code of the parent&#39;s category | [optional] [default to 'null']
**updated** | **str** | Date of the last update | [optional] 
**position** | **int** | Position of the category in its level, start from 1 (only available since the 7.0 version and when query parameter \&quot;with_position\&quot; is set to \&quot;true\&quot;) | [optional] 
**labels** | [**CategoriesAllOfEmbeddedItemsInnerAllOfLabels**](CategoriesAllOfEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 
**values** | [**CategoriesAllOfEmbeddedItemsInnerAllOfValues**](CategoriesAllOfEmbeddedItemsInnerAllOfValues.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_categories_code200_response import GetCategoriesCode200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCategoriesCode200Response from a JSON string
get_categories_code200_response_instance = GetCategoriesCode200Response.from_json(json)
# print the JSON string representation of the object
print(GetCategoriesCode200Response.to_json())

# convert the object into a dict
get_categories_code200_response_dict = get_categories_code200_response_instance.to_dict()
# create an instance of GetCategoriesCode200Response from a dict
get_categories_code200_response_from_dict = GetCategoriesCode200Response.from_dict(get_categories_code200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


