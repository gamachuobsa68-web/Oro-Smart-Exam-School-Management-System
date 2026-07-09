from kivy.uix.screenmanager import Screen

from api import (
    login,
    get_student_exams,
    start_exam,
    save_answer,
    submit_exam
)



class LoginScreen(Screen):

    def login_user(self):

        username = self.ids.username.text
        password = self.ids.password.text


        if login(username, password):

            self.manager.current = "home"

        else:

            self.ids.message.text = "Login failed"





class HomeScreen(Screen):

    def on_pre_enter(self):

        exams = get_student_exams()

        text = ""


        for exam in exams:

            text += (
                str(exam["id"])
                + " - "
                + exam["title"]
                + "\n"
            )


        self.ids.exam_list.text = text



    def open_exam(self):

        exam_id = self.ids.exam_id.text

        self.manager.exam_id = exam_id

        self.manager.current = "exam"





class ExamScreen(Screen):

    def on_pre_enter(self):

        exam_id = self.manager.exam_id

        data = start_exam(exam_id)

        self.manager.exam_data = data


        question = data["questions"][0]


        self.ids.question.text = question["question_text"]

        self.ids.a.text = question["option_a"]
        self.ids.b.text = question["option_b"]
        self.ids.c.text = question["option_c"]
        self.ids.d.text = question["option_d"]



    def send_answer(self, answer):

        save_answer(
            self.manager.exam_id,
            self.manager.exam_data["questions"][0]["id"],
            answer
        )


    def finish(self):

        result = submit_exam(
            self.manager.exam_id
        )

        self.ids.result.text = str(result)
