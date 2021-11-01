"""
ASGI config for chat_core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.routing import get_default_application
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat_core.settings")
django.setup()
application = get_default_application()
