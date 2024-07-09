# CategoryUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Category code | 
**parent** | **str** | Category code of the parent&#39;s category | [optional] [default to 'null']
**updated** | **str** | Date of the last update | [optional] 
**position** | **int** | Position of the category in its level, start from 1 (only available since the 7.0 version and when query parameter \&quot;with_position\&quot; is set to \&quot;true\&quot;) | [optional] 
**labels** | [**CategoriesAllOfEmbeddedItemsInnerAllOfLabels**](CategoriesAllOfEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 
**values** | [**List[PostCategoriesRequestValuesInner]**](PostCategoriesRequestValuesInner.md) | Attribute values (only available on SaaS). | [optional] 

## Example

```python
from openapi_client.models.category_update import CategoryUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryUpdate from a JSON string
category_update_instance = CategoryUpdate.from_json(json)
# print the JSON string representation of the object
print(CategoryUpdate.to_json())

# convert the object into a dict
category_update_dict = category_update_instance.to_dict()
# create an instance of CategoryUpdate from a dict
category_update_from_dict = CategoryUpdate.from_dict(category_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


