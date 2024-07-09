# AppCatalogList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductsAllOfEmbeddedItemsInnerAllOfLinks**](ProductsAllOfEmbeddedItemsInnerAllOfLinks.md) |  | [optional] 
**id** | **str** | Catalog id | [optional] 
**name** | **str** | Catalog name | [optional] 
**enabled** | **bool** | Whether the catalog is enabled or not | [optional] [default to False]
**managed_currencies** | **List[str]** | List of currency codes | [optional] 
**managed_locales** | **List[str]** | List of locale codes | [optional] 

## Example

```python
from openapi_client.models.app_catalog_list import AppCatalogList

# TODO update the JSON string below
json = "{}"
# create an instance of AppCatalogList from a JSON string
app_catalog_list_instance = AppCatalogList.from_json(json)
# print the JSON string representation of the object
print(AppCatalogList.to_json())

# convert the object into a dict
app_catalog_list_dict = app_catalog_list_instance.to_dict()
# create an instance of AppCatalogList from a dict
app_catalog_list_from_dict = AppCatalogList.from_dict(app_catalog_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


