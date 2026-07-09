import requests


# Yeroo server irratti fe'amu kana jijjiirra
BASE_URL = "http://127.0.0.1:8000"


access_token = None



# =========================
# LOGIN JWT TOKEN
# =========================

def login(username, password):

    global access_token


    url = BASE_URL + "/api/token/"


    data = {
        "username": username,
        "password": password
    }


    try:

        response = requests.post(
            url,
            json=data
        )


        if response.status_code == 200:

            access_token = (
                response.json()
                .get("access")
            )

            return True


        return False


    except Exception:

        return False





# =========================
# AUTH HEADER
# =========================

def headers():

    return {

        "Authorization":
        "Bearer " + access_token

    }





# =========================
# GET STUDENT EXAMS
# =========================

def get_student_exams():


    url = (
        BASE_URL
        +
        "/api/exams/student/exams/"
    )


    try:

        response = requests.get(

            url,

            headers=headers()

        )


        if response.status_code == 200:

            return response.json()


        return []


    except Exception:

        return []





# =========================
# START EXAM
# =========================

def start_exam(exam_id):


    url = (
        BASE_URL
        +
        "/api/exams/start/"
    )


    data = {

        "exam_id": exam_id

    }


    try:

        response = requests.post(

            url,

            json=data,

            headers=headers()

        )


        if response.status_code == 200:

            return response.json()


        return None


    except Exception:

        return None





# =========================
# SAVE ANSWER
# =========================

def save_answer(
        exam_id,
        question_id,
        answer
):


    url = (
        BASE_URL
        +
        "/api/exams/answers/save/"
    )


    data = {

        "exam_id": exam_id,

        "question_id": question_id,

        "answer": answer

    }


    try:

        response = requests.post(

            url,

            json=data,

            headers=headers()

        )


        return response.json()


    except Exception:

        return None





# =========================
# SUBMIT EXAM
# =========================

def submit_exam(exam_id):


    url = (
        BASE_URL
        +
        "/api/exams/submit/"
    )


    data = {

        "exam_id": exam_id

    }


    try:

        response = requests.post(

            url,

            json=data,

            headers=headers()

        )


        if response.status_code == 200:

            return response.json()


        return {
            "error":
            "Submit failed"
        }


    except Exception:

        return {
            "error":
            "Connection failed"
    }
