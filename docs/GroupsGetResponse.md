# GroupsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[GroupsGetItem]**](GroupsGetItem.md) | The list of resources. | 
**count** | **int** | The number of resources returned in the response. | 
**next** | **str** |  | 

## Example

```python
from pyhpeuxi.models.groups_get_response import GroupsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsGetResponse from a JSON string
groups_get_response_instance = GroupsGetResponse.from_json(json)
# print the JSON string representation of the object
print(GroupsGetResponse.to_json())

# convert the object into a dict
groups_get_response_dict = groups_get_response_instance.to_dict()
# create an instance of GroupsGetResponse from a dict
groups_get_response_from_dict = GroupsGetResponse.from_dict(groups_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


