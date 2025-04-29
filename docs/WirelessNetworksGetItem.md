# WirelessNetworksGetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the wireless network | 
**name** | **str** | The name of the wireless network | 
**ssid** | **str** | The SSID of the wireless network | 
**security** | **str** |  | 
**ip_version** | [**IpVersion**](IpVersion.md) | The IP version of the wireless network | 
**created_at** | **datetime** | The creation timestamp of the wireless network | 
**updated_at** | **datetime** | The last update timestamp of the wireless network | 
**hidden** | **bool** | Whether the wireless network is hidden | 
**band_locking** | **str** | The band locking setting of the wireless network | 
**dns_lookup_domain** | **str** |  | 
**disable_edns** | **bool** | Whether EDNS is disabled for the wireless network | 
**use_dns64** | **bool** | Whether DNS64 is used for the wireless network | 
**external_connectivity** | **bool** | Whether the wireless network has external connectivity | 
**type** | **str** | The type of the resource. | 

## Example

```python
from pyhpeuxi.models.wireless_networks_get_item import WirelessNetworksGetItem

# TODO update the JSON string below
json = "{}"
# create an instance of WirelessNetworksGetItem from a JSON string
wireless_networks_get_item_instance = WirelessNetworksGetItem.from_json(json)
# print the JSON string representation of the object
print(WirelessNetworksGetItem.to_json())

# convert the object into a dict
wireless_networks_get_item_dict = wireless_networks_get_item_instance.to_dict()
# create an instance of WirelessNetworksGetItem from a dict
wireless_networks_get_item_from_dict = WirelessNetworksGetItem.from_dict(wireless_networks_get_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


