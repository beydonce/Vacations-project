from src.utils.dal import DAL


class VacationLogic:
    def __init__(self):
        self.dal = DAL()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()

    def get_all_vacations(self):
        """
        Fetch all vacations from the database.
        Returns:
            list: List of vacation dictionaries. Returns an empty list if no vacations are found.
        """
        query = "SELECT * FROM vacations_mysql.vacations"
        try:
            result = self.dal.get_table(query)
            return result if result else []
        except Exception as e:
            print(f"Error fetching vacations: {e}")
            return []

    def get_vacation_by_id(self, vacation_id):
        """
        Fetch vacation details by ID.
        Args:
            vacation_id (int): ID of the vacation to retrieve.
        Returns:
            dict: A dictionary of vacation details or None if not found.
        """
        query = "SELECT * FROM vacations_mysql.vacations WHERE id = %s"
        params = (vacation_id,)
        try:
            result = self.dal.get_table(query, params)
            return result[0] if result else None
        except Exception as e:
            print(f"Error fetching vacation by ID {vacation_id}: {e}")
            return None

    def add_vacation(self, title, description, start_date, end_date, 
                     countries_name, price, image):
        """
        Add a new vacation to the database.
        Args:
            title (str): Title of the vacation.
            description (str): Description of the vacation.
            start_date (date): Start date of the vacation.
            end_date (date): End date of the vacation.
            countries_name (str): Name of the country associated with the vacation.
            price (float): Price of the vacation.
            image (str): URL of the vacation image.
        Returns:
            bool: True if the vacation was added successfully, False otherwise.
        """
        query = """
        INSERT INTO vacations_mysql.vacations 
        (title, description, start_date, end_date, countries_id, price, 
        total_likes, image)
        VALUES 
        (%s, %s, %s, %s, 
        (SELECT id FROM vacations_mysql.countries WHERE country_name LIKE %s), 
        %s, 0, %s)
        """
        params = (
            title, description, start_date, end_date, 
            f"%{countries_name}%", price, image
        )
        try:
            self.dal.insert(query, params)
            return True
        except Exception as e:
            print(f"Error adding vacation: {e}")
            return False

    def edit_vacation(self, vacation_id, **kwargs):
        """
        Edit details of an existing vacation.
        Args:
            vacation_id (int): ID of the vacation to edit.
            **kwargs: Key-value pairs of fields to update (e.g., title="New Title").
        Returns:
            bool: True if the vacation was updated successfully, False otherwise.
        """
        if not kwargs:
            print("No fields provided to update.")
            return False

        clause = ", ".join([f"{k} = %s" for k in kwargs.keys()])
        params = tuple(kwargs.values()) + (vacation_id,)
        query = f"UPDATE vacations_mysql.vacations SET {clause} WHERE id = %s"
        try:
            self.dal.update(query, params)
            return True
        except Exception as e:
            print(f"Error updating vacation with ID {vacation_id}: {e}")
            return False

    def delete_vacation(self, vacation_id):
        """
        Delete a vacation from the database.
        Args:
            vacation_id (int): ID of the vacation to delete.
        Returns:
            bool: True if the vacation was deleted successfully, False otherwise.
        """
        query = "DELETE FROM vacations_mysql.vacations WHERE id = %s"
        params = (vacation_id,)
        try:
            self.dal.delete(query, params)
            return True
        except Exception as e:
            print(f"Error deleting vacation with ID {vacation_id}: {e}")
            return False

    def increment_likes(self, vacation_id):
        """
        Increment the like count of a vacation.
        Args:
            vacation_id (int): ID of the vacation to increment likes.
        Returns:
            bool: True if the likes were incremented successfully, False otherwise.
        """
        query = """
        UPDATE vacations_mysql.vacations
        SET total_likes = total_likes + 1
        WHERE id = %s
        """
        params = (vacation_id,)
        try:
            self.dal.update(query, params)
            return True
        except Exception as e:
            print(f"Error incrementing likes for vacation ID {vacation_id}: {e}")
            return False

    def filter_vacations_by_date(self, start_date=None, end_date=None):
        """
        Filter vacations based on date range.
        Args:
            start_date (date): Optional start date for filtering.
            end_date (date): Optional end date for filtering.
        Returns:
            list: List of filtered vacation dictionaries.
        """
        query = "SELECT * FROM vacations_mysql.vacations WHERE 1=1"
        params = []

        if start_date:
            query += " AND start_date >= %s"
            params.append(start_date)
        if end_date:
            query += " AND end_date <= %s"
            params.append(end_date)

        try:
            result = self.dal.get_table(query, tuple(params))
            return result if result else []
        except Exception as e:
            print(f"Error filtering vacations by date: {e}")
            return []


if __name__ == "__main__":
    try:
        with VacationLogic() as vacation_logic:
            vacations = vacation_logic.get_all_vacations()
            print("\nAvailable Vacations:")
            for vacation in vacations:
                print("----------------------")
                print(vacation)
    except Exception as e:
        print(f"Error: {e}")
