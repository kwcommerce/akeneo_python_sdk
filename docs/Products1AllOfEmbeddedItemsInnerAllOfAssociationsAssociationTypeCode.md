# Products1AllOfEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **List[str]** | Array of groups codes with which the product is in relation | [optional] 
**products** | **List[str]** | Array of product identifiers with which the product is in relation | [optional] 
**product_models** | **List[str]** | Array of product model codes with which the product is in relation (only available since the v2.1) | [optional] 

## Example

```python
from openapi_client.models.products1_all_of_embedded_items_inner_all_of_associations_association_type_code import Products1AllOfEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode

# TODO update the JSON string below
json = "{}"
# create an instance of Products1AllOfEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode from a JSON string
products1_all_of_embedded_items_inner_all_of_associations_association_type_code_instance = Products1AllOfEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode.from_json(json)
# print the JSON string representation of the object
print(Products1AllOfEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode.to_json())

# convert the object into a dict
products1_all_of_embedded_items_inner_all_of_associations_association_type_code_dict = products1_all_of_embedded_items_inner_all_of_associations_association_type_code_instance.to_dict()
# create an instance of Products1AllOfEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode from a dict
products1_all_of_embedded_items_inner_all_of_associations_association_type_code_from_dict = Products1AllOfEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode.from_dict(products1_all_of_embedded_items_inner_all_of_associations_association_type_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


