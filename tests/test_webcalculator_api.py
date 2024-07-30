import pytest
from utils import send_request, start_application, stop_application

from config import TEST_HOST, TEST_PORT


@pytest.fixture(scope="module")
def app():
    start_application()
    yield
    stop_application()


@pytest.mark.parametrize("endpoint,data,expected", [
    ('addition', {'x': 0, 'y': 6}, 6),
    ('addition', {'x': -1, 'y': -2}, -3),
    ('addition', {'x': 1, 'y': -5, 'info': 'it is ok'}, -4),
    ('multiplication', {'x': 4, 'y': 6}, 24),
    ('multiplication', {'x': 123443, 'y': 0}, 0),
    ('division', {'x': 5, 'y': 1}, 5),
    ('division', {'x': 1, 'y': 5}, 0),
    ('remainder', {'x': 1, 'y': 5}, 1),
    ('remainder', {'x': 5, 'y': 2}, 1),
])
def test_arithmetic_operations(app, endpoint, data, expected):
    response = send_request(TEST_HOST, TEST_PORT, endpoint, method='POST', data=data)
    assert response == {'statusCode': 0, 'result': expected}


@pytest.mark.parametrize("data", [
    {'x': 5, 'y': 0},
    {'x': 0, 'y': 0},
])
def test_division_by_zero(app, data):
    response = send_request(TEST_HOST, TEST_PORT, 'division', method='POST', data=data)
    assert response == {'statusCode': 1, 'statusMessage': 'Ошибка вычисления'}


@pytest.mark.parametrize("data", [
    {'x': 5},
    {'y': 1},
    {'a': 1, 'b': 5},
    {'x': 1, 'z': 10000},
    {},
])
def test_missing_keys(app, data):
    response = send_request(TEST_HOST, TEST_PORT, 'addition', method='POST', data=data)
    assert response == {'statusCode': 2, 'statusMessage': 'Не указаны необходимые параметры'}


@pytest.mark.parametrize("data", [
    {'x': 'invalid', 'y': 5},
    {'x': 2, 'y': 'fake_valid'},
    {'x': None, 'y': None},
    {'x': 0.3, 'y': 5.4},
    {'x': [2], 'y': 5},
    {'x': '0', 'y': '5'},
    {'x': 5.0, 'y': 5},
    {'x': {'x': 200}, 'y': {'y': 100}},
])
def test_invalid_input(app, data):
    response = send_request(TEST_HOST, TEST_PORT, 'addition', method='POST', data=data)
    assert response == {'statusCode': 3, 'statusMessage': 'Значения параметров должны быть целыми'}


@pytest.mark.parametrize("data", [
    {'x': 2147483649, 'y': 1},
    {'x': -2147483649, 'y': 2147483648},
    {'x': 12321, 'y': -2147483649},
])
def test_out_of_range(app, data):
    response = send_request(TEST_HOST, TEST_PORT, 'addition', method='POST', data=data)
    assert response == {'statusCode': 4, 'statusMessage': 'Превышены максимальные значения параметров'}
