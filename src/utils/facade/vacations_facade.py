# vacation_facade.py

from logic.vacation_logic import VacationLogic

class VacationFacade:
    def __init__(self):
        self.logic = VacationLogic()

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

        # Pause and wait for user input to return to the main menu
        input("\nPress Enter to return to the main menu...")


    def add_vacation(self):
        print("\n--- Add New Vacation ---")
        title = input("Enter vacation title: ")
        description = input("Enter vacation description: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        price = float(input("Enter price: "))
        country_id = int(input("Enter country ID: "))
        image_url = input("Enter image URL (optional): ")

        self.logic.add_vacation(title, description, start_date, end_date, price, country_id, image_url)

    def update_vacation(self):
        print("\n--- Update Vacation ---")
        vacation_id = int(input("Enter vacation ID to update: "))
        title = input("Enter new title: ")
        description = input("Enter new description: ")
        start_date = input("Enter new start date (YYYY-MM-DD): ")
        end_date = input("Enter new end date (YYYY-MM-DD): ")
        price = float(input("Enter new price: "))
        country_id = int(input("Enter new country ID: "))
        image_url = input("Enter new image URL (optional): ")

        self.logic.update_vacation(vacation_id, title, description, start_date, end_date, price, country_id, image_url)

    def delete_vacation(self):
        print("\n--- Delete Vacation ---")
        vacation_id = int(input("Enter vacation ID to delete: "))
        self.logic.delete_vacation(vacation_id)

    def manage_vacations():
        while True:
            print("\n=== Manage Vacations ===")
            print("1. Add New Vacation 🏖️")
            print("2. Update Vacation Details 📝")
            print("3. Delete Vacation 🗑️")
            print("0. Back to Main Menu 🔙")
            
            choice = input("Choose an option: ")

            if choice == "1":
                add_vacation()
            elif choice == "2":
                update_vacation()
            elif choice == "3":
                delete_vacation()
            elif choice == "0":
                break
            else:
                print("\nInvalid choice. Please try again!")

