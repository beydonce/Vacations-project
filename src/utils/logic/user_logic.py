from src.utils.dal import DAL


class UserLogic:
    def __init__(self):
        self.dal = DAL()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()

    def get_all_users(self):
        """
        Retrieve all users from the database.
        Returns:
            list: A list of user dictionaries.
        """
        query = "SELECT * FROM vacations_mysql.users"
        result = self.dal.get_table(query)
        return result if result else []

    def add_user(self, username, password, email, first_name, last_name):
        """
        Add a new user to the database.
        Args:
            username (str): The username.
            password (str): The password (stored as plain text, per your request).
            email (str): The email address.
            first_name (str): The first name.
            last_name (str): The last name.
        Returns:
            bool: True if the user was added successfully, False otherwise.
        """
        try:
            query = """
            INSERT INTO vacations_mysql.users 
            (username, password, email, first_name, last_name) 
            VALUES (%s, %s, %s, %s, %s)
            """
            params = (username, password, email, first_name, last_name)
            self.dal.insert(query, params)
            return True
        except Exception as e:
            print(f"Error adding user: {e}")
            return False

    def edit_user(self, user_id, **kwargs):
        """
        Edit an existing user's details.
        Args:
            user_id (int): The user's ID.
            **kwargs: Key-value pairs of fields to update.
        Returns:
            bool: True if the user was updated successfully, False otherwise.
        """
        if not kwargs:
            return False

        clause = ", ".join([f"{key} = %s" for key in kwargs.keys()])
        params = tuple(kwargs.values()) + (user_id,)
        query = f"UPDATE vacations_mysql.users SET {clause} WHERE id = %s"

        try:
            self.dal.update(query, params)
            return True
        except Exception as e:
            print(f"Error updating user: {e}")
            return False

    def delete_user(self, user_id):
        """
        Delete a user from the database.
        Args:
            user_id (int): The user's ID.
        Returns:
            bool: True if the user was deleted successfully, False otherwise.
        """
        query = "DELETE FROM vacations_mysql.users WHERE id = %s"
        params = (user_id,)
        try:
            self.dal.delete(query, params)
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False

    def get_user_by_username(self, username):
        """
        Retrieve user information by username.
        Args:
            username (str): The username to search for.
        Returns:
            dict: The user details or None if not found.
        """
        query = "SELECT * FROM vacations_mysql.users WHERE username = %s"
        params = (username,)
        result = self.dal.get_record(query, params)
        return result

    def login(self, username, password):
        """
        Verify user credentials.
        Args:
            username (str): The username.
            password (str): The password.
        Returns:
            dict: User details if credentials are correct, None otherwise.
        """
        query = "SELECT * FROM vacations_mysql.users WHERE username = %s AND password = %s"
        params = (username, password)
        result = self.dal.get_record(query, params)
        return result if result else None


if __name__ == "__main__":
    try:
        with UserLogic() as user_logic:
            users = user_logic.get_all_users()
            print("All Users:")
            for user in users:
                print("----------------------")
                print(user)
    except Exception as err:
        print(f"Error: {err}")
