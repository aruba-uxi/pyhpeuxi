# SensorGroupAssignmentsGetSensor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the sensor | 

## Example

```python
from pyhpeuxi.models.sensor_group_assignments_get_sensor import SensorGroupAssignmentsGetSensor

# TODO update the JSON string below
json = "{}"
# create an instance of SensorGroupAssignmentsGetSensor from a JSON string
sensor_group_assignments_get_sensor_instance = SensorGroupAssignmentsGetSensor.from_json(json)
# print the JSON string representation of the object
print(SensorGroupAssignmentsGetSensor.to_json())

# convert the object into a dict
sensor_group_assignments_get_sensor_dict = sensor_group_assignments_get_sensor_instance.to_dict()
# create an instance of SensorGroupAssignmentsGetSensor from a dict
sensor_group_assignments_get_sensor_from_dict = SensorGroupAssignmentsGetSensor.from_dict(sensor_group_assignments_get_sensor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


