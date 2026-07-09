from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens import LoginScreen, HomeScreen


class OroExamManager(ScreenManager):
    pass


class OroSmartExam(App):

    def build(self):
        sm = OroExamManager()

        sm.add_widget(
            LoginScreen(name="login")
        )

        sm.add_widget(
            HomeScreen(name="home")
        )

        return sm


if __name__ == "__main__":
    OroSmartExam().run()
