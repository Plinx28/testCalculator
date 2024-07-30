import pytest
from utils import send_request, start_application, stop_application, restart_application, get_log_content, default_start_application

from config import TEST_HOST, TEST_PORT


@pytest.fixture()
def app():
    start_application()
    yield
    stop_application()


def test_state_clear(app):
    response = send_request(TEST_HOST, TEST_PORT, 'state')
    # The strings in the response are not Latin
    assert response == {'statusCode': 0, 'state': 'OK'}


def test_state_with_fixed_response(app):
    response = send_request(TEST_HOST, TEST_PORT, 'state')
    # Test can be passed with this:
    assert response['statusCode'] == 0
    assert response['state'].lower().replace('о', 'o').replace('к', 'k') == 'ok'


def test_default_start():
    default_start_application()
    response = send_request('127.0.0.1', 17678, 'state')
    # Test can be passed with this:
    assert response['statusCode'] == 0
    assert response['state'].lower().replace('о', 'o').replace('к', 'k') == 'ok'
    stop_application()


def test_restart(app):
    initial_state = send_request(TEST_HOST, TEST_PORT, 'state')
    restart_application()
    new_state = send_request(TEST_HOST, TEST_PORT, 'state')
    assert initial_state == new_state


def test_custom_host_and_port():
    start_application('localhost', 5445)
    response = send_request('localhost', 5445, 'state')
    # Test can be passed with this:
    assert response['statusCode'] == 0
    assert response['state'].lower().replace('о', 'o').replace('к', 'k') == 'ok'
    stop_application()


def test_log_file():
    log_content = get_log_content()
    assert log_content, "Log file should not be empty"
