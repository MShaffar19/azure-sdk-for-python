#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
Example to show managing queue entities under a ServiceBus Namespace, including
    - Create a queue
    - Get queue description and runtime information
    - Update a queue
    - Delete a queue
    - List queues under the given ServiceBus Namespace
"""

# pylint: disable=C0111

import os
from azure.servicebus.management import ServiceBusManagementClient, QueueDescription

CONNECTION_STR = os.environ['SERVICE_BUS_CONNECTION_STR']
QUEUE_NAME = "sb_mgmt_demo_queue"


def create_queue(servicebus_mgmt_client):
    print("-- Create Queue")
    queue_description = QueueDescription(QUEUE_NAME)
    # You can adjust the settings of a queue when creating.
    # Please refer to the QueueDescription class for available settings.
    queue_description.max_delivery_count = 10
    queue_description.dead_lettering_on_message_expiration = True

    servicebus_mgmt_client.create_queue(queue_description)
    print("Queue {} is created.".format(QUEUE_NAME))
    print("")


def delete_queue(servicebus_mgmt_client):
    print("-- Delete Queue")
    servicebus_mgmt_client.delete_queue(QUEUE_NAME)
    print("Queue {} is deleted.".format(QUEUE_NAME))
    print("")


def list_queues(servicebus_mgmt_client):
    print("-- List Queues")
    for queue_description in servicebus_mgmt_client.list_queues():
        print("Queue Name:", queue_description.name)
    print("")


def get_and_update_queue(servicebus_mgmt_client):
    print("-- Get and Update Queue")
    queue_description = servicebus_mgmt_client.get_queue(QUEUE_NAME)
    print("Queue Name:", queue_description.name)
    print("Queue Settings:")
    print("Auto Delete on Idle:", queue_description.auto_delete_on_idle)
    print("Default Message Time to Live:", queue_description.default_message_time_to_live)
    print("Dead Lettering on Message Expiration:", queue_description.dead_lettering_on_message_expiration)
    print("Please refer to QueueDescription for complete available settings.")
    print("")
    queue_description.max_delivery_count = 5
    servicebus_mgmt_client.update_queue(queue_description)


def get_queue_runtime_info(servicebus_mgmt_client):
    print("-- Get Queue Runtime Info")
    queue_runtime_info = servicebus_mgmt_client.get_queue_runtime_info(QUEUE_NAME)
    print("Queue Name:", queue_runtime_info.name)
    print("Queue Runtime Info:")
    print("Updated at:", queue_runtime_info.updated_at)
    print("Size in Bytes:", queue_runtime_info.size_in_bytes)
    print("Message Count:", queue_runtime_info.message_count)
    print("Please refer to QueueRuntimeInfo from complete available runtime information.")
    print("")


with ServiceBusManagementClient.from_connection_string(CONNECTION_STR) as servicebus_mgmt_client:
    create_queue(servicebus_mgmt_client)
    list_queues(servicebus_mgmt_client)
    get_and_update_queue(servicebus_mgmt_client)
    get_queue_runtime_info(servicebus_mgmt_client)
    delete_queue(servicebus_mgmt_client)
