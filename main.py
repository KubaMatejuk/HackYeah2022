from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.core.image import Image
from db_actions import get_password_for_user, add_marker_to_db
from class_marker import Marker
from class_user import User

from object_handler import get_markers, get_category, COLORS_DICT
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

    def logout(self):
        self.manager.current = 'logInScreen'


class WasteOverMap(Screen):
    map = ObjectProperty(None)
    placed = False
    exists = False
    marker = False
    block_adding_new_marker = False

    def place_pin(self, txt_input):
        item_name = txt_input.text
        test_user = User(user_id=3, username='kubam')
        marker = Marker(item_name, self.lat, self.lon, 'Test Item', test_user, 6)
        add_marker_to_db(marker)
        self.block_adding_new_marker = False

    def remove_pin(self):
        if self.exists:
            self.map.remove_widget(self.marker)
            self.placed = False
            self.exists = False
        pass

    def on_touch_up(self, touch):
        if touch.y > self.height * 0.05 and not self.block_adding_new_marker:
            marker = MapMarkerPopup(lat=self.map.get_latlon_at(touch.x, touch.y)[0],
                                            lon=self.map.get_latlon_at(touch.x, touch.y)[1])
            txt_input = TextInput(text_size=(self.width, self.height), multiline=False, hint_text='Provide short description', on_text_validate=self.place_pin)
            marker.add_widget(txt_input)
            self.map.add_widget(marker)
            self.exists = True
            self.lat = self.map.get_latlon_at(touch.x, touch.y)[0]
            self.lon = self.map.get_latlon_at(touch.x, touch.y)[1]
            self.block_adding_new_marker = True

    def load_markers(self):
        markers_list = get_markers()
        for marker in markers_list:
            self.add_marker_to_map(marker)

    def add_marker_to_map(self, marker):
        category_object = get_category(marker.category_id)

        marker_widget = MapMarkerPopup(lat=marker.latitude, lon=marker.longitude)
        pop_up = MarkerPopUp(marker.marker_name,marker.description, marker.user_name, category_name=category_object.name, category_color=category_object.colour)
        marker_widget.add_widget(pop_up)

        self.map.add_widget(marker_widget)

    def on_enter(self, *args):
        self.load_markers()

    def back(self):
        self.manager.current = 'mainMenu'

class MarkerPopUp(BoxLayout):
    message = ObjectProperty()
    titleLabel = ObjectProperty()
    category_text = ObjectProperty()
    def __init__(self, title, text, username, category_name='other', category_color='gray', **kwargs):
        super(MarkerPopUp, self).__init__(**kwargs)

        self.titleLabel.text = title
        if text:
            self.message.text = text + '\n\n' + 'Added by: ' + username
        else:
            self.message.text = 'Added by: ' + username
        self.category_text.text = 'Category: ' + category_name
        self.category_text.color = COLORS_DICT[category_color]


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
    def build(self):
        m = WindowManager(transition=NoTransition())
        return m

if __name__ == '__main__':
    WasteOverApp().run()    
