# GetAssetsCode200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of the asset | 
**values** | [**AssetAllOfEmbeddedItemsInnerAllOfValues**](AssetAllOfEmbeddedItemsInnerAllOfValues.md) |  | [optional] 
**created** | **str** | Date of creation | [optional] 
**updated** | **str** | Date of the last update | [optional] 

## Example

```python
from openapi_client.models.get_assets_code200_response import GetAssetsCode200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetsCode200Response from a JSON string
get_assets_code200_response_instance = GetAssetsCode200Response.from_json(json)
# print the JSON string representation of the object
print(GetAssetsCode200Response.to_json())

# convert the object into a dict
get_assets_code200_response_dict = get_assets_code200_response_instance.to_dict()
# create an instance of GetAssetsCode200Response from a dict
get_assets_code200_response_from_dict = GetAssetsCode200Response.from_dict(get_assets_code200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


