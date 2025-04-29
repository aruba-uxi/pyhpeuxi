# SensorPatchRequest

Request body for patching a sensor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The updated sensor name | [optional] 
**address_note** | **str** | The updated address note for the sensor | [optional] 
**notes** | **str** | Additional notes for the sensor | [optional] 
**pcap_mode** | [**SensorPcapMode**](SensorPcapMode.md) | The updated pcap mode for the sensor | [optional] 

## Example

```python
from pyhpeuxi.models.sensor_patch_request import SensorPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SensorPatchRequest from a JSON string
sensor_patch_request_instance = SensorPatchRequest.from_json(json)
# print the JSON string representation of the object
print(SensorPatchRequest.to_json())

# convert the object into a dict
sensor_patch_request_dict = sensor_patch_request_instance.to_dict()
# create an instance of SensorPatchRequest from a dict
sensor_patch_request_from_dict = SensorPatchRequest.from_dict(sensor_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


