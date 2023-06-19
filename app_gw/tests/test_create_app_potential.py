import random
import string
import pytest
from app_gw.config import env
from helpers.base_helper import (
    create_application_with_status,
    get_application_info,
    create_application_without_description,
    validate_response_schema
)
from helpers.test_assertions import (
    assert_application_creation_without_description,
    assert_application_info_without_description,
    assert_application_fields_match_without_description
)

from helpers.error_text import error_potential_user


def test_create_application_without_description():
    auth_token = env['POTENTIAL_TOKEN']

    application_name = ''.join(random.choices(string.ascii_letters, k=20))

    # Создание приложения
    response_data = create_application_without_description(auth_token, application_name)
    print(f"Приложение '{application_name}' успешно создано")

    # Проверка, что поле 'application_description' отсутствует в ответе
    assert 'application_description' not in response_data, "Field 'application_description' should not be in the response"
    print(f"Проверка отсутствия описания в ответе при создании приложения '{application_name}' выполнена успешно")

    # Проверка кода ответа и данных ответа
    assert_application_creation_without_description(response_data, 200, application_name)
    print(f"Проверка кода ответа приложения '{application_name}' выполнена успешно")

    # Получение application_uuid
    application_uuid = response_data['application_uuid']

    # Проверка метода GetInfo
    info_response_data = get_application_info(auth_token, application_uuid)
    assert_application_info_without_description(info_response_data, application_name, application_uuid)
    print(f"Проверка приложения '{application_name}' методом GetInfo выполнена успешно")

    # Проверка, что поле 'application_description' отсутствует в ответе GetInfo
    assert 'application_description' not in info_response_data, "Field 'application_description' should not be in the response"
    print(f"Проверка отсутствия описания в ответе приложения '{application_name}' методом GetInfo выполнена успешно")

    # Проверка совпадения полей
    assert_application_fields_match_without_description(response_data, info_response_data)
    print(f"Проверка приложения '{application_name}' на совпадение полей успешно выполнена")

    # Валидация схемы ответа
    validate_response_schema(response_data)
    print(f"Схема ответа при создании приложения '{application_name}' успешно проверена")

def test_create_application():
    auth_token = env['POTENTIAL_TOKEN']
    application_name = ''.join(random.choices(string.ascii_letters, k=10))

    # Создание приложения
    response, response_data = create_application_with_status(auth_token, application_name, "")

    assert response.status_code == 401
    assert response_data["error"] == error_potential_user
    print("Ошибка при создании второго приложения для потенциального пользователя")


