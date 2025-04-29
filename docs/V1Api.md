# pyhpeuxi.V1Api

All URIs are relative to *https://api.capenetworks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sensor_patch**](V1Api.md#sensor_patch) | **PATCH** /networking-uxi/v1alpha1/sensors/{id} | Sensor Patch


# **sensor_patch**
> SensorPatchResponse sensor_patch(id, sensor_patch_request)

Sensor Patch

Update the properties of a sensor.

### Example

* Bearer Authentication (HTTPBearer):

```python
import pyhpeuxi
from pyhpeuxi.models.sensor_patch_request import SensorPatchRequest
from pyhpeuxi.models.sensor_patch_response import SensorPatchResponse
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
    api_instance = pyhpeuxi.V1Api(api_client)
    id = 'id_example' # str | The unique identifier of the sensor
    sensor_patch_request = {"name":"Updated Agent Name","pcapMode":"off","notes":"Updated notes","addressNote":"Updated address note"} # SensorPatchRequest | 

    try:
        # Sensor Patch
        api_response = api_instance.sensor_patch(id, sensor_patch_request)
        print("The response of V1Api->sensor_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->sensor_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the sensor | 
 **sensor_patch_request** | [**SensorPatchRequest**](SensorPatchRequest.md)|  | 

### Return type

[**SensorPatchResponse**](SensorPatchResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
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

