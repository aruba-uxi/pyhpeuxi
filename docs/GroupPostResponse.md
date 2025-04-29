# GroupPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the group | 
**name** | **str** | The name of the group | 
**path** | **str** | The path of the group | 
**parent** | [**GroupPostParent**](GroupPostParent.md) | The parent group | 
**type** | **str** | The type of the resource. | 

## Example

```python
from pyhpeuxi.models.group_post_response import GroupPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPostResponse from a JSON string
group_post_response_instance = GroupPostResponse.from_json(json)
# print the JSON string representation of the object
print(GroupPostResponse.to_json())

# convert the object into a dict
group_post_response_dict = group_post_response_instance.to_dict()
# create an instance of GroupPostResponse from a dict
group_post_response_from_dict = GroupPostResponse.from_dict(group_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


