from utils.db import connect_db


class UserModel:
    '''
    This layer handles all interaction between service layer and database
    '''

    __table_name__ = "employee"

    # get all existing users in the database when login
    @classmethod
    def find_all_users(cls):
        connection = connect_db()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    ''' SELECT * FROM successgy.employee''')
                list_match = cursor.fetchall()
        return list_match

    # add new user to the database when register
    @classmethod
    def add_new_user(cls, user_info):
        connection = connect_db()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute('''INSERT INTO successgy.employee (emp_id, password , emp_name, emp_role)
                                    VALUES (%s, %s, %s, %s);''', (user_info['emp_id'], user_info['password'], user_info['emp_name'], user_info['emp_role']))
                connection.commit()
