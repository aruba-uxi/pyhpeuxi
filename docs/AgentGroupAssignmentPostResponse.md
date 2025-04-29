# AgentGroupAssignmentPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the agent group assignment | 
**group** | [**AgentGroupAssignmentPostGroup**](AgentGroupAssignmentPostGroup.md) | The group component of the agent group assignment | 
**agent** | [**AgentGroupAssignmentPostAgent**](AgentGroupAssignmentPostAgent.md) | The agent component of the agent group assignment | 
**type** | **str** | The type of the resource. | 

## Example

```python
from pyhpeuxi.models.agent_group_assignment_post_response import AgentGroupAssignmentPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGroupAssignmentPostResponse from a JSON string
agent_group_assignment_post_response_instance = AgentGroupAssignmentPostResponse.from_json(json)
# print the JSON string representation of the object
print(AgentGroupAssignmentPostResponse.to_json())

# convert the object into a dict
agent_group_assignment_post_response_dict = agent_group_assignment_post_response_instance.to_dict()
# create an instance of AgentGroupAssignmentPostResponse from a dict
agent_group_assignment_post_response_from_dict = AgentGroupAssignmentPostResponse.from_dict(agent_group_assignment_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


