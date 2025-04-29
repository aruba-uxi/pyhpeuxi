# SensorPatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the sensor | 
**serial** | **str** | The serial number of the sensor | 
**name** | **str** | The name of the sensor | 
**model_number** | **str** | The model number of the sensor | 
**wifi_mac_address** | **str** |  | 
**ethernet_mac_address** | **str** |  | 
**address_note** | **str** |  | 
**longitude** | **float** |  | 
**latitude** | **float** |  | 
**notes** | **str** |  | 
**pcap_mode** | [**SensorPcapMode**](SensorPcapMode.md) |  | 
**type** | **str** | The type of the resource. | 

## Example

```python
from pyhpeuxi.models.sensor_patch_response import SensorPatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SensorPatchResponse from a JSON string
sensor_patch_response_instance = SensorPatchResponse.from_json(json)
# print the JSON string representation of the object
print(SensorPatchResponse.to_json())

# convert the object into a dict
sensor_patch_response_dict = sensor_patch_response_instance.to_dict()
# create an instance of SensorPatchResponse from a dict
sensor_patch_response_from_dict = SensorPatchResponse.from_dict(sensor_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


