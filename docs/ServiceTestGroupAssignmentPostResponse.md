# ServiceTestGroupAssignmentPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the service test group assignment | 
**group** | [**ServiceTestGroupAssignmentPostGroup**](ServiceTestGroupAssignmentPostGroup.md) | The group component of the service test group assignment | 
**service_test** | [**ServiceTestGroupAssignmentPostServiceTest**](ServiceTestGroupAssignmentPostServiceTest.md) | The service test component of the service test group assignment | 
**type** | **str** | The type of the resource. | 

## Example

```python
from pyhpeuxi.models.service_test_group_assignment_post_response import ServiceTestGroupAssignmentPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTestGroupAssignmentPostResponse from a JSON string
service_test_group_assignment_post_response_instance = ServiceTestGroupAssignmentPostResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceTestGroupAssignmentPostResponse.to_json())

# convert the object into a dict
service_test_group_assignment_post_response_dict = service_test_group_assignment_post_response_instance.to_dict()
# create an instance of ServiceTestGroupAssignmentPostResponse from a dict
service_test_group_assignment_post_response_from_dict = ServiceTestGroupAssignmentPostResponse.from_dict(service_test_group_assignment_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


