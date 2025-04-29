# GroupPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **str** |  | [optional] 
**name** | **str** | The name of the group | 

## Example

```python
from pyhpeuxi.models.group_post_request import GroupPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPostRequest from a JSON string
group_post_request_instance = GroupPostRequest.from_json(json)
# print the JSON string representation of the object
print(GroupPostRequest.to_json())

# convert the object into a dict
group_post_request_dict = group_post_request_instance.to_dict()
# create an instance of GroupPostRequest from a dict
group_post_request_from_dict = GroupPostRequest.from_dict(group_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


