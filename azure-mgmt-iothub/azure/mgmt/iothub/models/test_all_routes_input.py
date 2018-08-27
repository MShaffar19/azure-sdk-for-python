# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TestAllRoutesInput(Model):
    """Input for testing all routes.

    :param routing_source: Routing source. Possible values include: 'Invalid',
     'DeviceMessages', 'TwinChangeEvents', 'DeviceLifecycleEvents',
     'DeviceJobLifecycleEvents'
    :type routing_source: str or ~azure.mgmt.iothub.models.RoutingSource
    :param message: Routing message
    :type message: ~azure.mgmt.iothub.models.RoutingMessage
    """

    _attribute_map = {
        'routing_source': {'key': 'routingSource', 'type': 'str'},
        'message': {'key': 'message', 'type': 'RoutingMessage'},
    }

    def __init__(self, **kwargs):
        super(TestAllRoutesInput, self).__init__(**kwargs)
        self.routing_source = kwargs.get('routing_source', None)
        self.message = kwargs.get('message', None)
