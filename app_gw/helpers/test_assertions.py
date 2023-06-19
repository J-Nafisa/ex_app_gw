def assert_application_creation(response_data, status_code, application_name, application_description):
    assert status_code == 200
    assert response_data["application_name"] == application_name
    assert response_data["application_description"] == application_description
    assert response_data["application_uuid"] is not None
    assert response_data["application_token"] is not None
    assert response_data["application_token"]["session_state"] is not None
    assert response_data["application_token"]["token"] is not None

def assert_application_info(info_response_data, application_name, application_description, application_uuid):
    assert info_response_data["application"]["application_name"] == application_name
    assert info_response_data["application"]["application_description"] == application_description
    assert info_response_data["application"]["application_uuid"] == application_uuid
    assert info_response_data["application"]["call_record"] is not None
    assert info_response_data["application"]["call_record"]["period"] is not None
    assert info_response_data["application"]["smpp"] is not None
    assert info_response_data["application"]["smpp"]["login"] is not None
    assert info_response_data["application"]["smpp"]["password"] is not None
    assert info_response_data["application"]["smpp"]["direction_type"] is not None

def assert_application_fields_match(response_data, info_response_data):
    assert response_data["application_name"] == info_response_data["application"]["application_name"]
    assert response_data["application_description"] == info_response_data["application"]["application_description"]
    assert response_data["application_uuid"] == info_response_data["application"]["application_uuid"]

def assert_application_creation_without_description(response_data, status_code, application_name):
    assert status_code == 200
    assert response_data["application_name"] == application_name
    assert "application_description" not in response_data
    assert response_data["application_uuid"] is not None
    assert response_data["application_token"] is not None
    assert response_data["application_token"]["session_state"] is not None
    assert response_data["application_token"]["token"] is not None

def assert_application_info_without_description(info_response_data, application_name, application_uuid):
    assert info_response_data["application"]["application_name"] == application_name
    assert "application_description" not in info_response_data["application"]
    assert info_response_data["application"]["application_uuid"] == application_uuid
    assert info_response_data["application"]["call_record"] is not None
    assert info_response_data["application"]["call_record"]["period"] is not None
    assert info_response_data["application"]["smpp"] is not None
    assert info_response_data["application"]["smpp"]["login"] is not None
    assert info_response_data["application"]["smpp"]["password"] is not None
    assert info_response_data["application"]["smpp"]["direction_type"] is not None

def assert_application_fields_match_without_description(response_data, info_response_data):
    assert response_data["application_name"] == info_response_data["application"]["application_name"]
    assert "application_description" not in response_data
    assert "application_description" not in info_response_data["application"]
    assert response_data["application_uuid"] == info_response_data["application"]["application_uuid"]

def assert_status_code(status_code, expected_code):
    assert status_code == expected_code, f"Expected status code {expected_code}, but got {status_code}"

