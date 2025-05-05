# (C) Copyright 2019-2025 Hewlett Packard Enterprise Development LP.
# Apache License 2.0

import json
from datetime import datetime, timedelta

import urllib3

from pyhpeuxi.configuration import BearerAuthSetting
from pyhpeuxi.exceptions import ApiException

urllib3.disable_warnings()

class TokenGenerator:
    def __init__(
        self,
        client_id,
        client_secret,
        oauth_token_url="https://sso.common.cloud.hpe.com/as/token.oauth2",
        verify_ssl=True,
    ) -> None:
        """
        This is the class constructor for HPE Aruba Networking User Experience Insight API Class.

        This constructor is required to be created before any modules can be used and must contain the following function arguments:

        Mandatory Parameters:
        client_id (string): oAuth API Client ID
        client_secret (string): oAuth API Client Secret

        Optional Parameters:
        url (string): Web Service for API Services  - https://api-dev.capenetworks.com
        verify_ssl (boolean): Validate web service cerificate - True/False
        oauth_token_url (string): URL for retrieving API Keys directly from GreenLake

        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.oauth_token_url = oauth_token_url
        self.verify_ssl = verify_ssl
        self.exires_at = 0
        self.access_token = None

    def _new_api_token(self):
        """
        Operation: Obtain an OAuth2 access token for making API calls
        Required Body Parameters: grant_type (string) = ['client_credentials']:
        Required Body Parameters: client_id (string): Client ID
        Required Body Parameters: client_secret (string): Client secret

        Required Body Parameters (type(dict) body example)- {
        "grant_type": "client_credentials",
        "client_id": "string",
        "client_secret": "string"
        }
        """

        try:
            # perform request and return response
            http = urllib3.PoolManager()

            response_data = http.request_encode_body(
                method="POST",
                url=self.oauth_token_url,
                encode_multipart=False,
                fields={"grant_type": "client_credentials", "client_id": self.client_id, "client_secret":self.client_secret},
                headers={"Content-Type": "application/x-www-form-urlencoded"}
            )

        except ApiException as e:
            raise e
        if response_data.status == 200:
            # Decode the response data
            try:
                decoded_response = json.loads(response_data.data.decode("utf-8"))
            except json.JSONDecodeError:
                raise ApiException(
                    status=response_data.status,
                    reason="Failed to decode JSON response",
                )
            if "expires_in" in decoded_response:
                expires_in = timedelta(seconds=int(decoded_response["expires_in"]))
                self.exires_at = datetime.now() + expires_in
            if "access_token" in decoded_response:
                self.access_token = decoded_response["access_token"]
            else:
                raise ApiException(
                    status=response_data.status,
                    reason="Access token not found in response",
                )

    def auth(self)-> BearerAuthSetting:
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        if self.access_token is None or self.exires_at < (datetime.now() + timedelta(seconds=1)):
            self._new_api_token()
        if self.access_token is None:
            raise ApiException(
                status=401,
                reason="Access token is not available",
            )
        auth: BearerAuthSetting = {}
        if self.access_token is not None:
            auth = {
                'type': 'bearer',
                'in': 'header',
                'key': 'Authorization',
                'value': 'Bearer ' + self.access_token
            }
        return auth
