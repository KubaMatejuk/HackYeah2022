from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty
from db_actions import get_password_for_user

from kivymd.app import MDApp


class WindowManager(ScreenManager):
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)


class WasteOverMenu(Screen):
    pass


class WasteOverLogInScreen(Screen):
    def login(self, **kwargs):
        password = self.ids.password.text
        email = self.ids.email.text
        actual_password = get_password_for_user(email)
        if password == actual_password:
            self.manager.current = 'mainMenu'


class WasteOverApp(MDApp):
    def build(self):
        m = WindowManager(transition=NoTransition())
        return m

if __name__ == '__main__':
    WasteOverApp().run()    
