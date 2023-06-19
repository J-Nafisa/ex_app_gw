import os
from dotenv import dotenv_values

# Получение пути к текущей папке
current_dir = os.path.dirname(os.path.abspath(__file__))

# Получение пути к файлу .env.prod
env_path = os.path.join(current_dir, '.env.prod')

# Загрузка переменных окружения
env = dotenv_values(env_path)

