# SensorGroupAssignmentPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The unique identifier of the group | 
**sensor_id** | **str** | The unique identifier of the sensor | 

## Example

```python
from pyhpeuxi.models.sensor_group_assignment_post_request import SensorGroupAssignmentPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SensorGroupAssignmentPostRequest from a JSON string
sensor_group_assignment_post_request_instance = SensorGroupAssignmentPostRequest.from_json(json)
# print the JSON string representation of the object
print(SensorGroupAssignmentPostRequest.to_json())

# convert the object into a dict
sensor_group_assignment_post_request_dict = sensor_group_assignment_post_request_instance.to_dict()
# create an instance of SensorGroupAssignmentPostRequest from a dict
sensor_group_assignment_post_request_from_dict = SensorGroupAssignmentPostRequest.from_dict(sensor_group_assignment_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


