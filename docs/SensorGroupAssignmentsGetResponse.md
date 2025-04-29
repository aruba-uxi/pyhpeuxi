# SensorGroupAssignmentsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SensorGroupAssignmentsGetItem]**](SensorGroupAssignmentsGetItem.md) | The list of resources. | 
**count** | **int** | The number of resources returned in the response. | 
**next** | **str** |  | 

## Example

```python
from pyhpeuxi.models.sensor_group_assignments_get_response import SensorGroupAssignmentsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SensorGroupAssignmentsGetResponse from a JSON string
sensor_group_assignments_get_response_instance = SensorGroupAssignmentsGetResponse.from_json(json)
# print the JSON string representation of the object
print(SensorGroupAssignmentsGetResponse.to_json())

# convert the object into a dict
sensor_group_assignments_get_response_dict = sensor_group_assignments_get_response_instance.to_dict()
# create an instance of SensorGroupAssignmentsGetResponse from a dict
sensor_group_assignments_get_response_from_dict = SensorGroupAssignmentsGetResponse.from_dict(sensor_group_assignments_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


