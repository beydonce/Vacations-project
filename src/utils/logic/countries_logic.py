<<<<<<< HEAD
from dal import DAL


class CountryLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_countries(self):
        query = "SELECT * FROM countries"
        return self.dal.get_table(query)

    def add_country(self, country_name):
        query = "INSERT INTO countries (country_name) VALUES (%s)"
        return self.dal.insert(query, (country_name,))
=======
from dal import DAL


class CountryLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_countries(self):
        query = "SELECT * FROM countries"
        return self.dal.get_table(query)

    def add_country(self, country_name):
        query = "INSERT INTO countries (country_name) VALUES (%s)"
        return self.dal.insert(query, (country_name,))
>>>>>>> d81b1a82505bc01d37a0de0e7de0a6779a52c964
