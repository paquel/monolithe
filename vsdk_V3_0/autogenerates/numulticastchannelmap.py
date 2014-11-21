# -*- coding: utf-8 -*-
"""

NUMultiCastChannelMap
This file has been autogenerated by Swagger  and should not be modified.

Author Christophe Serafin <christophe.serafin@alcatel-lucent.com>

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3.0 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

"""

from bambou import NURESTObject

from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUMultiCastRangesFetcher


class NUMultiCastChannelMap(NURESTObject):
    """ Represents a MultiCastChannelMap object in Nuage VSD solution
        IMPORTANT: Do not override this object.
    """

    def __init__(self, **kwargs):
        """ Initialize a NUMultiCastChannelMap instance """

        super(NUMultiCastChannelMap, self).__init__()

        # Read/Write Attributes
        self.description = None  #  A description field provided by the user that identifies the MultiCast Channel Map - int
        self.name = None  #  Name of the current entity - int
        
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=int)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=int)
        
        # Fetchers
        self.event_logs = []
        self.event_logs_fetcher = NUEventLogsFetcher.fetcher_with_object(nurest_object=self, local_name=u"event_logs")
        self.multi_cast_ranges = []
        self.multi_cast_ranges_fetcher = NUMultiCastRangesFetcher.fetcher_with_object(nurest_object=self, local_name=u"multi_cast_ranges")
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)



    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"multicastchannelmap"

