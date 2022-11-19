

class User:
    def __init__(self, user_id, username, password=None, email=None):
        self.id = user_id
        self.username = username
        self.password = password
        self.email = email
