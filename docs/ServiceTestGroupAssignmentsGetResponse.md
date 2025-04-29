# ServiceTestGroupAssignmentsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ServiceTestGroupAssignmentsGetItem]**](ServiceTestGroupAssignmentsGetItem.md) | The list of resources. | 
**count** | **int** | The number of resources returned in the response. | 
**next** | **str** |  | 

## Example

```python
from pyhpeuxi.models.service_test_group_assignments_get_response import ServiceTestGroupAssignmentsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTestGroupAssignmentsGetResponse from a JSON string
service_test_group_assignments_get_response_instance = ServiceTestGroupAssignmentsGetResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceTestGroupAssignmentsGetResponse.to_json())

# convert the object into a dict
service_test_group_assignments_get_response_dict = service_test_group_assignments_get_response_instance.to_dict()
# create an instance of ServiceTestGroupAssignmentsGetResponse from a dict
service_test_group_assignments_get_response_from_dict = ServiceTestGroupAssignmentsGetResponse.from_dict(service_test_group_assignments_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


