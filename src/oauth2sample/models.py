
from pyramid.security import Allow
from pyramid.security import Authenticated
from pyramid.security import DENY_ALL


class SampleSite(object):
    __parent__ = None
    __name__ = None  # @ReservedAssignment

    __acl__ = (
        (Allow, Authenticated, 'view'),
        DENY_ALL,
    )

    def __init__(self, request):
        pass
