# ProductsAllOfLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**ProductsAllOfLinksSelf**](ProductsAllOfLinksSelf.md) |  | [optional] 
**first** | [**ProductsAllOfLinksFirst**](ProductsAllOfLinksFirst.md) |  | [optional] 
**previous** | [**ProductsAllOfLinksPrevious**](ProductsAllOfLinksPrevious.md) |  | [optional] 
**next** | [**ProductsAllOfLinksNext**](ProductsAllOfLinksNext.md) |  | [optional] 

## Example

```python
from openapi_client.models.products_all_of_links import ProductsAllOfLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsAllOfLinks from a JSON string
products_all_of_links_instance = ProductsAllOfLinks.from_json(json)
# print the JSON string representation of the object
print(ProductsAllOfLinks.to_json())

# convert the object into a dict
products_all_of_links_dict = products_all_of_links_instance.to_dict()
# create an instance of ProductsAllOfLinks from a dict
products_all_of_links_from_dict = ProductsAllOfLinks.from_dict(products_all_of_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


