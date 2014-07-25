# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUEgressACLsFetcher(NURESTFetcher):
    """ EgressACL fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUEgressACL
        return NUEgressACL