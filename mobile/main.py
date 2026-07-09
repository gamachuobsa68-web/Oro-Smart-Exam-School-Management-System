from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


class LoginScreen(Screen):
    def login(self):
        self.manager.current = "home"


class HomeScreen(Screen):
    pass


class ExamApp(App):
    def build(self):
        Builder.load_file("ui.kv")

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))
        return sm


if __name__ == "__main__":
    ExamApp().run()
