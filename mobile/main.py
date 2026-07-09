from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens import (
    LoginScreen,
    HomeScreen,
    ExamScreen
)



class OroExamManager(ScreenManager):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.exam_id = None

        self.exam_data = None

        self.questions = []

        self.question_index = 0





class OroSmartExam(App):


    def build(self):

        sm = OroExamManager()


        sm.add_widget(
            LoginScreen(
                name="login"
            )
        )


        sm.add_widget(
            HomeScreen(
                name="home"
            )
        )


        sm.add_widget(
            ExamScreen(
                name="exam"
            )
        )


        return sm





if __name__ == "__main__":

    OroSmartExam().run()
