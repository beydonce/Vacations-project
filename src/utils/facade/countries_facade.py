from logic.countries_logic import CountryLogic

class CountryFacade:
    def __init__(self):
        self.logic = CountryLogic()

    def display_all_countries(self):
        countries = self.logic.get_all_countries()
        if countries:
            for country in countries:
                print(country)
        else:
            print("No countries found.")

    def add_country(self):
        country_name = input("Enter the country name: ")
        self.logic.add_country(country_name)
        print("Country added successfully!")
