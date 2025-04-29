# pyhpeuxi.WirelessNetworksApi

All URIs are relative to *https://api.capenetworks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wireless_networks_get**](WirelessNetworksApi.md#wireless_networks_get) | **GET** /networking-uxi/v1alpha1/wireless-networks | Wireless Networks Get


# **wireless_networks_get**
> WirelessNetworksGetResponse wireless_networks_get(id=id, next=next, limit=limit)

Wireless Networks Get

Get a list of wireless networks

### Example

* Bearer Authentication (HTTPBearer):

```python
import pyhpeuxi
from pyhpeuxi.models.wireless_networks_get_response import WirelessNetworksGetResponse
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
    api_instance = pyhpeuxi.WirelessNetworksApi(api_client)
    id = 'id_example' # str | The ID of the resource. (optional)
    next = 'next_example' # str | The next cursor for pagination. (optional)
    limit = 50 # int | The maximum number of items returned in the response. (optional) (default to 50)

    try:
        # Wireless Networks Get
        api_response = api_instance.wireless_networks_get(id=id, next=next, limit=limit)
        print("The response of WirelessNetworksApi->wireless_networks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WirelessNetworksApi->wireless_networks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource. | [optional] 
 **next** | **str**| The next cursor for pagination. | [optional] 
 **limit** | **int**| The maximum number of items returned in the response. | [optional] [default to 50]

### Return type

[**WirelessNetworksGetResponse**](WirelessNetworksGetResponse.md)

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

