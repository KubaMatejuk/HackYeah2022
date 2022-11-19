# install mysql-connector-python==8.0.29
import mysql.connector
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


def get_markers(user_id=None, categories_id: list = None) -> list:
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
    result_dicts_list = []
    for marker_tuple in result_tuples_list:
        marker_dict = {'user': get_user_details(marker_tuple[1]),
                       'marker_name': marker_tuple[2],
                       'description': marker_tuple[3],
                       'category_id': marker_tuple[4],
                       'photo': None,
                       'latitude': marker_tuple[5],
                       'longitude': marker_tuple[6]}
        result_dicts_list.append(marker_dict)
    return result_dicts_list


def get_user_details(user_id: int) -> tuple:
    query = "SELECT * FROM users WHERE user_id = {0}".format(user_id)
    user = run_sql_query(db_connect(), query)
    username = user[0][1]
    return (user_id, username)


def get_category_details(category_id: int) -> dict:
    query = "SELECT * FROM marker_category WHERE category_id = {0}".format(category_id)
    category_details_tuple = run_sql_query(db_connect(), query)[0]
    category_details_dict = {'name': category_details_tuple[1],
                             'description': category_details_tuple[2],
                             'colour': category_details_tuple[3],
                             'icon': category_details_tuple[4]}
    return category_details_dict


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
        #add user_id to result
    else:
        return None


def add_user_to_db(username, email, password):
    #check if username already exists
    pass


def add_marker_to_db(marker: dict):
    sql_command = "INSERT INTO `markers` " \
    "(`marker_id`, `user_id`, `marker_name`, `description`, `marker_category_id`, `latitude`, `longitude`) " \
    "VALUES " \
    "(NULL, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}');".format(
        marker['user'][0],
        marker['marker_name'],
        marker['description'],
        marker['category_id'],
        marker['latitude'],
        marker['longitude'])
    try:
        mydb = db_connect()
        run_sql_query(mydb, sql_command)
        mydb.commit()
    except Exception as e:
        print('Issue when adding marker: {0} to DB: {1}'.format(marker_dict, e))
        pass
    # add photo
    pass

def edit_marker_in_db(marker):
    pass

marker_dict = {'user': (2, 'patrykp'), 'marker_name': 'Telewizor', 'description': 'Nowy, nieuzywany',
               'category_id': 3, 'photo': None, 'latitude': 51.1265, 'longitude': 17.1689}

# for marker in get_markers():
#     print(marker)

add_marker_to_db(marker_dict)

