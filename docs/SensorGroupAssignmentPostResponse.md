# SensorGroupAssignmentPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the sensor group assignment | 
**group** | [**SensorGroupAssignmentPostGroup**](SensorGroupAssignmentPostGroup.md) | The group component of the sensor group assignment | 
**sensor** | [**SensorGroupAssignmentPostSensor**](SensorGroupAssignmentPostSensor.md) | The sensor component of the sensor group assignment | 
**type** | **str** | The type of the resource. | 

## Example

```python
from pyhpeuxi.models.sensor_group_assignment_post_response import SensorGroupAssignmentPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SensorGroupAssignmentPostResponse from a JSON string
sensor_group_assignment_post_response_instance = SensorGroupAssignmentPostResponse.from_json(json)
# print the JSON string representation of the object
print(SensorGroupAssignmentPostResponse.to_json())

# convert the object into a dict
sensor_group_assignment_post_response_dict = sensor_group_assignment_post_response_instance.to_dict()
# create an instance of SensorGroupAssignmentPostResponse from a dict
sensor_group_assignment_post_response_from_dict = SensorGroupAssignmentPostResponse.from_dict(sensor_group_assignment_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


