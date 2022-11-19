from db_actions import get_user_tuple


class User:
    def __init__(self, user_id, username=None, password=None, email=None):
        self.id = user_id
        if not username:
            self.username = get_user_tuple(user_id)[1]
        else:
            self.username = username
        self.password = password
        self.email = email
