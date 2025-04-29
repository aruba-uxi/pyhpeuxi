# ServiceTestsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ServiceTestsGetItem]**](ServiceTestsGetItem.md) | The list of resources. | 
**count** | **int** | The number of resources returned in the response. | 
**next** | **str** |  | 

## Example

```python
from pyhpeuxi.models.service_tests_get_response import ServiceTestsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTestsGetResponse from a JSON string
service_tests_get_response_instance = ServiceTestsGetResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceTestsGetResponse.to_json())

# convert the object into a dict
service_tests_get_response_dict = service_tests_get_response_instance.to_dict()
# create an instance of ServiceTestsGetResponse from a dict
service_tests_get_response_from_dict = ServiceTestsGetResponse.from_dict(service_tests_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


