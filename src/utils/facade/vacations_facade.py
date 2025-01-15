from logic.vacation_logic import VacationLogic


class VacationFacade:
    def __init__(self):
        self.logic = VacationLogic()

    def display_all_vacations(self):
        vacations = self.logic.get_all_vacations()
        for vacation in vacations:
            print(vacation)

    def add_vacation(self):
        title = input("Enter vacation title: ")
        description = input("Enter description: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        price = float(input("Enter price: "))
        country_id = int(input("Enter country ID: "))
        image_url = input("Enter image URL (optional): ")

        self.logic.add_vacation(title, description, start_date, end_date, price, country_id, image_url)
        print("Vacation added successfully!")
