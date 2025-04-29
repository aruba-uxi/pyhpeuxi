# AgentGroupAssignmentPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The unique identifier of the group | 
**agent_id** | **str** | The unique identifier of the agent | 

## Example

```python
from pyhpeuxi.models.agent_group_assignment_post_request import AgentGroupAssignmentPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGroupAssignmentPostRequest from a JSON string
agent_group_assignment_post_request_instance = AgentGroupAssignmentPostRequest.from_json(json)
# print the JSON string representation of the object
print(AgentGroupAssignmentPostRequest.to_json())

# convert the object into a dict
agent_group_assignment_post_request_dict = agent_group_assignment_post_request_instance.to_dict()
# create an instance of AgentGroupAssignmentPostRequest from a dict
agent_group_assignment_post_request_from_dict = AgentGroupAssignmentPostRequest.from_dict(agent_group_assignment_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


