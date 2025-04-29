# SensorGroupAssignmentsGetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the sensor group assignment | 
**group** | [**SensorGroupAssignmentsGetGroup**](SensorGroupAssignmentsGetGroup.md) | The group component of the sensor group assignment | 
**sensor** | [**SensorGroupAssignmentsGetSensor**](SensorGroupAssignmentsGetSensor.md) | The sensor component of the sensor group assignment | 
**type** | **str** | The type of the resource. | 

## Example

```python
from pyhpeuxi.models.sensor_group_assignments_get_item import SensorGroupAssignmentsGetItem

# TODO update the JSON string below
json = "{}"
# create an instance of SensorGroupAssignmentsGetItem from a JSON string
sensor_group_assignments_get_item_instance = SensorGroupAssignmentsGetItem.from_json(json)
# print the JSON string representation of the object
print(SensorGroupAssignmentsGetItem.to_json())

# convert the object into a dict
sensor_group_assignments_get_item_dict = sensor_group_assignments_get_item_instance.to_dict()
# create an instance of SensorGroupAssignmentsGetItem from a dict
sensor_group_assignments_get_item_from_dict = SensorGroupAssignmentsGetItem.from_dict(sensor_group_assignments_get_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


