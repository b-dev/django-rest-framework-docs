from django.conf import settings

API_DOCS_PROTECTED = getattr(settings, 'API_DOCS_PROTECTED', True)
API_DOCS_PROTECTED_GROUP = getattr(settings, 'API_DOCS_PROTECTED_GROUP', 'API')
