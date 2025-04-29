# NetworkGroupAssignmentPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the network group assignment | 
**group** | [**NetworkGroupAssignmentPostGroup**](NetworkGroupAssignmentPostGroup.md) | The group component of the network group assignment | 
**network** | [**NetworkGroupAssignmentPostNetwork**](NetworkGroupAssignmentPostNetwork.md) | The network component of the network group assignment | 
**type** | **str** | The type of the resource. | 

## Example

```python
from pyhpeuxi.models.network_group_assignment_post_response import NetworkGroupAssignmentPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkGroupAssignmentPostResponse from a JSON string
network_group_assignment_post_response_instance = NetworkGroupAssignmentPostResponse.from_json(json)
# print the JSON string representation of the object
print(NetworkGroupAssignmentPostResponse.to_json())

# convert the object into a dict
network_group_assignment_post_response_dict = network_group_assignment_post_response_instance.to_dict()
# create an instance of NetworkGroupAssignmentPostResponse from a dict
network_group_assignment_post_response_from_dict = NetworkGroupAssignmentPostResponse.from_dict(network_group_assignment_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


