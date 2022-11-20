import datetime

class Marker:
    def __init__(self, marker_name, latitude, longitude, description, user, category_id,
                  marker_id=None, photo=None, addtion_datetime = None, updated_datetime = None):
        self.id = marker_id
        self.marker_name = marker_name
        self.latitude = latitude
        self.longitude = longitude
        self.description = description
        self.user_id = user.id
        self.user_name = user.username
        self.category_id = category_id
        self.photo = photo
        self.addition_date = None
        self.addition_time = None
        if addtion_datetime:
            self.addition_datetime = addtion_datetime
            self.addition_date = self.addition_datetime.date()
            self.addition_time = self.addition_datetime.time()
        self.updated_date = None
        self.updated_time = None
        if updated_datetime:
            self.updated_datetime = updated_datetime
            self.updated_date = self.updated_datetime.date()
            self.updated_time = self.updated_datetime.time()
