import pyhpeuxi
from pyhpeuxi.rest import ApiException
from pprint import pprint
import os

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


if __name__ == "__main__":
    # Enter a context with an instance of the API client
    with pyhpeuxi.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = pyhpeuxi.V1alpha1Api(api_client)

        try:
            groups = api_instance.groups_get()
            pprint(groups)
        except ApiException as e:
            print("Exception when calling groups_get: %s\n" % e)
