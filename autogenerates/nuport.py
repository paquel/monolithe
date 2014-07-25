# -*- coding: utf-8 -*-

from ..fetchers import NUAlarmsFetcher
from ..fetchers import NUEnterprisePermissionsFetcher
from ..fetchers import NUVlansFetcher
from ..fetchers import NUPermittedActionsFetcher

from restnuage import NURESTObject


class NUPort(NURESTObject):
    """ Represents a Port object """

    def __init__(self):
        """ Initializing object """

        super(NUPort, self).__init__()

        # Read/Write Attributes
        
        self.template_id = None
        self.name = None
        self.permitted_action = None
        self.physical_name = None
        self.port_type = None
        self.status = None
        self.user_mnemonic = None
        self.use_user_mnemonic = None
        self.description = None
        self.vlan_range = None
        
        self.expose_attribute(local_name=u"template_id", remote_name=u"templateID", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"permitted_action", remote_name=u"permittedAction", attribute_type=str)
        self.expose_attribute(local_name=u"physical_name", remote_name=u"physicalName", attribute_type=str)
        self.expose_attribute(local_name=u"port_type", remote_name=u"portType", attribute_type=str)
        self.expose_attribute(local_name=u"status", remote_name=u"status", attribute_type=str)
        self.expose_attribute(local_name=u"user_mnemonic", remote_name=u"userMnemonic", attribute_type=str)
        self.expose_attribute(local_name=u"use_user_mnemonic", remote_name=u"useUserMnemonic", attribute_type=bool)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"vlan_range", remote_name=u"VLANRange", attribute_type=str)

        # Fetchers
        
        self.alarms = []
        self._alarms_fetcher = NUAlarmsFetcher.fetcher_with_entity(entity=self, local_name=u"alarms")
        
        self.enterprisepermissions = []
        self._enterprisepermissions_fetcher = NUEnterprisePermissionsFetcher.fetcher_with_entity(entity=self, local_name=u"enterprisepermissions")
        
        self.vlans = []
        self._vlans_fetcher = NUVlansFetcher.fetcher_with_entity(entity=self, local_name=u"vlans")
        
        self.permissions = []
        self._permissions_fetcher = NUPermittedActionsFetcher.fetcher_with_entity(entity=self, local_name=u"permissions")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"port"

    # REST methods
    
    def create_alarm(self, alarm, async=False, callback=None):
        """ Create a alarm
            :param alarm: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=alarm, async=async, callback=callback)

    def delete_alarm(self, alarm, async=False, callback=None):
        """ Removes a alarm
            :param alarm: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=alarm, async=async, callback=callback)

    def fetch_alarms(self, filter=None, page=None, order_by=None):
        """ Fetch Alarms """

        if order_by:
            self._alarms_fetcher.order_by = order_by

        return self._alarms_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_enterprisepermission(self, enterprisepermission, async=False, callback=None):
        """ Create a enterprisepermission
            :param enterprisepermission: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=enterprisepermission, async=async, callback=callback)

    def delete_enterprisepermission(self, enterprisepermission, async=False, callback=None):
        """ Removes a enterprisepermission
            :param enterprisepermission: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=enterprisepermission, async=async, callback=callback)

    def fetch_enterprisepermissions(self, filter=None, page=None, order_by=None):
        """ Fetch EnterprisePermissions """

        if order_by:
            self._enterprisepermissions_fetcher.order_by = order_by

        return self._enterprisepermissions_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_vlan(self, vlan, async=False, callback=None):
        """ Create a vlan
            :param vlan: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vlan, async=async, callback=callback)

    def delete_vlan(self, vlan, async=False, callback=None):
        """ Removes a vlan
            :param vlan: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vlan, async=async, callback=callback)

    def fetch_vlans(self, filter=None, page=None, order_by=None):
        """ Fetch Vlans """

        if order_by:
            self._vlans_fetcher.order_by = order_by

        return self._vlans_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_permission(self, permission, async=False, callback=None):
        """ Create a permission
            :param permission: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=permission, async=async, callback=callback)

    def delete_permission(self, permission, async=False, callback=None):
        """ Removes a permission
            :param permission: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=permission, async=async, callback=callback)

    def fetch_permissions(self, filter=None, page=None, order_by=None):
        """ Fetch PermittedActions """

        if order_by:
            self._permissions_fetcher.order_by = order_by

        return self._permissions_fetcher.fetch_matching_entities(filter=filter, page=page)
    