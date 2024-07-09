# GetProductsUuid401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | HTTP status code | [optional] 
**message** | **str** | Message explaining the error | [optional] 

## Example

```python
from openapi_client.models.get_products_uuid401_response import GetProductsUuid401Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductsUuid401Response from a JSON string
get_products_uuid401_response_instance = GetProductsUuid401Response.from_json(json)
# print the JSON string representation of the object
print(GetProductsUuid401Response.to_json())

# convert the object into a dict
get_products_uuid401_response_dict = get_products_uuid401_response_instance.to_dict()
# create an instance of GetProductsUuid401Response from a dict
get_products_uuid401_response_from_dict = GetProductsUuid401Response.from_dict(get_products_uuid401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


