# django-dual-sessions
Manage your Django sessions differently for authenticated and unauthenticated users - with minimal configuration required!

# Why?
Django will automatically delete sessions upon user logout - but if a user doesn't
logout (for example, because they're unauthenticated) then your database can rapidly fill
with once-off user sessions. This package allows you to control the behavior for unauthenticated
and authenticated user sessions, so your user-sessions table (and your database) doesn't fill with junk!

# Quickstart
1. Replace your Django session middlewar with django-dual session middleware.
2. Set a backend in your `settings.py` for both unauthenticated and authenticated users. You need to set a `UNAUTH_SESSION_ENGINE` and
and a `AUTH_SESSION_ENGINE`.

```python 
AUTH_SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
UNAUTH_SESSION_ENGINE = 'django_contrib.sessions.backend.cache`
```
Your `UNAUTH_SESSION_ENGINE` is the session engine used to process unauthenticated requests, and your `AUTH_SESSION_ENGINE`
engine is used to process authenticated requests.
3. That's it!

# Design Principles
* Minimal configuration - this library should remain a dropin replacement for `django.contrib.sessions`
* YAGNI - This library should remain as lightweight as possible - the less code we override the less the risk of breaking
  changes during Django updates

Made with ❤ by Aristotle Cloud Services Australia
