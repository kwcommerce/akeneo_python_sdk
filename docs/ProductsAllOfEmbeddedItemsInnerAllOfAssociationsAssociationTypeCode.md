# ProductsAllOfEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **List[str]** | Array of groups codes with which the product is in relation | [optional] 
**products** | **List[str]** | Array of product uuids with which the product is in relation | [optional] 
**product_models** | **List[str]** | Array of product model codes with which the product is in relation (only available since the v2.1) | [optional] 

## Example

```python
from openapi_client.models.products_all_of_embedded_items_inner_all_of_associations_association_type_code import ProductsAllOfEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsAllOfEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode from a JSON string
products_all_of_embedded_items_inner_all_of_associations_association_type_code_instance = ProductsAllOfEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode.from_json(json)
# print the JSON string representation of the object
print(ProductsAllOfEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode.to_json())

# convert the object into a dict
products_all_of_embedded_items_inner_all_of_associations_association_type_code_dict = products_all_of_embedded_items_inner_all_of_associations_association_type_code_instance.to_dict()
# create an instance of ProductsAllOfEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode from a dict
products_all_of_embedded_items_inner_all_of_associations_association_type_code_from_dict = ProductsAllOfEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode.from_dict(products_all_of_embedded_items_inner_all_of_associations_association_type_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


