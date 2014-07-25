# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NUAddressRange(NURESTObject):
    """ Represents a AddressRange object """

    def __init__(self):
        """ Initializing object """

        super(NUAddressRange, self).__init__()

        # Read/Write Attributes
        
        self.max_address = None
        self.min_address = None
        
        self.expose_attribute(local_name=u"max_address", remote_name=u"maxAddress", attribute_type=str)
        self.expose_attribute(local_name=u"min_address", remote_name=u"minAddress", attribute_type=str)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"addressrange"

    # REST methods
    