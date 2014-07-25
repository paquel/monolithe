# -*- coding: utf-8 -*-

from ..fetchers import NUVPortsFetcher

from restnuage import NURESTObject


class NUTier(NURESTObject):
    """ Represents a Tier object """

    def __init__(self):
        """ Initializing object """

        super(NUTier, self).__init__()

        # Read/Write Attributes
        
        self.address = None
        self.associated_network_object_id = None
        self.associated_network_object_type = None
        self.description = None
        self.gateway = None
        self.metadata = None
        self.name = None
        self.netmask = None
        self.associated_network_macro_id = None
        self.type = None
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"associated_network_object_id", remote_name=u"associatedNetworkObjectID", attribute_type=str)
        self.expose_attribute(local_name=u"associated_network_object_type", remote_name=u"associatedNetworkObjectType", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"gateway", remote_name=u"gateway", attribute_type=str)
        self.expose_attribute(local_name=u"metadata", remote_name=u"metadata", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=str)
        self.expose_attribute(local_name=u"associated_network_macro_id", remote_name=u"associatedNetworkMacroID", attribute_type=str)
        self.expose_attribute(local_name=u"type", remote_name=u"type", attribute_type=str)

        # Fetchers
        
        self.vports = []
        self._vports_fetcher = NUVPortsFetcher.fetcher_with_entity(entity=self, local_name=u"vports")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"tier"

    # REST methods
    
    def create_vport(self, vport, async=False, callback=None):
        """ Create a vport
            :param vport: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vport, async=async, callback=callback)

    def delete_vport(self, vport, async=False, callback=None):
        """ Removes a vport
            :param vport: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vport, async=async, callback=callback)

    def fetch_vports(self, filter=None, page=None, order_by=None):
        """ Fetch VPorts """

        if order_by:
            self._vports_fetcher.order_by = order_by

        return self._vports_fetcher.fetch_matching_entities(filter=filter, page=page)
    