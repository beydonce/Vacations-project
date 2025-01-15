from dal import DAL


class VacationLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_vacations(self):
        query = """
        SELECT v.*, c.country_name 
        FROM vacations v
        JOIN countries c ON v.countries_idcountries = c.idcountries
        ORDER BY v.start_date ASC
        """
        return self.dal.get_table(query)

    def add_vacation(self, title, description, start_date, end_date, price, country_id, image_url=None):
        query = """
        INSERT INTO vacations (title, description, start_date, end_date, price, countries_idcountries, image_url)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = (title, description, start_date, end_date, price, country_id, image_url)
        return self.dal.insert(query, params)
