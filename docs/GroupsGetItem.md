# GroupsGetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the group | 
**name** | **str** | The name of the group | 
**parent** | [**GroupsGetParent**](GroupsGetParent.md) |  | 
**path** | **str** | The path of the group | 
**type** | **str** | The type of the resource. | 

## Example

```python
from pyhpeuxi.models.groups_get_item import GroupsGetItem

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsGetItem from a JSON string
groups_get_item_instance = GroupsGetItem.from_json(json)
# print the JSON string representation of the object
print(GroupsGetItem.to_json())

# convert the object into a dict
groups_get_item_dict = groups_get_item_instance.to_dict()
# create an instance of GroupsGetItem from a dict
groups_get_item_from_dict = GroupsGetItem.from_dict(groups_get_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


