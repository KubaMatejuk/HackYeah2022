from class_marker import Marker
from class_marker_category import MarkerCategory
from class_user import User
from db_actions import get_category_tuple, get_user_tuple, get_markers_tuple


def get_category(category_id: int) -> MarkerCategory:
    category_details_tuple = get_category_tuple(category_id)
    category = MarkerCategory(category_id=category_id, name=category_details_tuple[1],
                              colour=category_details_tuple[3], description=category_details_tuple[2],
                              icon=category_details_tuple[4])
    return category


def get_user(user_id: int) -> User:
    user_tuple = get_user_tuple(user_id)
    user = User(user_id=user_id, username=user_tuple[1])
    return user


def get_markers(user_id=None, categories_id: list = None) -> list:
    markers_list = []
    for marker_tuple in get_markers_tuple(user_id, categories_id):
        marker = Marker(marker_id=marker_tuple[0], marker_name=marker_tuple[2], description=marker_tuple[3],
                        category_id=marker_tuple[4], photo=None, latitude=marker_tuple[5], longitude=marker_tuple[6],
                        user=get_user(marker_tuple[1]))
        markers_list.append(marker)
    return markers_list