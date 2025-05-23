#
# Copyright 2025 Hewlett Packard Enterprise Development LP.
#

# coding: utf-8

# flake8: noqa
"""
    HPE Aruba Networking UXI Configuration

    This document outlines the API contracts for HPE Aruba Networking UXI.

    The version of the OpenAPI document: 6.5.0
    Contact: support@capenetworks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from pyhpeuxi.models.agent_group_assignment_post_agent import AgentGroupAssignmentPostAgent
from pyhpeuxi.models.agent_group_assignment_post_group import AgentGroupAssignmentPostGroup
from pyhpeuxi.models.agent_group_assignment_post_request import AgentGroupAssignmentPostRequest
from pyhpeuxi.models.agent_group_assignment_post_response import AgentGroupAssignmentPostResponse
from pyhpeuxi.models.agent_group_assignments_get_agent import AgentGroupAssignmentsGetAgent
from pyhpeuxi.models.agent_group_assignments_get_group import AgentGroupAssignmentsGetGroup
from pyhpeuxi.models.agent_group_assignments_get_item import AgentGroupAssignmentsGetItem
from pyhpeuxi.models.agent_group_assignments_get_response import AgentGroupAssignmentsGetResponse
from pyhpeuxi.models.agent_patch_request import AgentPatchRequest
from pyhpeuxi.models.agent_patch_response import AgentPatchResponse
from pyhpeuxi.models.agent_pcap_mode import AgentPcapMode
from pyhpeuxi.models.agents_get_item import AgentsGetItem
from pyhpeuxi.models.agents_get_response import AgentsGetResponse
from pyhpeuxi.models.error_detail import ErrorDetail
from pyhpeuxi.models.error_response import ErrorResponse
from pyhpeuxi.models.group_patch_parent import GroupPatchParent
from pyhpeuxi.models.group_patch_request import GroupPatchRequest
from pyhpeuxi.models.group_patch_response import GroupPatchResponse
from pyhpeuxi.models.group_post_parent import GroupPostParent
from pyhpeuxi.models.group_post_request import GroupPostRequest
from pyhpeuxi.models.group_post_response import GroupPostResponse
from pyhpeuxi.models.groups_get_item import GroupsGetItem
from pyhpeuxi.models.groups_get_parent import GroupsGetParent
from pyhpeuxi.models.groups_get_response import GroupsGetResponse
from pyhpeuxi.models.http_validation_error import HTTPValidationError
from pyhpeuxi.models.ip_version import IpVersion
from pyhpeuxi.models.issue import Issue
from pyhpeuxi.models.issue_subject import IssueSubject
from pyhpeuxi.models.network_group_assignment_post_group import NetworkGroupAssignmentPostGroup
from pyhpeuxi.models.network_group_assignment_post_network import NetworkGroupAssignmentPostNetwork
from pyhpeuxi.models.network_group_assignment_post_request import NetworkGroupAssignmentPostRequest
from pyhpeuxi.models.network_group_assignment_post_response import NetworkGroupAssignmentPostResponse
from pyhpeuxi.models.network_group_assignments_get_group import NetworkGroupAssignmentsGetGroup
from pyhpeuxi.models.network_group_assignments_get_item import NetworkGroupAssignmentsGetItem
from pyhpeuxi.models.network_group_assignments_get_network import NetworkGroupAssignmentsGetNetwork
from pyhpeuxi.models.network_group_assignments_get_response import NetworkGroupAssignmentsGetResponse
from pyhpeuxi.models.sensor_group_assignment_post_group import SensorGroupAssignmentPostGroup
from pyhpeuxi.models.sensor_group_assignment_post_request import SensorGroupAssignmentPostRequest
from pyhpeuxi.models.sensor_group_assignment_post_response import SensorGroupAssignmentPostResponse
from pyhpeuxi.models.sensor_group_assignment_post_sensor import SensorGroupAssignmentPostSensor
from pyhpeuxi.models.sensor_group_assignments_get_group import SensorGroupAssignmentsGetGroup
from pyhpeuxi.models.sensor_group_assignments_get_item import SensorGroupAssignmentsGetItem
from pyhpeuxi.models.sensor_group_assignments_get_response import SensorGroupAssignmentsGetResponse
from pyhpeuxi.models.sensor_group_assignments_get_sensor import SensorGroupAssignmentsGetSensor
from pyhpeuxi.models.sensor_patch_request import SensorPatchRequest
from pyhpeuxi.models.sensor_patch_response import SensorPatchResponse
from pyhpeuxi.models.sensor_pcap_mode import SensorPcapMode
from pyhpeuxi.models.sensors_get_item import SensorsGetItem
from pyhpeuxi.models.sensors_get_response import SensorsGetResponse
from pyhpeuxi.models.service_test_group_assignment_post_group import ServiceTestGroupAssignmentPostGroup
from pyhpeuxi.models.service_test_group_assignment_post_request import ServiceTestGroupAssignmentPostRequest
from pyhpeuxi.models.service_test_group_assignment_post_response import ServiceTestGroupAssignmentPostResponse
from pyhpeuxi.models.service_test_group_assignment_post_service_test import ServiceTestGroupAssignmentPostServiceTest
from pyhpeuxi.models.service_test_group_assignments_get_group import ServiceTestGroupAssignmentsGetGroup
from pyhpeuxi.models.service_test_group_assignments_get_item import ServiceTestGroupAssignmentsGetItem
from pyhpeuxi.models.service_test_group_assignments_get_response import ServiceTestGroupAssignmentsGetResponse
from pyhpeuxi.models.service_test_group_assignments_get_service_test import ServiceTestGroupAssignmentsGetServiceTest
from pyhpeuxi.models.service_tests_get_item import ServiceTestsGetItem
from pyhpeuxi.models.service_tests_get_response import ServiceTestsGetResponse
from pyhpeuxi.models.validation_error import ValidationError
from pyhpeuxi.models.validation_error_loc_inner import ValidationErrorLocInner
from pyhpeuxi.models.wired_networks_get_item import WiredNetworksGetItem
from pyhpeuxi.models.wired_networks_get_response import WiredNetworksGetResponse
from pyhpeuxi.models.wireless_networks_get_item import WirelessNetworksGetItem
from pyhpeuxi.models.wireless_networks_get_response import WirelessNetworksGetResponse
