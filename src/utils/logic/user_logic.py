<<<<<<< HEAD
from dal import DAL

class UserLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_users(self):
        query = "SELECT * FROM users"
        return self.dal.get_table(query)

    def get_user_by_id(self, user_id):
        query = "SELECT * FROM users WHERE idusers = %s"
        return self.dal.get_one(query, (user_id,))

    def get_user_by_username(self, username):
        query = "SELECT * FROM users WHERE username = %s"
        return self.dal.get_one(query, (username,))

    def add_user(self, username, first_name, last_name, email, password, date_of_birth, role_id):
        query = """
        INSERT INTO users (username, first_name, last_name, email, password, date_of_birth, role_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = (username, first_name, last_name, email, password, date_of_birth, role_id)
        return self.dal.insert(query, params)

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE idusers = %s"
        return self.dal.delete(query, (user_id,))
=======
from dal import DAL


class UserLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_users(self):
        query = "SELECT * FROM users"
        return self.dal.get_table(query)

    def get_user_by_id(self, user_id):
        query = "SELECT * FROM users WHERE idusers = %s"
        return self.dal.get_one(query, (user_id,))

    def get_user_by_username(self, username):
        query = "SELECT * FROM users WHERE username = %s"
        return self.dal.get_one(query, (username,))

    def add_user(self, username, first_name, last_name, email, password, date_of_birth, role_id):
        query = """
        INSERT INTO users (username, first_name, last_name, email, password, date_of_birth, role_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = (username, first_name, last_name, email, password, date_of_birth, role_id)
        return self.dal.insert(query, params)

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE idusers = %s"
        return self.dal.delete(query, (user_id,))
>>>>>>> d81b1a82505bc01d37a0de0e7de0a6779a52c964
