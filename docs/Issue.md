# Issue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**subject** | [**IssueSubject**](IssueSubject.md) |  | 
**source** | **str** |  | 

## Example

```python
from pyhpeuxi.models.issue import Issue

# TODO update the JSON string below
json = "{}"
# create an instance of Issue from a JSON string
issue_instance = Issue.from_json(json)
# print the JSON string representation of the object
print(Issue.to_json())

# convert the object into a dict
issue_dict = issue_instance.to_dict()
# create an instance of Issue from a dict
issue_from_dict = Issue.from_dict(issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


