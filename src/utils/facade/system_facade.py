import sys
import os
import re
from datetime import datetime, date
from logic.country_logic import CountryLogic
from logic.vacation_logic import VacationLogic

class VacationFacade:
    def __init__(self):
        self.params = {
            "title": None,
            "description": None,
            "start_date": None,
            "end_date": None,
            "country": None,
            "price": None,
            "image_url": None
        }
        self.now = date.today()
        self.logic = VacationLogic()
        self.country_logic = CountryLogic()

    def add_vacation(self):
        self.get_title()
        self.get_description()
        self.get_start_date()
        self.get_end_date()
        self.get_countries_name()
        self.get_price()
        self.get_image()

        return self.logic.add_vacation(
            self.params["title"],
            self.params["description"],
            self.params["start_date"],
            self.params["end_date"],
            self.params["country"],
            self.params["price"],
            self.params["image_url"]
        )

    def get_title(self):
        while True:
            title = input("Enter title: ").strip()
            if not title.replace(" ", "").isalpha():
                print("Title must contain only letters and spaces")
            elif len(title) < 5:
                print("Title must be at least 5 characters long")
            else:
                self.params["title"] = title
                print("Title added")
                break

    def get_countries_name(self):
        while True:
            countries_name = input("Enter country name: ").strip().lower()
            if self.country_logic.check_if_country_exist(countries_name):
                print("Country added to vacation info!")
                self.params["country"] = countries_name
                break
            else:
                print("Country does not exist in the database.")
                print("Suggested countries:")
                countries = self.country_logic.get_all_countries()
                print(" | ".join(country["country_name"] for country in countries))

    def get_description(self):
        while True:
            description = input("Enter description: ").strip()
            if not description:
                print("Description is mandatory!")
            else:
                self.params["description"] = description
                break

    def get_start_date(self):
        while True:
            try:
                date_str = input("Enter start date (YYYY-MM-DD): ")
                start_date = datetime.strptime(date_str, "%Y-%m-%d").date()

                if start_date < self.now:
                    print("Start date cannot be in the past")
                    continue

                self.params["start_date"] = start_date
                print("Start date added")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD")

    def get_end_date(self):
        while True:
            try:
                date_str = input("Enter end date (YYYY-MM-DD): ")
                end_date = datetime.strptime(date_str, "%Y-%m-%d").date()

                if end_date < self.now:
                    print("End date cannot be in the past")
                    continue

                if end_date <= self.params["start_date"]:
                    print("End date must be after start date")
                    continue

                self.params["end_date"] = end_date
                print("End date added")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD")

    def get_price(self):
        while True:
            try:
                price = float(input("Enter price: "))
                if not 1000 <= price <= 10000:
                    print("Price must be between 1000 and 10000")
                else:
                    self.params["price"] = price
                    print("Price added")
                    break
            except ValueError:
                print("Price must be a number!")

    def get_image(self):
        while True:
            image_url = input("Enter image URL (optional, press Enter to skip): ").strip()
            if not image_url:
                self.params["image_url"] = None
                print("No image URL selected")
                break

            # Basic URL validation with regular expression
            url_pattern = r'^https?:\/\/[\w.-]+(?:\.[\w\.-]+)+(?:[\w\-\.\?\,\'\/\\\+&%\$#_=]*)?$'
            if not re.match(url_pattern, image_url):
                print("Invalid URL format!")
                continue

            self.params["image_url"] = image_url
            print("Image URL added")
            break

if __name__ == "__main__":
    vacation = VacationFacade()
    result = vacation.add_vacation()

    print("\nBooking Results:")
    print("---------------")
    for key, value in vacation.params.items():
        print(f"{key.capitalize().replace('_', ' ')}: {value}")
