
from oauth2sample.models import SampleSite
from pyramid.httpexceptions import HTTPForbidden
from pyramid.security import authenticated_userid
from pyramid.view import forbidden_view_config
from pyramid.view import view_config
from pyramid_oauth2_client.facebook import FacebookClient
from pyramid_oauth2_client.yasso import YassoClient


def get_oauth2_client(request):
    client_type = request.registry.settings['oauth2_client']
    if client_type == 'yasso':
        return YassoClient(request)
    elif client_type == 'facebook':
        return FacebookClient(request)
    else:
        raise ValueError(client_type)


@view_config(context=SampleSite, permission='view',
        renderer='templates/home.pt')
def home(request):
    client = get_oauth2_client(request)
    response = client.refresh()
    if response is not None:
        return response
    return {'userid': authenticated_userid(request)}


@forbidden_view_config()
def forbidden(request):
    if authenticated_userid(request) is not None:
        return HTTPForbidden()
    client = get_oauth2_client(request)
    return client.login(came_from=request.url)


@view_config(context=SampleSite, name='oauth2callback')
def oauth2callback(request):
    client = get_oauth2_client(request)
    return client.callback()


@view_config(context=SampleSite, name='login')
def login(request):
    client = get_oauth2_client(request)
    return client.login()
