# ProductsAllOfEmbeddedItemsInnerAllOfValuesAttributeCodeInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | &lt;a href&#x3D;&#39;api-reference.html#Channel&#39;&gt;Channel&lt;/a&gt; code of the product value | [optional] 
**locale** | **str** | &lt;a href&#x3D;&#39;api-reference.html#Locale&#39;&gt;Locale&lt;/a&gt; code of the product value | [optional] 
**data** | **object** | Product value. See &lt;a href&#x3D;&#39;/concepts/products.html#the-data-format&#39;&gt;the &#x60;data&#x60; format&lt;/a&gt; section for more details. | [optional] 
**linked_data** | [**ProductsAllOfEmbeddedItemsInnerAllOfValuesAttributeCodeInnerLinkedData**](ProductsAllOfEmbeddedItemsInnerAllOfValuesAttributeCodeInnerLinkedData.md) |  | [optional] 
**attribute_type** | **str** | The type of the value&#39;s attribute. See &lt;a href&#x3D;&#39;/concepts/catalog-structure.html#attribute&#39;&gt;type&lt;/a&gt; section for more details. | [optional] 
**reference_data_name** | **str** | Reference entity code when the attribute type is &#x60;akeneo_reference_entity&#x60; or &#x60;akeneo_reference_entity_collection&#x60; OR Asset family code when the attribute type is &#x60;pim_catalog_asset_collection&#x60; | [optional] 

## Example

```python
from openapi_client.models.products_all_of_embedded_items_inner_all_of_values_attribute_code_inner import ProductsAllOfEmbeddedItemsInnerAllOfValuesAttributeCodeInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsAllOfEmbeddedItemsInnerAllOfValuesAttributeCodeInner from a JSON string
products_all_of_embedded_items_inner_all_of_values_attribute_code_inner_instance = ProductsAllOfEmbeddedItemsInnerAllOfValuesAttributeCodeInner.from_json(json)
# print the JSON string representation of the object
print(ProductsAllOfEmbeddedItemsInnerAllOfValuesAttributeCodeInner.to_json())

# convert the object into a dict
products_all_of_embedded_items_inner_all_of_values_attribute_code_inner_dict = products_all_of_embedded_items_inner_all_of_values_attribute_code_inner_instance.to_dict()
# create an instance of ProductsAllOfEmbeddedItemsInnerAllOfValuesAttributeCodeInner from a dict
products_all_of_embedded_items_inner_all_of_values_attribute_code_inner_from_dict = ProductsAllOfEmbeddedItemsInnerAllOfValuesAttributeCodeInner.from_dict(products_all_of_embedded_items_inner_all_of_values_attribute_code_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


