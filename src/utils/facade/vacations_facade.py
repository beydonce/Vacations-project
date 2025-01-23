import re
from datetime import datetime
from logic.vacation_logic import VacationLogic
from logic.countries_logic import CountryLogic

class VacationFacade:
    def __init__(self):
        self.logic = VacationLogic()
        self.country_logic = CountryLogic()  # Assuming this class exists to check country IDs

    def display_all_vacations(self):
        vacations = self.logic.get_all_vacations()
        if not vacations:
            print("No vacations available.")
            input("\nPress Enter to return to the main menu...")
            return

        print("\n=== Available Vacations ===\n")
        for vacation in vacations:
            print(f"🏖️ {vacation['title']}")
            print(f"ID: {vacation['idvacations']}")  # Display vacation ID
            print(f"   Country: {vacation['country_name']}")
            print(f"   Price: ${vacation['price']:.2f}")
            print(f"   Dates: {vacation['start_date']} to {vacation['end_date']}")
            print(f"   Description: {vacation['description']}")
            if vacation['image_url']:
                print(f"   Image: {vacation['image_url']}")
            print("-" * 40)

        input("\nPress Enter to return to the main menu...")

    def add_vacation(self):
        print("\n--- Add New Vacation ---")

        title = input("Enter vacation title: ")
        if not title.strip():
            print("Title cannot be empty!")
            return

        description = input("Enter vacation description: ")
        if not description.strip():
            print("Description cannot be empty!")
            return

        # Date Validation (start date cannot be before today)
        start_date = input("Enter start date (YYYY-MM-DD): ")
        if not self.is_valid_date(start_date):
            print("Invalid start date format! Please use YYYY-MM-DD.")
            return

        # Compare the start date to today's date
        today = datetime.today().date()
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
        if start_date_obj < today:
            print(f"Start date cannot be before today's date ({today})!")
            return

        end_date = input("Enter end date (YYYY-MM-DD): ")
        if not self.is_valid_date(end_date):
            print("Invalid end date format! Please use YYYY-MM-DD.")
            return

        if start_date > end_date:
            print("Start date cannot be later than end date!")
            return

        # Price Validation
        try:
            price = float(input("Enter price: "))
            if price <= 0:
                print("Price must be a positive number!")
                return
        except ValueError:
            print("Invalid price! Please enter a valid number.")
            return

        # Country ID Validation
        try:
            country_id = int(input("Enter country ID: "))
            if not self.country_logic.check_country_exists(country_id):
                print("Invalid country ID! Country does not exist.")
                return
        except ValueError:
            print("Invalid country ID! Please enter a valid number.")
            return

        image_url = input("Enter image URL (optional): ")

        self.logic.add_vacation(title, description, start_date, end_date, price, country_id, image_url)


    def update_vacation(self):
        print("\n--- Update Vacation ---")
        vacation_id = int(input("Enter vacation ID to update: "))

        # Check if the vacation ID exists
        vacation = self.logic.get_vacation_by_id(vacation_id)
        if not vacation:
            print(f"Vacation with ID {vacation_id} does not exist.")
            return

        title = input("Enter new title: ")
        if not title.strip():
            print("Title cannot be empty!")
            return

        description = input("Enter new description: ")
        if not description.strip():
            print("Description cannot be empty!")
            return

        # Date Validation
        start_date = input("Enter new start date (YYYY-MM-DD): ")
        if not self.is_valid_date(start_date):
            print("Invalid start date format! Please use YYYY-MM-DD.")
            return

        end_date = input("Enter new end date (YYYY-MM-DD): ")
        if not self.is_valid_date(end_date):
            print("Invalid end date format! Please use YYYY-MM-DD.")
            return

        if start_date > end_date:
            print("Start date cannot be later than end date!")
            return

        # Price Validation
        try:
            price = float(input("Enter new price: "))
            if price <= 0:
                print("Price must be a positive number!")
                return
        except ValueError:
            print("Invalid price! Please enter a valid number.")
            return

        # Country ID Validation
        try:
            country_id = int(input("Enter new country ID: "))
            if not self.country_logic.check_country_exists(country_id):
                print("Invalid country ID! Country does not exist.")
                return
        except ValueError:
            print("Invalid country ID! Please enter a valid number.")
            return

        image_url = input("Enter new image URL (optional): ")

        # Proceed to update vacation if all inputs are valid
        self.logic.update_vacation(vacation_id, title, description, start_date, end_date, price, country_id, image_url)



    def delete_vacation(self):
        print("\n--- Delete Vacation ---")
        vacation_id = int(input("Enter vacation ID to delete: "))
        self.logic.delete_vacation(vacation_id)

    def is_valid_date(self, date_str):
        """ Validate if the date is in YYYY-MM-DD format. """
        try:
            datetime_obj = datetime.strptime(date_str, '%Y-%m-%d')
            return datetime_obj
        except ValueError:
            return None

    def is_valid_url(self, url):
        """ Validate if the URL has a basic structure. """
        regex = re.compile(r'^(http|https)://')
        return re.match(regex, url) is not None

    def validate_vacation_input(self, title, description, start_date, end_date, price, country_id, image_url=None):
        """ Perform input validation for adding or updating vacation. """
        if not title.strip() or not description.strip():
            return False, "Title and description cannot be empty!"

        # Date Validation
        start_date_obj = self.is_valid_date(start_date)
        end_date_obj = self.is_valid_date(end_date)
        if not start_date_obj or not end_date_obj:
            return False, "Invalid date format! Please use YYYY-MM-DD."
        if start_date_obj > end_date_obj:
            return False, "Start date cannot be later than end date!"

        # Price Validation
        if price <= 0:
            return False, "Price must be a positive number!"

        # Country ID Validation
        if not self.country_logic.check_country_exists(country_id):
            return False, "Invalid country ID! Country does not exist."

        # Image URL Validation
        if image_url and not self.is_valid_url(image_url):
            return False, "Invalid image URL format!"

        return True, "Validation passed!"
