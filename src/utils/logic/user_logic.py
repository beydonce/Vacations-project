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

    def add_user(self, first_name, last_name, email, password, d_o_b, role_id):
        query = """
        INSERT INTO users (first_name, last_name, email, password, d_o_b, roles_idroles)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (first_name, last_name, email, password, d_o_b, role_id)
        return self.dal.insert(query, params)

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE idusers = %s"
        return self.dal.delete(query, (user_id,))
