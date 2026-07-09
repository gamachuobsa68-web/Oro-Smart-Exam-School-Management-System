import requests


# Yeroo production ta'u server kee itti jijjiirta
BASE_URL = "http://127.0.0.1:8000"


token = None



def login(username, password):

    global token

    url = BASE_URL + "/api/token/"

    data = {
        "username": username,
        "password": password
    }


    response = requests.post(
        url,
        json=data
    )


    if response.status_code == 200:

        token = response.json()["access"]

        return True


    return False





def get_headers():

    return {
        "Authorization":
        f"Bearer {token}"
    }





def get_student_exams():

    url = BASE_URL + "/api/exams/student/exams/"


    response = requests.get(
        url,
        headers=get_headers()
    )


    if response.status_code == 200:

        return response.json()


    return []
