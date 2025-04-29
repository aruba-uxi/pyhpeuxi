# GroupPatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the group | 
**name** | **str** | The name of the group | 
**path** | **str** | The path of the group | 
**parent** | [**GroupPatchParent**](GroupPatchParent.md) | The parent group | 
**type** | **str** | The type of the resource. | 

## Example

```python
from pyhpeuxi.models.group_patch_response import GroupPatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPatchResponse from a JSON string
group_patch_response_instance = GroupPatchResponse.from_json(json)
# print the JSON string representation of the object
print(GroupPatchResponse.to_json())

# convert the object into a dict
group_patch_response_dict = group_patch_response_instance.to_dict()
# create an instance of GroupPatchResponse from a dict
group_patch_response_from_dict = GroupPatchResponse.from_dict(group_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


