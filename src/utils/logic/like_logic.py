from src.utils.dal import DAL


class LikeLogic:
    def __init__(self):
        self.dal = DAL()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()

    def get_all_likes(self):
        """
        Retrieve all likes from the database.
        Returns:
            list: A list of like dictionaries.
        """
        query = "SELECT * FROM vacations_mysql.likes"
        result = self.dal.get_table(query)
        return result if result else []

    def add_like(self, user_id, vacation_id):
        """
        Add a like for a vacation by a user.
        Args:
            user_id (int): The ID of the user who liked the vacation.
            vacation_id (int): The ID of the vacation being liked.
        Returns:
            bool: True if the like was added successfully, False otherwise.
        """
        try:
            query = """
            INSERT INTO vacations_mysql.likes (user_id, vacation_id) 
            VALUES (%s, %s)
            """
            params = (user_id, vacation_id)
            self.dal.insert(query, params)

            # Update the vacation's total_likes count
            update_query = """
            UPDATE vacations_mysql.vacations 
            SET total_likes = total_likes + 1 
            WHERE id = %s
            """
            self.dal.update(update_query, (vacation_id,))
            return True
        except Exception as e:
            print(f"Error adding like: {e}")
            return False

    def remove_like(self, user_id, vacation_id):
        """
        Remove a like for a vacation by a user.
        Args:
            user_id (int): The ID of the user who liked the vacation.
            vacation_id (int): The ID of the vacation being unliked.
        Returns:
            bool: True if the like was removed successfully, False otherwise.
        """
        try:
            query = """
            DELETE FROM vacations_mysql.likes 
            WHERE user_id = %s AND vacation_id = %s
            """
            params = (user_id, vacation_id)
            self.dal.delete(query, params)

            # Update the vacation's total_likes count
            update_query = """
            UPDATE vacations_mysql.vacations 
            SET total_likes = total_likes - 1 
            WHERE id = %s
            """
            self.dal.update(update_query, (vacation_id,))
            return True
        except Exception as e:
            print(f"Error removing like: {e}")
            return False

    def get_likes_by_user(self, user_id):
        """
        Retrieve all vacations liked by a specific user.
        Args:
            user_id (int): The user's ID.
        Returns:
            list: A list of vacation IDs liked by the user.
        """
        query = "SELECT vacation_id FROM vacations_mysql.likes WHERE user_id = %s"
        params = (user_id,)
        result = self.dal.get_table(query, params)
        return [like['vacation_id'] for like in result] if result else []

    def get_likes_for_vacation(self, vacation_id):
        """
        Retrieve all users who liked a specific vacation.
        Args:
            vacation_id (int): The vacation's ID.
        Returns:
            list: A list of user IDs who liked the vacation.
        """
        query = "SELECT user_id FROM vacations_mysql.likes WHERE vacation_id = %s"
        params = (vacation_id,)
        result = self.dal.get_table(query, params)
        return [like['user_id'] for like in result] if result else []

    def is_liked(self, user_id, vacation_id):
        """
        Check if a user has liked a specific vacation.
        Args:
            user_id (int): The user's ID.
            vacation_id (int): The vacation's ID.
        Returns:
            bool: True if the user has liked the vacation, False otherwise.
        """
        query = """
        SELECT 1 FROM vacations_mysql.likes 
        WHERE user_id = %s AND vacation_id = %s
        LIMIT 1
        """
        params = (user_id, vacation_id)
        result = self.dal.get_record(query, params)
        return bool(result)


if __name__ == "__main__":
    try:
        with LikeLogic() as like_logic:
            likes = like_logic.get_all_likes()
            print("All Likes:")
            for like in likes:
                print("----------------------")
                print(like)
    except Exception as err:
        print(f"Error: {err}")
