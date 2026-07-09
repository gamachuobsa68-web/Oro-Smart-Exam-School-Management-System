import requests


BASE_URL = "http://YOUR_SERVER_IP:8000"


def login_user(username, password):
    url = BASE_URL + "/api/login/"

    data = {
        "username": username,
        "password": password
    }

    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            return response.json()

        return None

    except Exception:
        return None


def get_exams():
    url = BASE_URL + "/api/exams/"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        return []

    except Exception:
        return []
