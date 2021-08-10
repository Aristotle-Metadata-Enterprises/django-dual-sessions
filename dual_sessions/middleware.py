"""
Middleware that overrides Django's base session middleware so that different backends can be used for
authed users and unauthed users
"""
from importlib import import_module

from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.sessions.backends.base import SessionBase
from django.conf import settings

from typing import Iterable


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
        engine = import_module(settings.UNAUTH_SESSION_ENGINE)
        return engine.SessionStore

    def create_store(self, SessionStore, session_key, *args):
        return SessionStore(session_key, *args)

    def get_auth_args(self, request) -> Iterable:
        """
        Get arguments for creating the authenticated SessionStore object
        Note: this is only required if you are using a custom Session backend
         """
        raise NotImplemented

    def get_unauth_args(self, request) -> Iterable:
        """
        Get arguments for creating the unauthenticated SessionStore object
        Note: this is only required if you are using a custom Session backend
        """
        raise NotImplemented

    def process_request(self, request):
        # Get the session key
        session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME)
        if request.user.is_authenticated:
            SessionStore = self.get_auth_store()
            request.session = self.create_store(SessionStore, session_key, *self.get_auth_args(request))
        else:
            SessionStore = self.get_unauth_store()
            request.session = self.create_store(SessionStore, session_key, *self.get_unauth_args(request))
