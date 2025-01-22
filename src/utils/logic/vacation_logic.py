# vacation_logic.py

from dal import DAL

class VacationLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_vacations(self, limit=10, offset=0):
        query = """
        SELECT v.idvacations, v.title, v.price, v.start_date, v.end_date, v.description, v.image_url, c.name AS country_name
        FROM vacations v
        JOIN countries c ON v.countries_id = c.id
        ORDER BY v.start_date ASC
        LIMIT %s OFFSET %s
        """
        return self.dal.get_table(query, (limit, offset))

    def add_vacation(self, title, description, start_date, end_date, price, countries_id, image_url=None):
        try:
            if not image_url:
                image_url = "https://example.com/default-image.jpg"
            query = """
            INSERT INTO vacations (title, description, start_date, end_date, price, countries_id, image_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            params = (title, description, start_date, end_date, price, countries_id, image_url)
            self.dal.insert(query, params)
            print("Vacation added successfully!")
        except Exception as e:
            print(f"Error adding vacation: {e}")

    def update_vacation(self, vacation_id, title=None, description=None, start_date=None, end_date=None, price=None, country_id=None, image_url=None):
        try:
            updates = []
            params = []
            if title:
                updates.append("title = %s")
                params.append(title)
            if description:
                updates.append("description = %s")
                params.append(description)
            if start_date:
                updates.append("start_date = %s")
                params.append(start_date)
            if end_date:
                updates.append("end_date = %s")
                params.append(end_date)
            if price:
                updates.append("price = %s")
                params.append(price)
            if country_id:
                updates.append("countries_idcountries = %s")
                params.append(country_id)
            if image_url:
                updates.append("image_url = %s")
                params.append(image_url)

            if not updates:
                print("No fields to update!")
                return

            query = f"UPDATE vacations SET {', '.join(updates)} WHERE idvacations = %s"
            params.append(vacation_id)
            self.dal.update(query, tuple(params))
            print("Vacation updated successfully!")
        except Exception as e:
            print(f"Error updating vacation: {e}")

    def delete_vacation(self, vacation_id):
        try:
            query = "DELETE FROM vacations WHERE idvacations = %s"
            self.dal.delete(query, (vacation_id,))
            print("Vacation deleted successfully!")
        except Exception as e:
            print(f"Error deleting vacation: {e}")

