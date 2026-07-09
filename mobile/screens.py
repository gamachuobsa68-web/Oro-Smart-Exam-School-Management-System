from kivy.uix.screenmanager import Screen

from api import (
    login,
    get_student_exams,
    start_exam,
    save_answer,
    submit_exam
)



# =========================
# LOGIN SCREEN
# =========================

class LoginScreen(Screen):

    def login_user(self):

        username = self.ids.username.text
        password = self.ids.password.text


        success = login(
            username,
            password
        )


        if success:

            self.ids.message.text = ""

            self.manager.current = "home"

        else:

            self.ids.message.text = "Login failed"





# =========================
# HOME / STUDENT DASHBOARD
# =========================

class HomeScreen(Screen):


    def on_pre_enter(self):

        exams = get_student_exams()


        self.ids.exam_list.text = ""


        if exams:

            for exam in exams:

                self.ids.exam_list.text += (
                    str(exam["id"])
                    + " - "
                    + exam["title"]
                    + "\n"
                )

        else:

            self.ids.exam_list.text = (
                "No published exams"
            )




    def open_exam(self):

        exam_id = self.ids.exam_id.text


        if exam_id:

            self.manager.exam_id = int(
                exam_id
            )

            self.manager.current = "exam"





# =========================
# EXAM SCREEN
# =========================

class ExamScreen(Screen):


    def on_pre_enter(self):

        exam_id = self.manager.exam_id


        data = start_exam(
            exam_id
        )


        if data:

            self.manager.exam_data = data


            questions = data.get(
                "questions",
                []
            )


            if questions:

                self.manager.questions = questions

                self.manager.question_index = 0


                self.show_question()




    def show_question(self):

        index = self.manager.question_index


        question = (
            self.manager.questions[index]
        )


        self.ids.question.text = (
            question["question_text"]
        )


        self.ids.a.text = (
            question.get(
                "option_a",
                ""
            )
        )


        self.ids.b.text = (
            question.get(
                "option_b",
                ""
            )
        )


        self.ids.c.text = (
            question.get(
                "option_c",
                ""
            )
        )


        self.ids.d.text = (
            question.get(
                "option_d",
                ""
            )
        )




    def answer(self, value):

        index = self.manager.question_index


        question = (
            self.manager.questions[index]
        )


        save_answer(

            self.manager.exam_id,

            question["id"],

            value

        )



        if index + 1 < len(
            self.manager.questions
        ):

            self.manager.question_index += 1

            self.show_question()


        else:

            self.ids.question.text = (
                "Exam finished. Submit."
            )




    def submit(self):

        result = submit_exam(
            self.manager.exam_id
        )


        self.ids.result.text = str(
            result
                )
