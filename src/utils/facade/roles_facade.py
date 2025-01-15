from logic.roles_logic import RolesLogic


class RolesFacade:
    def __init__(self):
        self.logic = RolesLogic()

    def display_all_roles(self):
        """
        הצגת כל התפקידים
        """
        roles = self.logic.get_all_roles()
        if roles:
            for role in roles:
                print(f"Role ID: {role['idroles']}, Role Name: {role['roles_name']}")
        else:
            print("No roles found.")

    def add_role(self):
        """
        הוספת תפקיד חדש
        """
        role_name = input("Enter the role name: ")
        result = self.logic.add_role(role_name)
        if result:
            print("Role added successfully!")
        else:
            print("Failed to add role.")
