from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.animation import Animation
from kivy.properties import StringProperty, ObjectProperty, ListProperty, NumericProperty
from kivy.clock import Clock
from kivy.lang.builder import Builder

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
        self.manager.current = 'mainMenu'


class WasteOverApp(MDApp):
    def build(self):
        m = WindowManager(transition=NoTransition())
        return m

if __name__ == '__main__':
    WasteOverApp().run()    
