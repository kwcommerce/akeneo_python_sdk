# PostCategoriesRequestValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Attribute value. It should be a &#x60;string&#x60; for Text and Text Area attributes, a &#x60;boolean&#x60; for Yes/No attribute and for Image attribute use the &lt;a href&#x3D;\&quot;api-reference.html#post_category_media_files\&quot;&gt;create category media file endpoint&lt;/a&gt;. It can also be &#x60;null&#x60; to remove the value. | [optional] 
**locale** | **str** | &lt;a href&#x3D;\&quot;api-reference.html#Locale\&quot;&gt;Locale&lt;/a&gt; code of the attribute value. | [optional] 
**channel** | **str** | &lt;a href&#x3D;\&quot;api-reference.html#Channel\&quot;&gt;Channel&lt;/a&gt; code of the attribute value. | [optional] 
**attribute_code** | **str** | The attribute code. | [optional] 

## Example

```python
from openapi_client.models.post_categories_request_values_inner import PostCategoriesRequestValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostCategoriesRequestValuesInner from a JSON string
post_categories_request_values_inner_instance = PostCategoriesRequestValuesInner.from_json(json)
# print the JSON string representation of the object
print(PostCategoriesRequestValuesInner.to_json())

# convert the object into a dict
post_categories_request_values_inner_dict = post_categories_request_values_inner_instance.to_dict()
# create an instance of PostCategoriesRequestValuesInner from a dict
post_categories_request_values_inner_from_dict = PostCategoriesRequestValuesInner.from_dict(post_categories_request_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


