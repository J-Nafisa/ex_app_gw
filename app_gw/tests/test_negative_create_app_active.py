import pytest
import random
import string
from app_gw.config import env
from helpers.base_helper import create_application_with_status
from helpers.error_text import (
    error_create_application_name_invalid,
    error_create_application_description_invalid,
    error_invalid_token,
    error_application_already_exists,
)

# Ошибка при создании приложения с названием превышающим позволенную длину
def test_create_application_with_long_name():
    auth_token = env['ACTIVE_TOKEN']
    application_name = ''.join(random.choices(string.ascii_letters, k=41))  # Генерация случайного имени длиннее 40 символов

    # Попытка создания приложения с длинным именем
    response, response_data = create_application_with_status(auth_token, application_name, '')
    assert response.status_code == 400
    assert response_data["error"] == error_create_application_name_invalid
    print("Приложение с названием длиннее 40 символов не создалось")

# Ошибка при создании приложения с пустым названием
def test_create_application_with_empty_name():
    auth_token = env['ACTIVE_TOKEN']
    application_name = ""  # Пустое название приложения

    # Попытка создания приложения с пустым названием
    response, response_data = create_application_with_status(auth_token, application_name, "")
    assert response.status_code == 400
    assert response_data["error"] == error_create_application_name_invalid
    print("Приложения с пустым названием не создалось")

# Ошибка при создании приложения с описанием превышающим 90 символов
def test_create_application_with_long_description():
    auth_token = env['ACTIVE_TOKEN']
    application_name = ''.join(random.choices(string.ascii_letters, k=20))
    application_description = ''.join(random.choices(string.ascii_letters, k=91))  # Генерация случайного описания длиннее 90 символов

    # Попытка создания приложения с длинным описанием
    response, response_data = create_application_with_status(auth_token, application_name, application_description)
    assert response.status_code == 400
    assert response_data["error"] == error_create_application_description_invalid
    print("Приложение с описанием длиннее 90 символов не создалось")

# Ошибка при использовании неверного токена
def test_create_application_with_invalid_token():
    auth_token = "invalid_token"  # Неверный токен
    application_name = ''.join(random.choices(string.ascii_letters, k=10))
    application_description = "Test Application"

    # Попытка создания приложения с неверным токеном
    response, response_data = create_application_with_status(auth_token, application_name, application_description)
    assert response.status_code == 401
    assert response_data["error"] == error_invalid_token
    print("Приложение не создалось из-за неверного токена")

# Ошибка при создании приложения с уже существующим именем
def test_create_application_with_existing_name():
    auth_token = env['ACTIVE_TOKEN']
    application_name = ''.join(random.choices(string.ascii_letters, k=10))
    application_description = ''.join(random.choices(string.ascii_letters, k=10))

    # Создание приложения
    create_application_with_status(auth_token, application_name, application_description)

    # Попытка создания приложения с уже существующим именем
    response, response_data = create_application_with_status(auth_token, application_name, application_description)
    assert response.status_code == 500
    assert response_data["error"] == error_application_already_exists.format(name=application_name)
    print("Приложение с уже существующим именем не создалось")



