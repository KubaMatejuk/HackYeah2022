from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock
from db_actions import get_password_for_user

from object_handler import get_markers
from kivymd.app import MDApp
from kivy_garden.mapview import MapMarkerPopup


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
    placed = False
    exists = False
    marker = False

    def place_pin(self):
        self.placed = True
        pass

    def remove_pin(self):
        if self.exists:
            self.map.remove_widget(self.marker)
            self.placed = False
            self.exists = False
        pass

    def on_touch_up(self, touch):
        if touch.y > self.height * 0.05:
            if self.placed == True and self.exists == False:
                self.marker = MapMarkerPopup(lat=self.map.get_latlon_at(touch.x, touch.y)[0],
                                             lon=self.map.get_latlon_at(touch.x, touch.y)[1])
                self.marker.add_widget(TextInput(text="TEST"))
                self.map.add_widget(self.marker)
                self.exists = True
                print(self.map.get_latlon_at(touch.x, touch.y))

    def load_markers(self):
        markers_list = get_markers()
        for marker in markers_list:
            self.add_marker_to_map(marker)

    def add_marker_to_map(self, marker):
        marker_widget = MapMarkerPopup(lat=marker.latitude, lon=marker.longitude)
        # marker_widget.add_widget(Label(text=marker.marker_name + '\n'
        #                                + str(marker.description) + '\n'
        #                                + 'Added by: ' + marker.user_name, color= [0, 0, 0]))
        marker_widget.add_widget(Popup(title=marker.marker_name,
                                       content=Label(text=marker.marker_name + '\n'
                                                          + str(marker.description) + '\n'
                                                          + 'Added by: ' + marker.user_name),
                                       size_hint=(None, None), size=(200, 200)))

        self.map.add_widget(marker_widget)

    def on_enter(self, *args):
        self.load_markers()

class WasteOverBarReader(Screen):
    bar = ObjectProperty(None)

    def back(self):
        self.manager.current = 'mainMenu'

class WasteOverSecondLife(Screen):
    second_life = ObjectProperty(None)
    def back(self):
        self.manager.current = 'mainMenu'


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
