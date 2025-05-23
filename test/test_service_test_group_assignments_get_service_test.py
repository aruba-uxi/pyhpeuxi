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

from pyhpeuxi.models.service_test_group_assignments_get_service_test import ServiceTestGroupAssignmentsGetServiceTest

class TestServiceTestGroupAssignmentsGetServiceTest(unittest.TestCase):
    """ServiceTestGroupAssignmentsGetServiceTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceTestGroupAssignmentsGetServiceTest:
        """Test ServiceTestGroupAssignmentsGetServiceTest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceTestGroupAssignmentsGetServiceTest`
        """
        model = ServiceTestGroupAssignmentsGetServiceTest()
        if include_optional:
            return ServiceTestGroupAssignmentsGetServiceTest(
                id = ''
            )
        else:
            return ServiceTestGroupAssignmentsGetServiceTest(
                id = '',
        )
        """

    def testServiceTestGroupAssignmentsGetServiceTest(self):
        """Test ServiceTestGroupAssignmentsGetServiceTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
