# NetworkGroupAssignmentsGetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the network group assignment | 
**group** | [**NetworkGroupAssignmentsGetGroup**](NetworkGroupAssignmentsGetGroup.md) | The group component of the network group assignment | 
**network** | [**NetworkGroupAssignmentsGetNetwork**](NetworkGroupAssignmentsGetNetwork.md) | The network component of the network group assignment | 
**type** | **str** | The type of the resource. | 

## Example

```python
from pyhpeuxi.models.network_group_assignments_get_item import NetworkGroupAssignmentsGetItem

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkGroupAssignmentsGetItem from a JSON string
network_group_assignments_get_item_instance = NetworkGroupAssignmentsGetItem.from_json(json)
# print the JSON string representation of the object
print(NetworkGroupAssignmentsGetItem.to_json())

# convert the object into a dict
network_group_assignments_get_item_dict = network_group_assignments_get_item_instance.to_dict()
# create an instance of NetworkGroupAssignmentsGetItem from a dict
network_group_assignments_get_item_from_dict = NetworkGroupAssignmentsGetItem.from_dict(network_group_assignments_get_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


