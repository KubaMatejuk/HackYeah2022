import folium
import webbrowser
from db_actions import add_marker_to_db, edit_marker_in_db, remove_marker_from_db
from object_handler import get_category, get_markers


def create_map(center_point=(51.1102, 17.0350), zoom_start=12, width=800, height=600):
    map_object = folium.Map(location=center_point, zoom_start=zoom_start, width=width, height=height)
    return map_object

def save_map(map_object, file_name='map.html'):
    map_object.save(file_name)

def add_market_to_map(map_object, marker_object):
    category_object = get_category(marker_object.category_id)

    icon = folium.Icon(icon=category_object.icon, color=category_object.colour)

    html_message =f"""
        <h1> {marker_object.marker_name}</h1>
        <p>Category: {category_object.name}</p>
        <p>{marker_object.description}</p>
        <img src='{marker_object.photo}' width=200px>
        </p>
        <p>Added by: {marker_object.user_name}</p>
        """

    folium.Marker((marker_object.latitude, marker_object.longitude), popup=html_message, icon=icon,
                  tooltip=marker_object.marker_name).add_to(map_object)
    return map_object

def edit_existing_marker(marker_object):
    edit_marker_in_db(marker_object)
    # generate refreshed map
    load_markers()

def load_markers(user_id=None, categories_id: list = None):
    markers = get_markers(user_id, categories_id)
    map_object = create_map()
    for marker in markers:
        add_market_to_map(map_object, marker)
    save_map(map_object)
    return map_object

def add_new_marker(map_object, marker_obj):
    try:
        add_marker_to_db(marker_obj)
        add_market_to_map(map_object, marker_obj)
    except Exception:
        raise Exception('Adding new marker failed')

def remove_marker(marker_object):
    remove_marker_from_db(marker_object.id)
    # generate refreshed map
    load_markers()

def get_coordinates(map_object):
    latitude = map_object['last_clicked']['lat']
    longitude = map_object['last_clicked']['lng']
    return latitude, longitude





# testing purposes
def open_map(chrome_path, url):
    webbrowser.get(chrome_path).open(url, new=2)
load_markers()
open_map('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s',
         'file:C:/Users/Rafał/Documents/GitHub/HackYeah2022/map.html')



