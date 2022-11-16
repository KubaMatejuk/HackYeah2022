import folium
import webbrowser

def create_map(center_point, zoom_start=12, width=800, height=400):
    map = folium.Map(location=center_point, zoom_start=zoom_start, width=width, height=height)
    return map

def save_map(map_object, file_name='map.html'):
    map_object.save(file_name)

def open_map(chrome_path, url):
    webbrowser.get(chrome_path).open(url, new=2)

def add_new_marker(map_object, latitude, longitude, message, image=None):
    location = float(latitude), float(longitude)
    folium.Marker(location, popup=message).add_to(map_object)
    return map_object

# example flow and data
map = create_map((51.1102, 17.0350))
map_with_marker = add_new_marker(map, '51.1174', '16.9962', 'New marker added!')
save_map(map_with_marker)
open_map('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s',
         'file:C:/Users/Rafał/Desktop//Python/map.html')
