# WiredNetworksGetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the wired network | 
**name** | **str** | The name of the wired network | 
**ip_version** | [**IpVersion**](IpVersion.md) | The IP version of the wired network | 
**created_at** | **datetime** | The creation timestamp of the wired network | 
**updated_at** | **datetime** | The last update timestamp of the wired network | 
**security** | **str** |  | 
**dns_lookup_domain** | **str** |  | 
**disable_edns** | **bool** | Whether EDNS is disabled for the wired network | 
**use_dns64** | **bool** | Whether DNS64 is used for the wired network | 
**external_connectivity** | **bool** | Whether the wired network has external connectivity | 
**v_lan_id** | **int** |  | 
**type** | **str** | The type of the resource. | 

## Example

```python
from pyhpeuxi.models.wired_networks_get_item import WiredNetworksGetItem

# TODO update the JSON string below
json = "{}"
# create an instance of WiredNetworksGetItem from a JSON string
wired_networks_get_item_instance = WiredNetworksGetItem.from_json(json)
# print the JSON string representation of the object
print(WiredNetworksGetItem.to_json())

# convert the object into a dict
wired_networks_get_item_dict = wired_networks_get_item_instance.to_dict()
# create an instance of WiredNetworksGetItem from a dict
wired_networks_get_item_from_dict = WiredNetworksGetItem.from_dict(wired_networks_get_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


