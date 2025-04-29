# WirelessNetworksGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[WirelessNetworksGetItem]**](WirelessNetworksGetItem.md) | The list of resources. | 
**count** | **int** | The number of resources returned in the response. | 
**next** | **str** |  | 

## Example

```python
from pyhpeuxi.models.wireless_networks_get_response import WirelessNetworksGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WirelessNetworksGetResponse from a JSON string
wireless_networks_get_response_instance = WirelessNetworksGetResponse.from_json(json)
# print the JSON string representation of the object
print(WirelessNetworksGetResponse.to_json())

# convert the object into a dict
wireless_networks_get_response_dict = wireless_networks_get_response_instance.to_dict()
# create an instance of WirelessNetworksGetResponse from a dict
wireless_networks_get_response_from_dict = WirelessNetworksGetResponse.from_dict(wireless_networks_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


