# ServiceTestGroupAssignmentsGetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the service test group assignment | 
**group** | [**ServiceTestGroupAssignmentsGetGroup**](ServiceTestGroupAssignmentsGetGroup.md) | The group component of the service test group assignment | 
**service_test** | [**ServiceTestGroupAssignmentsGetServiceTest**](ServiceTestGroupAssignmentsGetServiceTest.md) | The service test component of the service test group assignment | 
**type** | **str** | The type of the resource. | 

## Example

```python
from pyhpeuxi.models.service_test_group_assignments_get_item import ServiceTestGroupAssignmentsGetItem

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTestGroupAssignmentsGetItem from a JSON string
service_test_group_assignments_get_item_instance = ServiceTestGroupAssignmentsGetItem.from_json(json)
# print the JSON string representation of the object
print(ServiceTestGroupAssignmentsGetItem.to_json())

# convert the object into a dict
service_test_group_assignments_get_item_dict = service_test_group_assignments_get_item_instance.to_dict()
# create an instance of ServiceTestGroupAssignmentsGetItem from a dict
service_test_group_assignments_get_item_from_dict = ServiceTestGroupAssignmentsGetItem.from_dict(service_test_group_assignments_get_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


