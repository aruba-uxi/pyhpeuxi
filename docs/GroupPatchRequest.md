# GroupPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The updated group name | [optional] 

## Example

```python
from pyhpeuxi.models.group_patch_request import GroupPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPatchRequest from a JSON string
group_patch_request_instance = GroupPatchRequest.from_json(json)
# print the JSON string representation of the object
print(GroupPatchRequest.to_json())

# convert the object into a dict
group_patch_request_dict = group_patch_request_instance.to_dict()
# create an instance of GroupPatchRequest from a dict
group_patch_request_from_dict = GroupPatchRequest.from_dict(group_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


