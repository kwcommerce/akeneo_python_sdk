# PostCategoryMediaFilesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The category to which the media file will be associated. It is a JSON string that follows this format &#39;{\&quot;code\&quot;:\&quot;category code\&quot;, \&quot;attribute_code\&quot;:\&quot;attribute code\&quot;, \&quot;channel\&quot;:\&quot;channel code or null\&quot;, \&quot;locale\&quot;:\&quot;locale code or null\&quot;}&#39;. | [optional] 
**file** | **bytearray** | The binary of the file. | 

## Example

```python
from openapi_client.models.post_category_media_files_request import PostCategoryMediaFilesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCategoryMediaFilesRequest from a JSON string
post_category_media_files_request_instance = PostCategoryMediaFilesRequest.from_json(json)
# print the JSON string representation of the object
print(PostCategoryMediaFilesRequest.to_json())

# convert the object into a dict
post_category_media_files_request_dict = post_category_media_files_request_instance.to_dict()
# create an instance of PostCategoryMediaFilesRequest from a dict
post_category_media_files_request_from_dict = PostCategoryMediaFilesRequest.from_dict(post_category_media_files_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


