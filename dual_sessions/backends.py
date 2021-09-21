from django.contrib.sessions.backends.cached_db import SessionStore


KEY_PREFIX = "django_dual_sessions"


class DualSessionStore(SessionStore):
    """This is basically a modified cached_db - just with segmented loading and saving behaviours depending on whether
    the user is authenticated or unauthenticated"""
