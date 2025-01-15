from logic.user_logic import UserLogic


class UserFacade:
    def __init__(self):
        self.logic = UserLogic()

    def display_all_users(self):
        users = self.logic.get_all_users()
        for user in users:
            print(user)

    def register_user(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        d_o_b = input("Enter date of birth (YYYY-MM-DD): ")
        role_id = int(input("Enter role ID (1 for admin, 2 for user): "))

        self.logic.add_user(first_name, last_name, email, password, d_o_b, role_id)
        print("User registered successfully!")

    def delete_user(self):
        user_id = int(input("Enter user ID to delete: "))
        self.logic.delete_user(user_id)
        print("User deleted successfully!")
