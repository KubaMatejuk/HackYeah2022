from class_marker import Marker
from class_marker_category import MarkerCategory
from class_user import User
from db_actions import get_markers_tuple, add_user_to_db, get_categories_data, get_users_data

CATEGORIES_CACHE = []
USERS_CACHE = []

COLORS_DICT = {
    'gray': (0.4,0.4,0.4,1),
    'orange': (1,0.8,0,1),
    'beige': (0.6,0.4,0.01,1),
    'lightblue': (0,1,0.8,1),
    'purple': (1,0.1,0.9),
    'blue': (0,0,1,1)
}


def get_category(category_id: int) -> MarkerCategory:
    category_details_tuple = None
    global CATEGORIES_CACHE
    if not CATEGORIES_CACHE:
        CATEGORIES_CACHE = get_categories_data()
    for category_tuple in CATEGORIES_CACHE:
        if category_tuple[0] == category_id:
            category_details_tuple = category_tuple
            break
    if category_details_tuple:
        category = MarkerCategory(category_id=category_id, name=category_details_tuple[1],
                                  colour=category_details_tuple[3], description=category_details_tuple[2],
                                  icon=category_details_tuple[4])
    else:
        category = None
    return category


def get_user(user_id: int) -> User:
    username = None
    email = None
    global USERS_CACHE
    if not USERS_CACHE:
        USERS_CACHE = get_users_data()
    for user_tuple in USERS_CACHE:
        if user_tuple[0] == user_id:
            username = user_tuple[1]
            email = user_tuple[2]
            break
    if username:
        user = User(user_id=user_id, username=username, email=email)
    else:
        user = None
    return user


def get_markers(user_id=None, categories_id: list = None) -> list:
    markers_list = []
    for marker_tuple in get_markers_tuple(user_id, categories_id):
        marker = Marker(marker_id=marker_tuple[0], marker_name=marker_tuple[2], description=marker_tuple[3],
                        category_id=marker_tuple[4], photo=None, latitude=marker_tuple[5], longitude=marker_tuple[6],
                        user=get_user(marker_tuple[1]), addtion_datetime=marker_tuple[7], updated_datetime=marker_tuple[8])
        markers_list.append(marker)
    return markers_list


def add_user(username: str, email: str, password: str) -> User:
    user_id = add_user_to_db(username, email, password)
    user = User(user_id=user_id, username=username, password=password, email=email)
    return user

