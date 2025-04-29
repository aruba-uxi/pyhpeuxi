# SensorsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SensorsGetItem]**](SensorsGetItem.md) | The list of resources. | 
**count** | **int** | The number of resources returned in the response. | 
**next** | **str** |  | 

## Example

```python
from pyhpeuxi.models.sensors_get_response import SensorsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SensorsGetResponse from a JSON string
sensors_get_response_instance = SensorsGetResponse.from_json(json)
# print the JSON string representation of the object
print(SensorsGetResponse.to_json())

# convert the object into a dict
sensors_get_response_dict = sensors_get_response_instance.to_dict()
# create an instance of SensorsGetResponse from a dict
sensors_get_response_from_dict = SensorsGetResponse.from_dict(sensors_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


