# NetworkGroupAssignmentsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NetworkGroupAssignmentsGetItem]**](NetworkGroupAssignmentsGetItem.md) | The list of resources. | 
**count** | **int** | The number of resources returned in the response. | 
**next** | **str** |  | 

## Example

```python
from pyhpeuxi.models.network_group_assignments_get_response import NetworkGroupAssignmentsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkGroupAssignmentsGetResponse from a JSON string
network_group_assignments_get_response_instance = NetworkGroupAssignmentsGetResponse.from_json(json)
# print the JSON string representation of the object
print(NetworkGroupAssignmentsGetResponse.to_json())

# convert the object into a dict
network_group_assignments_get_response_dict = network_group_assignments_get_response_instance.to_dict()
# create an instance of NetworkGroupAssignmentsGetResponse from a dict
network_group_assignments_get_response_from_dict = NetworkGroupAssignmentsGetResponse.from_dict(network_group_assignments_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


