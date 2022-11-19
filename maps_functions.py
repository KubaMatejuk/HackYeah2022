import folium
import webbrowser
from db_actions import get_markers, get_category_details

def create_map(center_point=(51.1102, 17.0350), zoom_start=12, width=800, height=600):
    map_object = folium.Map(location=center_point, zoom_start=zoom_start, width=width, height=height)
    return map_object

def save_map(map_object, file_name='map.html'):
    map_object.save(file_name)

def save_marker(map_object, latitude, longitude,
                marker_name, description,
                user_name, category_id,
                photo):
    category_details = get_category_details(category_id)
    category_name = category_details['name']
    marker_colour = category_details['colour']
    icon = category_details['icon']

    location = float(latitude), float(longitude)
    icon = folium.Icon(icon=icon, color=marker_colour)

    html_message =f"""
        <h1> {marker_name}</h1>
        <p>Category: {category_name}</p>
        <p>{description}</p>
        <img src='{photo}' width=200px>
        </p>
        <p>Added by: {user_name}</p>
        """
    folium.Marker(location, popup=html_message, icon=icon, tooltip=marker_name).add_to(map_object)
    return map_object

def load_markers():
    markers = get_markers()
    map_object = create_map()
    for marker in markers:
        save_marker(map_object, marker['latitude'], marker['longitude'],
                    marker['marker_name'], marker['description'],
                    marker['username'], marker['category_id'], marker['photo'])
    save_map(map_object)

# testing purposes
def open_map(chrome_path, url):
    webbrowser.get(chrome_path).open(url, new=2)
load_markers()
open_map('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s',
         'file:C:/Users/Rafał/Documents/GitHub/HackYeah2022/map.html')


