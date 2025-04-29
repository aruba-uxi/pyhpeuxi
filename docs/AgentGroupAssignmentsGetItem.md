# AgentGroupAssignmentsGetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the agent group assignment | 
**group** | [**AgentGroupAssignmentsGetGroup**](AgentGroupAssignmentsGetGroup.md) | The group component of the agent group assignment | 
**agent** | [**AgentGroupAssignmentsGetAgent**](AgentGroupAssignmentsGetAgent.md) | The agent component of the agent group assignment | 
**type** | **str** | The type of the resource. | 

## Example

```python
from pyhpeuxi.models.agent_group_assignments_get_item import AgentGroupAssignmentsGetItem

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGroupAssignmentsGetItem from a JSON string
agent_group_assignments_get_item_instance = AgentGroupAssignmentsGetItem.from_json(json)
# print the JSON string representation of the object
print(AgentGroupAssignmentsGetItem.to_json())

# convert the object into a dict
agent_group_assignments_get_item_dict = agent_group_assignments_get_item_instance.to_dict()
# create an instance of AgentGroupAssignmentsGetItem from a dict
agent_group_assignments_get_item_from_dict = AgentGroupAssignmentsGetItem.from_dict(agent_group_assignments_get_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


