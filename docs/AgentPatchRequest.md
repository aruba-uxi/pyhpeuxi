# AgentPatchRequest

Request body for patching an agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the agent | [optional] 
**notes** | **str** | The notes of the agent | [optional] 
**pcap_mode** | [**AgentPcapMode**](AgentPcapMode.md) | The pcap mode of the agent | [optional] 

## Example

```python
from pyhpeuxi.models.agent_patch_request import AgentPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentPatchRequest from a JSON string
agent_patch_request_instance = AgentPatchRequest.from_json(json)
# print the JSON string representation of the object
print(AgentPatchRequest.to_json())

# convert the object into a dict
agent_patch_request_dict = agent_patch_request_instance.to_dict()
# create an instance of AgentPatchRequest from a dict
agent_patch_request_from_dict = AgentPatchRequest.from_dict(agent_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


