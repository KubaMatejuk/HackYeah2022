
class Marker:
    def __init__(self, marker_name, latitude, longitude, description, user, category_id,
                  marker_id=None, photo=None):
        self.marker_id = marker_id
        self.marker_name = marker_name
        self.latitude = latitude
        self.longitude = longitude
        self.description = description
        self.user_id = user.id
        self.user_name = user.username
        self.category_id = category_id
        self.photo = photo



