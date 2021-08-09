"""
Middleware that overrides Django's base session middleware so that different backends can be used for
authed users and unauthed users
"""
__version__ = "1.0.0"

class DualSession:
    pass