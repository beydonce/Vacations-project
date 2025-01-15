from dal import DAL


class RolesLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_roles(self):
        """
        שליפת כל התפקידים
        """
        query = "SELECT * FROM roles"
        return self.dal.get_table(query)

    def get_role_by_id(self, role_id):
        """
        שליפת תפקיד לפי מזהה
        """
        query = "SELECT * FROM roles WHERE idroles = %s"
        return self.dal.get_one(query, (role_id,))

    def add_role(self, role_name):
        """
        הוספת תפקיד חדש
        """
        query = "INSERT INTO roles (roles_name) VALUES (%s)"
        return self.dal.insert(query, (role_name,))
