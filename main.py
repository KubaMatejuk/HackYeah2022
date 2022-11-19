from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock
from db_actions import get_password_for_user

from kivymd.app import MDApp


class WindowManager(ScreenManager):
    screen_login = ObjectProperty(None)
    screen_mainmenu = ObjectProperty(None)
    screen_map = ObjectProperty(None)


class WasteOverMenu(Screen):
    def open_maps(self):
        self.manager.current = 'mapScreen'


class WasteOverMap(Screen):
    map = ObjectProperty(None)


class WasteOverLogInScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.updating, 1)

    def updating(self, *args):
        anim_hide = Animation(opacity=1, duration=1)
        anim_hide += Animation(opacity=0, duration=1)
        anim_hide.start(self.ids.start_text)
        anim_show = Animation(opacity=0, duration=2)
        anim_show += Animation(opacity=1, duration=1)
        anim_show.start(self.ids.end_text)


    def login(self, **kwargs):
        password = self.ids.password.text
        email = self.ids.email.text
        # if password and email:
            # actual_password = get_password_for_user(email)
            #if password == actual_password:
        self.manager.current = 'mainMenu'
        

class WasteOverApp(MDApp):
    Window.size = (450, 700)

    def build(self):
        m = WindowManager(transition=NoTransition())
        return m

if __name__ == '__main__':
    WasteOverApp().run()    
