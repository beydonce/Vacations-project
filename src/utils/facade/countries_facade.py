from logic.countries_logic import CountryLogic

class CountryFacade:
    def __init__(self):
        self.logic = CountryLogic()

    def display_all_countries(self):
        countries = self.logic.get_all_countries()
        if countries:
            print("\n=== List of Countries ===")
            print(f"{'ID':<5} {'Name':<25} {'Code':<10} {'Population':<15}")
            print("-" * 60)
            for country in countries:
                print(
                    f"{country['id']:<5} {country['name']:<25} {country['code']:<10} {country['population'] or 'N/A':<15}"
                )
            print("-" * 60)
        else:
            print("No countries found.")
        
        input("\nPress Enter to return to the main menu...")

    def add_country(self):
        print("\n=== Add a New Country ===")
        while True:
            country_name = input("Enter the country name: ").strip()
            if not country_name.isalpha():
                print("Invalid input. Country name should only contain letters.")
                continue

            country_code = input("Enter the 2-letter country code: ").strip().upper()
            if len(country_code) != 2 or not country_code.isalpha():
                print("Invalid input. Country code should be exactly 2 letters.")
                continue

            try:
                population = int(input("Enter the population (or leave blank for none): ") or "0")
                if population < 0:
                    print("Population cannot be negative.")
                    continue
            except ValueError:
                print("Invalid input. Population must be a number.")
                continue

            result = self.logic.add_country(country_name, country_code, population)
            print(result["message"])

            if result["success"]:
                break
