import requests


BASE_URL = "http://192.168.1.5:8000"


token = None



def login(username, password):

    global token


    response = requests.post(

        BASE_URL + "/api/token/",

        json={
            "username": username,
            "password": password
        }

    )


    if response.status_code == 200:

        token = response.json()["access"]

        return True


    return False




def auth_header():

    return {
        "Authorization":
        f"Bearer {token}"
    }





def get_student_exams():

    response = requests.get(

        BASE_URL +
        "/api/exams/student/exams/",

        headers=auth_header()

    )


    if response.status_code == 200:

        return response.json()


    return []





def start_exam(exam_id):

    response = requests.post(

        BASE_URL +
        "/api/exams/start/",

        json={
            "exam_id": exam_id
        },

        headers=auth_header()

    )


    if response.status_code == 200:

        return response.json()


    return None





def save_answer(
        exam_id,
        question_id,
        answer
):


    response = requests.post(

        BASE_URL +
        "/api/exams/answers/save/",

        json={

            "exam_id": exam_id,

            "question_id": question_id,

            "answer": answer

        },

        headers=auth_header()

    )


    return response.json()





def submit_exam(exam_id):


    response = requests.post(

        BASE_URL +
        "/api/exams/submit/",

        json={
            "exam_id": exam_id
        },

        headers=auth_header()

    )


    return response.json()
