# PublishedProductListAllOfValuesAttributeCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | &lt;a href&#x3D;&#39;api-reference.html#Channel&#39;&gt;Channel&lt;/a&gt; code of the product value | [optional] 
**locale** | **str** | &lt;a href&#x3D;&#39;api-reference.html#Locale&#39;&gt;Locale&lt;/a&gt; code of the product value | [optional] 
**data** | **object** | &lt;a href&#x3D;&#39;api-reference.html#Productuuid&#39;&gt;Product&lt;/a&gt; value | [optional] 

## Example

```python
from openapi_client.models.published_product_list_all_of_values_attribute_code import PublishedProductListAllOfValuesAttributeCode

# TODO update the JSON string below
json = "{}"
# create an instance of PublishedProductListAllOfValuesAttributeCode from a JSON string
published_product_list_all_of_values_attribute_code_instance = PublishedProductListAllOfValuesAttributeCode.from_json(json)
# print the JSON string representation of the object
print(PublishedProductListAllOfValuesAttributeCode.to_json())

# convert the object into a dict
published_product_list_all_of_values_attribute_code_dict = published_product_list_all_of_values_attribute_code_instance.to_dict()
# create an instance of PublishedProductListAllOfValuesAttributeCode from a dict
published_product_list_all_of_values_attribute_code_from_dict = PublishedProductListAllOfValuesAttributeCode.from_dict(published_product_list_all_of_values_attribute_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


