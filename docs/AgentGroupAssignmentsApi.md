# pyhpeuxi.AgentGroupAssignmentsApi

All URIs are relative to *https://api.capenetworks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_group_assignment_delete**](AgentGroupAssignmentsApi.md#agent_group_assignment_delete) | **DELETE** /networking-uxi/v1alpha1/agent-group-assignments/{id} | Agent Group Assignment Delete
[**agent_group_assignment_post**](AgentGroupAssignmentsApi.md#agent_group_assignment_post) | **POST** /networking-uxi/v1alpha1/agent-group-assignments | Agent Group Assignment Post
[**agent_group_assignments_get**](AgentGroupAssignmentsApi.md#agent_group_assignments_get) | **GET** /networking-uxi/v1alpha1/agent-group-assignments | Agent Group Assignments Get


# **agent_group_assignment_delete**
> agent_group_assignment_delete(id)

Agent Group Assignment Delete

Delete the specified agent group assignment

### Example

* Bearer Authentication (HTTPBearer):

```python
import pyhpeuxi
from pyhpeuxi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.capenetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pyhpeuxi.Configuration(
    host = "https://api.capenetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = pyhpeuxi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pyhpeuxi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyhpeuxi.AgentGroupAssignmentsApi(api_client)
    id = 'id_example' # str | The unique identifier of the assignment

    try:
        # Agent Group Assignment Delete
        api_instance.agent_group_assignment_delete(id)
    except Exception as e:
        print("Exception when calling AgentGroupAssignmentsApi->agent_group_assignment_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the assignment | 

### Return type

void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_group_assignment_post**
> AgentGroupAssignmentPostResponse agent_group_assignment_post(agent_group_assignment_post_request)

Agent Group Assignment Post

Create an agent group assignment

### Example

* Bearer Authentication (HTTPBearer):

```python
import pyhpeuxi
from pyhpeuxi.models.agent_group_assignment_post_request import AgentGroupAssignmentPostRequest
from pyhpeuxi.models.agent_group_assignment_post_response import AgentGroupAssignmentPostResponse
from pyhpeuxi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.capenetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pyhpeuxi.Configuration(
    host = "https://api.capenetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = pyhpeuxi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pyhpeuxi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyhpeuxi.AgentGroupAssignmentsApi(api_client)
    agent_group_assignment_post_request = {"groupId":"e0f97a387c31","agentId":"0f4c2917-9886-41bf-8ea6-faaea9fddbf0"} # AgentGroupAssignmentPostRequest | 

    try:
        # Agent Group Assignment Post
        api_response = api_instance.agent_group_assignment_post(agent_group_assignment_post_request)
        print("The response of AgentGroupAssignmentsApi->agent_group_assignment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentGroupAssignmentsApi->agent_group_assignment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_group_assignment_post_request** | [**AgentGroupAssignmentPostRequest**](AgentGroupAssignmentPostRequest.md)|  | 

### Return type

[**AgentGroupAssignmentPostResponse**](AgentGroupAssignmentPostResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**405** | Method Not Allowed |  -  |
**409** | Conflict |  -  |
**415** | Unsupported Media Type |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_group_assignments_get**
> AgentGroupAssignmentsGetResponse agent_group_assignments_get(id=id, next=next, limit=limit)

Agent Group Assignments Get

Get a list of agent group assignments

### Example

* Bearer Authentication (HTTPBearer):

```python
import pyhpeuxi
from pyhpeuxi.models.agent_group_assignments_get_response import AgentGroupAssignmentsGetResponse
from pyhpeuxi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.capenetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pyhpeuxi.Configuration(
    host = "https://api.capenetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = pyhpeuxi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pyhpeuxi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyhpeuxi.AgentGroupAssignmentsApi(api_client)
    id = 'id_example' # str | The ID of the resource. (optional)
    next = 'next_example' # str | The next cursor for pagination. (optional)
    limit = 50 # int | The maximum number of items returned in the response. (optional) (default to 50)

    try:
        # Agent Group Assignments Get
        api_response = api_instance.agent_group_assignments_get(id=id, next=next, limit=limit)
        print("The response of AgentGroupAssignmentsApi->agent_group_assignments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentGroupAssignmentsApi->agent_group_assignments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource. | [optional] 
 **next** | **str**| The next cursor for pagination. | [optional] 
 **limit** | **int**| The maximum number of items returned in the response. | [optional] [default to 50]

### Return type

[**AgentGroupAssignmentsGetResponse**](AgentGroupAssignmentsGetResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

