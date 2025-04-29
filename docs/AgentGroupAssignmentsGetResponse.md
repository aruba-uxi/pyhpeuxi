# AgentGroupAssignmentsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AgentGroupAssignmentsGetItem]**](AgentGroupAssignmentsGetItem.md) | The list of resources. | 
**count** | **int** | The number of resources returned in the response. | 
**next** | **str** |  | 

## Example

```python
from pyhpeuxi.models.agent_group_assignments_get_response import AgentGroupAssignmentsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGroupAssignmentsGetResponse from a JSON string
agent_group_assignments_get_response_instance = AgentGroupAssignmentsGetResponse.from_json(json)
# print the JSON string representation of the object
print(AgentGroupAssignmentsGetResponse.to_json())

# convert the object into a dict
agent_group_assignments_get_response_dict = agent_group_assignments_get_response_instance.to_dict()
# create an instance of AgentGroupAssignmentsGetResponse from a dict
agent_group_assignments_get_response_from_dict = AgentGroupAssignmentsGetResponse.from_dict(agent_group_assignments_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


