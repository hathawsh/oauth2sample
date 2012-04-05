
from oauth2sample.models import SampleSite
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(
        root_factory=SampleSite,
        settings=settings,
        authentication_policy=SessionAuthenticationPolicy(),
        authorization_policy=ACLAuthorizationPolicy(),
    )
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan()
    return config.make_wsgi_app()
