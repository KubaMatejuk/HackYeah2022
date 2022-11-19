# install mysql-connector-python==8.0.29
import mysql.connector


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


def get_markers(user_id=None, categories_id: list = None) -> dict:
    query = "SELECT * FROM markers"
    if user_id:
        query += " WHERE user_id = {0}".format(user_id)
    if categories_id:
        if "WHERE" not in query:
            query+= " WHERE marker_category_id IN ("
        else:
            query += " AND marker_category_id IN ("
        for category_id in categories_id:
            query += str(category_id) + ","
        query = query[:-1] + ")"
    result_tuples_list = run_sql_query(db_connect(), query)
    result_dicts_list = []
    for marker_tuple in result_tuples_list:
        dict = {'username': get_username(marker_tuple[1]),
                'marker_name': marker_tuple[2],
                'description': marker_tuple[3],
                'category_id': marker_tuple[4],
                'photo': None,
                'latitude': marker_tuple[5],
                'longitude': marker_tuple[6]}
        result_dicts_list.append(dict)
    return result_dicts_list

def add_marker_to_db():
    #add photo
    pass

def get_username(user_id: int) -> str:
    pass

def get_category_details(category_id):
    pass

def get_password_for_user(user):

    pass

def add_user_to_db():
    pass

for x in get_markers():
    print(x)


# SELECT * FROM `markers` WHERE `marker_category_id` IN (1)

# for x in run_sql_query(db_connect(), "SELECT * FROM markers"):
#     print(x)

# INSERT INTO `markers` (`marker_id`, `marker_name`, `marker_category_id`, `latitude`, `longitude`)
# VALUES (NULL, 'Lodowka Spoleczna Bujwida', '2', '51.11864559716737', '17.068446189474464');
