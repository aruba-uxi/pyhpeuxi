# pyhpeuxi.NetworkGroupAssignmentsApi

All URIs are relative to *https://api.capenetworks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_group_assignment_delete**](NetworkGroupAssignmentsApi.md#network_group_assignment_delete) | **DELETE** /networking-uxi/v1alpha1/network-group-assignments/{id} | Network Group Assignment Delete
[**network_group_assignment_post**](NetworkGroupAssignmentsApi.md#network_group_assignment_post) | **POST** /networking-uxi/v1alpha1/network-group-assignments | Network Group Assignment Post
[**network_group_assignments_get**](NetworkGroupAssignmentsApi.md#network_group_assignments_get) | **GET** /networking-uxi/v1alpha1/network-group-assignments | Network Group Assignments Get


# **network_group_assignment_delete**
> network_group_assignment_delete(id)

Network Group Assignment Delete

Delete the specified network group assignment

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
    api_instance = pyhpeuxi.NetworkGroupAssignmentsApi(api_client)
    id = 'id_example' # str | The unique identifier of the network group assignment

    try:
        # Network Group Assignment Delete
        api_instance.network_group_assignment_delete(id)
    except Exception as e:
        print("Exception when calling NetworkGroupAssignmentsApi->network_group_assignment_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the network group assignment | 

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
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_group_assignment_post**
> NetworkGroupAssignmentPostResponse network_group_assignment_post(network_group_assignment_post_request)

Network Group Assignment Post

Create a network group assignment.

### Example

* Bearer Authentication (HTTPBearer):

```python
import pyhpeuxi
from pyhpeuxi.models.network_group_assignment_post_request import NetworkGroupAssignmentPostRequest
from pyhpeuxi.models.network_group_assignment_post_response import NetworkGroupAssignmentPostResponse
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
    api_instance = pyhpeuxi.NetworkGroupAssignmentsApi(api_client)
    network_group_assignment_post_request = {"groupId":"dsfldjsah389","networkId":"ssid-4gergsdgdf4tr"} # NetworkGroupAssignmentPostRequest | 

    try:
        # Network Group Assignment Post
        api_response = api_instance.network_group_assignment_post(network_group_assignment_post_request)
        print("The response of NetworkGroupAssignmentsApi->network_group_assignment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkGroupAssignmentsApi->network_group_assignment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_group_assignment_post_request** | [**NetworkGroupAssignmentPostRequest**](NetworkGroupAssignmentPostRequest.md)|  | 

### Return type

[**NetworkGroupAssignmentPostResponse**](NetworkGroupAssignmentPostResponse.md)

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

# **network_group_assignments_get**
> NetworkGroupAssignmentsGetResponse network_group_assignments_get(id=id, next=next, limit=limit)

Network Group Assignments Get

Get a list of network group assignments.

### Example

* Bearer Authentication (HTTPBearer):

```python
import pyhpeuxi
from pyhpeuxi.models.network_group_assignments_get_response import NetworkGroupAssignmentsGetResponse
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
    api_instance = pyhpeuxi.NetworkGroupAssignmentsApi(api_client)
    id = 'id_example' # str | The ID of the resource. (optional)
    next = 'next_example' # str | The next cursor for pagination. (optional)
    limit = 50 # int | The maximum number of items returned in the response. (optional) (default to 50)

    try:
        # Network Group Assignments Get
        api_response = api_instance.network_group_assignments_get(id=id, next=next, limit=limit)
        print("The response of NetworkGroupAssignmentsApi->network_group_assignments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkGroupAssignmentsApi->network_group_assignments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource. | [optional] 
 **next** | **str**| The next cursor for pagination. | [optional] 
 **limit** | **int**| The maximum number of items returned in the response. | [optional] [default to 50]

### Return type

[**NetworkGroupAssignmentsGetResponse**](NetworkGroupAssignmentsGetResponse.md)

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

