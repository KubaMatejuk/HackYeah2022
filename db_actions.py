# install mysql-connector-python==8.0.29
import mysql.connector
from class_marker import Marker
from class_user import User
from class_marker_category import MarkerCategory
from PIL import Image


def db_connect():
    mydb = mysql.connector.connect(
        host="sql7.freesqldatabase.com",
        user="sql7578595",
        password="8PNLIGzmDu",
        database="sql7578595")
    return mydb


def run_sql_query(connection, query: str) -> list:
    mycursor = connection.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult


def run_sql_insert(connection, query: str) -> list:
    mycursor = connection.cursor()
    mycursor.execute(query)
    connection.commit()
    return mycursor.lastrowid


def get_markers(user_id=None, categories_id: list = None) -> list:
    """
    Function to get filtered/all markers from DB
    :param user_id: int used to filter per user
    :param categories_id: list of int numbers used to filter per categories
    :return: list of Marker objects
    """
    query = "SELECT * FROM markers"
    if user_id:
        query += " WHERE user_id = {0}".format(user_id)
    if categories_id:
        if "WHERE" not in query:
            query += " WHERE marker_category_id IN ("
        else:
            query += " AND marker_category_id IN ("
        for category_id in categories_id:
            query += str(category_id) + ","
        query = query[:-1] + ")"
    result_tuples_list = run_sql_query(db_connect(), query)
    markers_list = []
    for marker_tuple in result_tuples_list:
        marker = Marker(marker_id=marker_tuple[0], marker_name=marker_tuple[2], description=marker_tuple[3],
                        category_id=marker_tuple[4], photo=None, latitude=marker_tuple[5], longitude=marker_tuple[6],
                        user=get_user(marker_tuple[1]))
        markers_list.append(marker)
    return markers_list


def get_user_tuple(user_id: int) -> tuple:
    query = "SELECT * FROM users WHERE user_id = {0}".format(user_id)
    return run_sql_query(db_connect(), query)[0]


def get_user(user_id: int) -> User:
    user_tuple = get_user_tuple(user_id)
    user = User(user_id=user_id, username=user_tuple[1])
    return user


def get_category_tuple(category_id: int) -> dict:
    query = "SELECT * FROM marker_category WHERE category_id = {0}".format(category_id)
    return run_sql_query(db_connect(), query)[0]


def get_category(category_id: int) -> MarkerCategory:
    category_details_tuple = get_category_tuple(category_id)
    category = MarkerCategory(category_id=category_id, name=category_details_tuple[1],
                              colour=category_details_tuple[3], description=category_details_tuple[2],
                              icon=category_details_tuple[4])
    return category


def get_password_for_user(user: str):
    """
    Function that will return password basing on user string
    :param user: string that will contain username or email
    :return: password: string with password for given user
    """
    query = r"SELECT password FROM users WHERE username = '{0}' OR email = '{0}'".format(user)
    password = run_sql_query(db_connect(), query)
    if password:
        return password[0][0]
        # add user_id to result
    else:
        return None


def add_user_to_db(username, email, password):
    # check if username already exists
    pass


def add_marker_to_db(marker):
    new_marker_id = None
    sql_command = "INSERT INTO `markers` " \
                  "(`marker_id`, `user_id`, `marker_name`, `description`, `marker_category_id`, `latitude`, `longitude`) " \
                  "VALUES " \
                  "(NULL, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}');".format(
        marker.user_id,
        marker.marker_name,
        marker.description,
        marker.category_id,
        marker.latitude,
        marker.longitude)
    try:
        mydb = db_connect()
        new_marker_id = run_sql_insert(mydb, sql_command)
    except Exception as e:
        print('Issue when adding marker: {0} to DB: {1}'.format(marker.marker_name, e))
        pass
    # add photo
    return new_marker_id


def edit_marker_in_db(marker: Marker):
    pass


def remove_marker_from_db(marker: Marker):
    pass


test_user = User(user_id=3, username='kubam')
test_marker = Marker(marker_name='Laptop DELL', description='2 letni laptop',
                     category_id=3, photo=None, latitude=51.1266, longitude=17.1689,
                     user=test_user)

# for marker in get_markers():
#     print(marker)

# print(add_marker_to_db(test_marker))
