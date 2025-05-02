import os
import time
from pprint import pprint

import pyhpeuxi
from pyhpeuxi.common import TokenGenerator
from pyhpeuxi.rest import ApiException

token_generator = TokenGenerator(
    client_id=os.environ["HPEUXI_CLIENT_ID"],
    client_secret=os.environ["HPEUXI_CLIENT_SECRET"],
    verify_ssl=False)

# Defining the host is optional and defaults to https://api.capenetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pyhpeuxi.Configuration(
    host = "https://api.capenetworks.com",
    access_token=token_generator.token(),
)

if __name__ == "__main__":
    # Enter a context with an instance of the API client
    with pyhpeuxi.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = pyhpeuxi.V1alpha1Api(api_client)
        while(True):
            try:
                groups = api_instance.groups_get()
                pprint(groups)
                wireless_networks = api_instance.wireless_networks_get()
                pprint(wireless_networks)
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                print("sleeping for 5 minutes")
                time.sleep(300)
            except ApiException as e:
                print("Exception when calling groups_get: %s\n" % e)
