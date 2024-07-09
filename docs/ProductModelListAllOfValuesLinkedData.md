# ProductModelListAllOfValuesLinkedData

Object containing additional data when a related query parameter is enabled. See <a href='/concepts/products.html#the-linked_data-format'>the `linked_data` format</a> section for more details. (only available since the 5.0)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**labels** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.product_model_list_all_of_values_linked_data import ProductModelListAllOfValuesLinkedData

# TODO update the JSON string below
json = "{}"
# create an instance of ProductModelListAllOfValuesLinkedData from a JSON string
product_model_list_all_of_values_linked_data_instance = ProductModelListAllOfValuesLinkedData.from_json(json)
# print the JSON string representation of the object
print(ProductModelListAllOfValuesLinkedData.to_json())

# convert the object into a dict
product_model_list_all_of_values_linked_data_dict = product_model_list_all_of_values_linked_data_instance.to_dict()
# create an instance of ProductModelListAllOfValuesLinkedData from a dict
product_model_list_all_of_values_linked_data_from_dict = ProductModelListAllOfValuesLinkedData.from_dict(product_model_list_all_of_values_linked_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


