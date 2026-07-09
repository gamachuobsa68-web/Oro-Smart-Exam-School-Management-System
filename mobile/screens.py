from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):
    def login(self):
        username = self.ids.username.text
        password = self.ids.password.text

        # yeroo jalqabaa test qofa
        if username and password:
            self.manager.current = "home"


class HomeScreen(Screen):
    pass
