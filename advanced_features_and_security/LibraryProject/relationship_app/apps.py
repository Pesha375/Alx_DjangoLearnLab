from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

    def ready(self):
        """
        Override the ready method to include application-specific initialization.
        This is useful for setting up signals, tasks, or any other app-specific configurations.
        """
        import relationship_app.signals  # type: ignore # Ensure your signal handlers are connected
