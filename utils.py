import requests
import subprocess

from typing import Literal

from config import APP_NAME, TEST_HOST, TEST_PORT, LOG_PATH


def send_request(
    host: str,
    port: int,
    endpoint: str,
    method: Literal['GET', 'POST'] = 'GET',
    data: dict | None = None
):
    url = f"http://{host}:{port}/api/{endpoint}"
    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url, json=data)
    return response.json()


def start_application(host: str = TEST_HOST, port: int = TEST_PORT):
    subprocess.Popen([APP_NAME, 'start', host, str(port)])


def default_start_application():
    subprocess.Popen([APP_NAME, 'start'])


def stop_application():
    subprocess.run([APP_NAME, 'stop'])


def restart_application():
    subprocess.run([APP_NAME, 'restart'])


def get_log_content() -> str:
    with open(LOG_PATH, 'r') as log_file:
        return log_file.read()


def clear_log_content():
    open(LOG_PATH, 'w').close()
