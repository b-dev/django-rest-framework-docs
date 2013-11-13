import urlparse

from functools import wraps
from django.conf import settings as django_settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
import settings

def has_ruolo(u):
    if not u.is_authenticated():
        return False
    if u.is_superuser:
        return True
    for g in u.groups.all():
        if g.name in settings.API_DOCS_PROTECTED_GROUP:
            return True
    return False

def api_doc_protected(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: has_ruolo(u),
        login_url=django_settings.LOGIN_URL,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator