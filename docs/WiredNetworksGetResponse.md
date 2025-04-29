# WiredNetworksGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[WiredNetworksGetItem]**](WiredNetworksGetItem.md) | The list of resources. | 
**count** | **int** | The number of resources returned in the response. | 
**next** | **str** |  | 

## Example

```python
from pyhpeuxi.models.wired_networks_get_response import WiredNetworksGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WiredNetworksGetResponse from a JSON string
wired_networks_get_response_instance = WiredNetworksGetResponse.from_json(json)
# print the JSON string representation of the object
print(WiredNetworksGetResponse.to_json())

# convert the object into a dict
wired_networks_get_response_dict = wired_networks_get_response_instance.to_dict()
# create an instance of WiredNetworksGetResponse from a dict
wired_networks_get_response_from_dict = WiredNetworksGetResponse.from_dict(wired_networks_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


