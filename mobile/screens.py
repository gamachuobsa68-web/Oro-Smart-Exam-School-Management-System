from kivy.uix.screenmanager import Screen

from api import login, get_student_exams



class LoginScreen(Screen):

    def login_user(self):

        username = self.ids.username.text
        password = self.ids.password.text


        success = login(
            username,
            password
        )


        if success:

            self.manager.current = "home"

        else:

            self.ids.message.text = "Login failed"





class HomeScreen(Screen):


    def on_pre_enter(self):

        exams = get_student_exams()


        text = "Available Exams\n\n"


        if exams:

            for exam in exams:

                text += (
                    exam["title"]
                    + "\n"
                )

        else:

            text += "No exams found"


        self.ids.exam_list.text = text
