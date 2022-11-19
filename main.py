from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty
from db_actions import get_password_for_user

from kivymd.app import MDApp


class WindowManager(ScreenManager):
    screen_login = ObjectProperty(None)
    screen_mainmenu = ObjectProperty(None)
    screen_map = ObjectProperty(None)
    screen_bar = ObjectProperty(None)
    screen_secondlife = ObjectProperty(None)


class WasteOverMenu(Screen):
    def open_maps(self):
        self.manager.current = 'mapScreen'

    def open_bars(self):
        self.manager.current = 'barScreen'

    def open_second_life(self):
        self.manager.current = 'secondLifeScreen'


class WasteOverMap(Screen):
    map = ObjectProperty(None)

class WasteOverBarReader(Screen):
    bat = ObjectProperty(None)

class WasteOverSecondLife(Screen):
    second_life = ObjectProperty(None)


class WasteOverLogInScreen(Screen):
    def login(self, **kwargs):
        password = self.ids.password.text
        email = self.ids.email.text
        actual_password = get_password_for_user(email)
        #if password == actual_password:
        self.manager.current = 'mainMenu'


class WasteOverApp(MDApp):
    def build(self):
        m = WindowManager(transition=NoTransition())
        return m

if __name__ == '__main__':
    WasteOverApp().run()    
