from django.apps import AppConfig


class SpeakerConfig(AppConfig):
    name = 'speaker'

    def ready(self):
        import speaker.signals