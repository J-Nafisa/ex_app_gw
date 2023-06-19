import requests

def create_application(auth_token, application_name, application_description):
    url = "https://api.exolve.ru/application/v1/Create"

    headers = {
        "Content-Type": "application/json",
        "Authorization": auth_token
    }

    data = {
        "application_name": application_name,
        "application_description": application_description
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()

    return response_data


def create_application_with_status(auth_token, application_name, application_description):
    url = "https://api.exolve.ru/application/v1/Create"

    headers = {
        "Content-Type": "application/json",
        "Authorization": auth_token
    }

    data = {
        "application_name": application_name,
        "application_description": application_description
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()

    return response, response_data



def create_application_without_description(auth_token, application_name):
    url = "https://api.exolve.ru/application/v1/Create"

    headers = {
        "Content-Type": "application/json",
        "Authorization": auth_token
    }

    data = {
        "application_name": application_name
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()

    return response_data

def get_application_info(auth_token, application_uuid):
    url = "https://api.exolve.ru/application/v1/GetInfo"

    headers = {
        "Content-Type": "application/json",
        "Authorization": auth_token
    }

    data = {
        "application_uuid": application_uuid
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()

    return response_data

from jsonschema import validate, ValidationError

def validate_response_schema(response_data):
    schema = {
        "type": "object",
        "properties": {
            "application_uuid": { "type": "string" },
            "application_name": { "type": "string" },
            "application_token": {
                "type": "object",
                "properties": {
                    "session_state": { "type": "string" },
                    "token": { "type": "string" },
                    "start": { "type": "string", "format": "date-time" },
                },
                "required": ["session_state", "token", "start"]
            },
        },
        "required": ["application_uuid", "application_name", "application_token"]
    }

    try:
        validate(instance=response_data, schema=schema)
    except ValidationError as e:
        assert False, f"Response data does not match the schema. Error: {str(e)}"



