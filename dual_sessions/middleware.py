"""
Middleware that overrides Django's base session middleware so that different backends can be used for
authed users and unauthed users
"""
from importlib import import_module

from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.sessions.backends.base import SessionBase
from django.conf import settings


class DualSessionMiddleware(SessionMiddleware):
    def __init__(self, get_response):
        super().__init__(get_response)
        # Never used, required during init
        default_engine = import_module(settings.AUTH_SESSION_ENGINE)
        self.SessionStore = default_engine.SessionStore

    def get_unauth_store(self) -> SessionBase:
        engine = import_module(settings.AUTH_SESSION_ENGINE)
        return engine.SessionStore

    def get_auth_store(self) -> SessionBase:
        engine = import_module(settings.UNUTH_SESSION_ENGINE)
        return engine.SessionStore

    def process_request(self, request):
        # Get the session key
        session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME)
        if request.user.is_authenticated:
            SessionStore = self.get_auth_store()
            request.session = SessionStore(session_key)
        else:
            SessionStore = self.get_unauth_store()
            request.session = SessionStore(session_key)