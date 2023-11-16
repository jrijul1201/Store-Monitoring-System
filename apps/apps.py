import sys
from datetime import datetime

from django.apps import AppConfig


class StoremonitoringsystemConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps"
    current_timestamp = datetime.strptime(
        "2023-01-25 18:13:22.479220", "%Y-%m-%d %H:%M:%S.%f"
    )
    is_importing_data = False

    def ready(self):
        from .utils.import_data import import_data

        if "runserver" in sys.argv:
            import_data()

    def set_is_importing_data(value):
        global is_importing_data
        is_importing_data = value

    def get_is_importing_data():
        return is_importing_data
