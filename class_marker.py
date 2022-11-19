
class Marker:
    def __init__(self, marker_name, latitude, longitude, description, user: tuple, category_id,
                  marker_id=None, photo=None):
        self.marker_id = marker_id
        self.marker_name = marker_name
        self.latitude = latitude
        self.longitude = longitude
        self.description = description
        self.user_id = user[0]
        self.user_name = user[1]
        self.category_id = category_id
        self.photo = photo



