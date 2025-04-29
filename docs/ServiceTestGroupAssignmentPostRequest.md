# ServiceTestGroupAssignmentPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The unique identifier of the group | 
**service_test_id** | **str** | The unique identifier of the service test | 

## Example

```python
from pyhpeuxi.models.service_test_group_assignment_post_request import ServiceTestGroupAssignmentPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTestGroupAssignmentPostRequest from a JSON string
service_test_group_assignment_post_request_instance = ServiceTestGroupAssignmentPostRequest.from_json(json)
# print the JSON string representation of the object
print(ServiceTestGroupAssignmentPostRequest.to_json())

# convert the object into a dict
service_test_group_assignment_post_request_dict = service_test_group_assignment_post_request_instance.to_dict()
# create an instance of ServiceTestGroupAssignmentPostRequest from a dict
service_test_group_assignment_post_request_from_dict = ServiceTestGroupAssignmentPostRequest.from_dict(service_test_group_assignment_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


