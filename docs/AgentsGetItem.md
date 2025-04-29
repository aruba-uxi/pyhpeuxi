# AgentsGetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the agent | 
**serial** | **str** | The serial number of the agent | 
**name** | **str** | The name of the agent | 
**model_number** | **str** |  | 
**wifi_mac_address** | **str** |  | 
**ethernet_mac_address** | **str** |  | 
**notes** | **str** |  | 
**pcap_mode** | [**AgentPcapMode**](AgentPcapMode.md) |  | 
**type** | **str** | The type of the resource. | 

## Example

```python
from pyhpeuxi.models.agents_get_item import AgentsGetItem

# TODO update the JSON string below
json = "{}"
# create an instance of AgentsGetItem from a JSON string
agents_get_item_instance = AgentsGetItem.from_json(json)
# print the JSON string representation of the object
print(AgentsGetItem.to_json())

# convert the object into a dict
agents_get_item_dict = agents_get_item_instance.to_dict()
# create an instance of AgentsGetItem from a dict
agents_get_item_from_dict = AgentsGetItem.from_dict(agents_get_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


