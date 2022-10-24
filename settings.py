# Файл с настройками и константами проекта
import os

DEBUG = False

if DEBUG:
    from dotenv import load_dotenv

    load_dotenv()

# Переменные окружения для работы бота
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Выносим формат в глобальную переменную
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
