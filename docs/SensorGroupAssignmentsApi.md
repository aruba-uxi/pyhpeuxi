# pyhpeuxi.SensorGroupAssignmentsApi

All URIs are relative to *https://api.capenetworks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sensor_group_assignment_delete**](SensorGroupAssignmentsApi.md#sensor_group_assignment_delete) | **DELETE** /networking-uxi/v1alpha1/sensor-group-assignments/{id} | Sensor Group Assignment Delete
[**sensor_group_assignment_post**](SensorGroupAssignmentsApi.md#sensor_group_assignment_post) | **POST** /networking-uxi/v1alpha1/sensor-group-assignments | Sensor Group Assignment Post
[**sensor_group_assignments_get**](SensorGroupAssignmentsApi.md#sensor_group_assignments_get) | **GET** /networking-uxi/v1alpha1/sensor-group-assignments | Sensor Group Assignments Get


# **sensor_group_assignment_delete**
> sensor_group_assignment_delete(id)

Sensor Group Assignment Delete

Delete the specified sensor group assignment

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
    api_instance = pyhpeuxi.SensorGroupAssignmentsApi(api_client)
    id = 'id_example' # str | The unique identifier of the sensor group assignment

    try:
        # Sensor Group Assignment Delete
        api_instance.sensor_group_assignment_delete(id)
    except Exception as e:
        print("Exception when calling SensorGroupAssignmentsApi->sensor_group_assignment_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the sensor group assignment | 

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

# **sensor_group_assignment_post**
> SensorGroupAssignmentPostResponse sensor_group_assignment_post(sensor_group_assignment_post_request)

Sensor Group Assignment Post

Create a sensor group assignment.

### Example

* Bearer Authentication (HTTPBearer):

```python
import pyhpeuxi
from pyhpeuxi.models.sensor_group_assignment_post_request import SensorGroupAssignmentPostRequest
from pyhpeuxi.models.sensor_group_assignment_post_response import SensorGroupAssignmentPostResponse
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
    api_instance = pyhpeuxi.SensorGroupAssignmentsApi(api_client)
    sensor_group_assignment_post_request = {"groupId":"dsfldjsah389","sensorId":"sensor-4gergsdgdf4tr"} # SensorGroupAssignmentPostRequest | 

    try:
        # Sensor Group Assignment Post
        api_response = api_instance.sensor_group_assignment_post(sensor_group_assignment_post_request)
        print("The response of SensorGroupAssignmentsApi->sensor_group_assignment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensorGroupAssignmentsApi->sensor_group_assignment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_group_assignment_post_request** | [**SensorGroupAssignmentPostRequest**](SensorGroupAssignmentPostRequest.md)|  | 

### Return type

[**SensorGroupAssignmentPostResponse**](SensorGroupAssignmentPostResponse.md)

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

# **sensor_group_assignments_get**
> SensorGroupAssignmentsGetResponse sensor_group_assignments_get(id=id, next=next, limit=limit)

Sensor Group Assignments Get

Get a list of sensor group assignments.

### Example

* Bearer Authentication (HTTPBearer):

```python
import pyhpeuxi
from pyhpeuxi.models.sensor_group_assignments_get_response import SensorGroupAssignmentsGetResponse
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
    api_instance = pyhpeuxi.SensorGroupAssignmentsApi(api_client)
    id = 'id_example' # str | The ID of the resource. (optional)
    next = 'next_example' # str | The next cursor for pagination. (optional)
    limit = 50 # int | The maximum number of items returned in the response. (optional) (default to 50)

    try:
        # Sensor Group Assignments Get
        api_response = api_instance.sensor_group_assignments_get(id=id, next=next, limit=limit)
        print("The response of SensorGroupAssignmentsApi->sensor_group_assignments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensorGroupAssignmentsApi->sensor_group_assignments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource. | [optional] 
 **next** | **str**| The next cursor for pagination. | [optional] 
 **limit** | **int**| The maximum number of items returned in the response. | [optional] [default to 50]

### Return type

[**SensorGroupAssignmentsGetResponse**](SensorGroupAssignmentsGetResponse.md)

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

