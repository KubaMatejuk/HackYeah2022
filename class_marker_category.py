from db_actions import get_category_details


class MarkerCategory:
    def __init__(self, category_id, name=None, colour=None, description=None, icon=None):
        self.id = category_id
        if name is None or colour is None:
            category_details = get_category_details(self.id)
        if name:
            self.name = name
        else:
            self.name = category_details['name']
        if colour:
            self.colour = colour
        else:
            self.colour = category_details['colour']
        self.description = description
        self.icon = icon
