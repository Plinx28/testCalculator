import requests
import subprocess
import time
import os

from config import APP_NAME, TEST_HOST, TEST_PORT


def send_request(host, port, endpoint, method='GET', data=None):
    url = f"http://{host}:{port}/api/{endpoint}"
    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url, json=data)
    return response.json()


def start_application(host=TEST_HOST, port=TEST_PORT):
    subprocess.Popen([APP_NAME, 'start', host, str(port)])


def default_start_application():
    subprocess.Popen([APP_NAME, 'start'])


def stop_application():
    subprocess.run([APP_NAME, 'stop'])


def restart_application():
    subprocess.run([APP_NAME, 'restart'])


def get_log_content():
    log_path = os.path.join(os.environ['LOCALAPPDATA'], 'webcalculator', 'webcalculator.log')
    with open(log_path, 'r') as log_file:
        return log_file.read()
