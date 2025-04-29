# AgentsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AgentsGetItem]**](AgentsGetItem.md) | The list of resources. | 
**count** | **int** | The number of resources returned in the response. | 
**next** | **str** |  | 

## Example

```python
from pyhpeuxi.models.agents_get_response import AgentsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentsGetResponse from a JSON string
agents_get_response_instance = AgentsGetResponse.from_json(json)
# print the JSON string representation of the object
print(AgentsGetResponse.to_json())

# convert the object into a dict
agents_get_response_dict = agents_get_response_instance.to_dict()
# create an instance of AgentsGetResponse from a dict
agents_get_response_from_dict = AgentsGetResponse.from_dict(agents_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


