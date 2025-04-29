# AgentPatchResponse


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
from pyhpeuxi.models.agent_patch_response import AgentPatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentPatchResponse from a JSON string
agent_patch_response_instance = AgentPatchResponse.from_json(json)
# print the JSON string representation of the object
print(AgentPatchResponse.to_json())

# convert the object into a dict
agent_patch_response_dict = agent_patch_response_instance.to_dict()
# create an instance of AgentPatchResponse from a dict
agent_patch_response_from_dict = AgentPatchResponse.from_dict(agent_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


