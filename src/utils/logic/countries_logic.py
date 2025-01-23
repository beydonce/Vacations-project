from dal import DAL


class CountryLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_countries(self):
        query = "SELECT * FROM countries"
        return self.dal.get_table(query)

    def add_country(self, country_name, country_code, population):
        # Check if the country already exists by its code
        check_query = "SELECT * FROM countries WHERE code = %s"
        if self.dal.get_one(check_query, (country_code,)):
            return {"success": False, "message": "Country code already exists."}
        
        # Insert the country into the database
        query = """
            INSERT INTO countries (name, code, population)
            VALUES (%s, %s, %s)
        """
        try:
            self.dal.insert(query, (country_name, country_code, population))
            return {"success": True, "message": "Country added successfully!"}
        except Exception as e:
            return {"success": False, "message": str(e)}