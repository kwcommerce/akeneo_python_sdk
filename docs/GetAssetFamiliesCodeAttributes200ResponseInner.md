# GetAssetFamiliesCodeAttributes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Attribute code | 
**labels** | [**AttributesAllOfEmbeddedItemsInnerAllOfLabels**](AttributesAllOfEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 
**type** | **str** | Attribute type. See &lt;a href&#x3D;&#39;/concepts/asset-manager.html#asset-attribute&#39;&gt;type&lt;/a&gt; section for more details. | 
**value_per_locale** | **bool** | Whether the attribute is localizable, i.e. can have one value by locale | [optional] [default to False]
**value_per_channel** | **bool** | Whether the attribute is scopable, i.e. can have one value by channel | [optional] [default to False]
**is_required_for_completeness** | **bool** | Whether the attribute should be part of the record&#39;s completeness calculation | [optional] [default to False]
**is_read_only** | **bool** | Whether the attribute should be in read only mode only in the UI, but you can still update it with the API | [optional] [default to False]
**max_characters** | **int** | Maximum number of characters allowed for the value of the attribute when the attribute type is &#x60;text&#x60; | [optional] 
**is_textarea** | **bool** | Whether the UI should display a text area instead of a simple field when the attribute type is &#x60;text&#x60; | [optional] [default to False]
**is_rich_text_editor** | **bool** | Whether the UI should display a rich text editor instead of a simple text area when the attribute type is &#x60;text&#x60; | [optional] 
**validation_rule** | **str** | Validation rule type used to validate the attribute value when the attribute type is &#x60;text&#x60; | [optional] [default to 'none']
**validation_regexp** | **str** | Regexp expression used to validate the attribute value when the attribute type is &#x60;text&#x60; | [optional] [default to 'null']
**allowed_extensions** | **List[str]** | Extensions allowed when the attribute type is &#x60;media_file&#x60; | [optional] 
**max_file_size** | **str** | Max file size in MB when the attribute type is &#x60;media_file&#x60; | [optional] [default to 'null']
**decimals_allowed** | **bool** | Whether decimals are allowed when the attribute type is &#x60;number&#x60; | [optional] [default to False]
**min_value** | **str** | Minimum value allowed when the attribute type is &#x60;number&#x60; | [optional] [default to 'null']
**max_value** | **str** | Maximum value allowed when the attribute type is &#x60;number&#x60; | [optional] [default to 'null']
**media_type** | **str** | For the &#x60;media_link&#x60; attribute type, it is the type of the media behind the url, to allow its preview in the PIM. For the &#x60;media_file&#x60; attribute type, it is the type of the file. | 
**prefix** | **str** | Prefix of the &#x60;media_link&#x60; attribute type. The common url root that prefixes the link to the media | [optional] [default to 'null']
**suffix** | **str** | Suffix of the &#x60;media_link&#x60; attribute type. The common url suffix for the media | [optional] [default to 'null']
**reference_entity** | **str** | Reference entity code for the &#x60;record&#x60; attribute type (see &lt;a href&#x3D;&#39;/api-reference.html#Referenceentity&#39;&gt;Reference entity&lt;/a&gt;). | [optional] [default to 'null']

## Example

```python
from openapi_client.models.get_asset_families_code_attributes200_response_inner import GetAssetFamiliesCodeAttributes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetFamiliesCodeAttributes200ResponseInner from a JSON string
get_asset_families_code_attributes200_response_inner_instance = GetAssetFamiliesCodeAttributes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetAssetFamiliesCodeAttributes200ResponseInner.to_json())

# convert the object into a dict
get_asset_families_code_attributes200_response_inner_dict = get_asset_families_code_attributes200_response_inner_instance.to_dict()
# create an instance of GetAssetFamiliesCodeAttributes200ResponseInner from a dict
get_asset_families_code_attributes200_response_inner_from_dict = GetAssetFamiliesCodeAttributes200ResponseInner.from_dict(get_asset_families_code_attributes200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


