#
# Copyright 2025 Hewlett Packard Enterprise Development LP.
#

# coding: utf-8

"""
    HPE Aruba Networking UXI Configuration

    This document outlines the API contracts for HPE Aruba Networking UXI.

    The version of the OpenAPI document: 6.6.0
    Contact: support@capenetworks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyhpeuxi.models.sensors_get_item import SensorsGetItem

class TestSensorsGetItem(unittest.TestCase):
    """SensorsGetItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SensorsGetItem:
        """Test SensorsGetItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SensorsGetItem`
        """
        model = SensorsGetItem()
        if include_optional:
            return SensorsGetItem(
                id = '',
                serial = '',
                name = '',
                model_number = '',
                wifi_mac_address = '',
                ethernet_mac_address = '',
                address_note = '',
                longitude = 1.337,
                latitude = 1.337,
                notes = '',
                pcap_mode = 'light',
                type = 'networking-uxi/sensor'
            )
        else:
            return SensorsGetItem(
                id = '',
                serial = '',
                name = '',
                model_number = '',
                wifi_mac_address = '',
                ethernet_mac_address = '',
                address_note = '',
                longitude = 1.337,
                latitude = 1.337,
                notes = '',
                pcap_mode = 'light',
                type = 'networking-uxi/sensor',
        )
        """

    def testSensorsGetItem(self):
        """Test SensorsGetItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
