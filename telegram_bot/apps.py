from django.apps import AppConfig
from threading import Thread
from .bot import start

class TelegramBotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telegram_bot'

    def ready(self):
        # Запуск бота в отдельном потоке
        Thread(target=start, daemon=True).start()