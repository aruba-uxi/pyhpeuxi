# NetworkGroupAssignmentPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The unique identifier of the group | 
**network_id** | **str** | The unique identifier of the network | 

## Example

```python
from pyhpeuxi.models.network_group_assignment_post_request import NetworkGroupAssignmentPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkGroupAssignmentPostRequest from a JSON string
network_group_assignment_post_request_instance = NetworkGroupAssignmentPostRequest.from_json(json)
# print the JSON string representation of the object
print(NetworkGroupAssignmentPostRequest.to_json())

# convert the object into a dict
network_group_assignment_post_request_dict = network_group_assignment_post_request_instance.to_dict()
# create an instance of NetworkGroupAssignmentPostRequest from a dict
network_group_assignment_post_request_from_dict = NetworkGroupAssignmentPostRequest.from_dict(network_group_assignment_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


