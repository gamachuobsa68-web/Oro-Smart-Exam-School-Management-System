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

        if login(

            self.ids.username.text,

            self.ids.password.text

        ):

            self.manager.current = "home"

        else:

            self.ids.message.text = "Login failed"





class HomeScreen(Screen):


    def on_pre_enter(self):

        exams = get_student_exams()

        self.ids.exam_list.text = ""


        for exam in exams:

            self.ids.exam_list.text += (

                str(exam["id"])
                +
                " - "
                +
                exam["title"]
                +
                "\n"

            )




    def open_exam(self):

        self.manager.exam_id = int(

            self.ids.exam_id.text

        )


        self.manager.current = "exam"





class ExamScreen(Screen):


    def on_pre_enter(self):

        data = start_exam(

            self.manager.exam_id

        )


        self.manager.questions = data["questions"]

        self.manager.question_index = 0

        self.show_question()




    def show_question(self):

        q = self.manager.questions[

            self.manager.question_index

        ]


        self.ids.question.text = q["question_text"]

        self.ids.a.text = q["option_a"]

        self.ids.b.text = q["option_b"]

        self.ids.c.text = q["option_c"]

        self.ids.d.text = q["option_d"]




    def answer(self,value):

        q = self.manager.questions[

            self.manager.question_index

        ]


        save_answer(

            self.manager.exam_id,

            q["id"],

            value

        )


        self.manager.question_index += 1


        if self.manager.question_index < len(

            self.manager.questions

        ):

            self.show_question()




    def submit(self):

        result = submit_exam(

            self.manager.exam_id

        )


        self.ids.result.text = str(result)
