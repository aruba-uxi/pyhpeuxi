# ServiceTestsGetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the service test | 
**category** | **str** | The category of the service test | 
**name** | **str** | The name of the service test | 
**target** | **str** |  | 
**template** | **str** | The template of the service test | 
**is_enabled** | **bool** | Indicates if the service test is enabled | 
**type** | **str** | The type of the resource. | 

## Example

```python
from pyhpeuxi.models.service_tests_get_item import ServiceTestsGetItem

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTestsGetItem from a JSON string
service_tests_get_item_instance = ServiceTestsGetItem.from_json(json)
# print the JSON string representation of the object
print(ServiceTestsGetItem.to_json())

# convert the object into a dict
service_tests_get_item_dict = service_tests_get_item_instance.to_dict()
# create an instance of ServiceTestsGetItem from a dict
service_tests_get_item_from_dict = ServiceTestsGetItem.from_dict(service_tests_get_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


