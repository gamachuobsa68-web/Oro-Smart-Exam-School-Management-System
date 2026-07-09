from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens import (
    LoginScreen,
    HomeScreen,
    ExamScreen
)



class GoExamManager(ScreenManager):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.exam_id = None
        self.exam_data = None
        self.questions = []
        self.question_index = 0




class GoExamApp(App):


    def build(self):

        manager = GoExamManager()


        manager.add_widget(
            LoginScreen(
                name="login"
            )
        )


        manager.add_widget(
            HomeScreen(
                name="home"
            )
        )


        manager.add_widget(
            ExamScreen(
                name="exam"
            )
        )


        return manager



if __name__ == "__main__":

    GoExamApp().run()
