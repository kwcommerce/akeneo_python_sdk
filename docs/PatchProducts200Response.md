# PatchProducts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line** | **int** | Line number | [optional] 
**identifier** | **str** | Resource identifier, only filled when the resource is a product | [optional] 
**code** | **str** | Resource code, only filled when the resource is not a product | [optional] 
**status_code** | **int** | HTTP status code, see &lt;a href&#x3D;\&quot;/documentation/responses.html#client-errors\&quot;&gt;Client errors&lt;/a&gt; to understand the meaning of each code | [optional] 
**message** | **str** | Message explaining the error | [optional] 

## Example

```python
from openapi_client.models.patch_products200_response import PatchProducts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PatchProducts200Response from a JSON string
patch_products200_response_instance = PatchProducts200Response.from_json(json)
# print the JSON string representation of the object
print(PatchProducts200Response.to_json())

# convert the object into a dict
patch_products200_response_dict = patch_products200_response_instance.to_dict()
# create an instance of PatchProducts200Response from a dict
patch_products200_response_from_dict = PatchProducts200Response.from_dict(patch_products200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


