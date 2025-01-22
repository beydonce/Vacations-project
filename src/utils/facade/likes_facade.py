from logic.likes_logic import LikesLogic


class LikesFacade:
    def __init__(self):
        self.logic = LikesLogic()

    def display_all_likes(self):
        """
        Display all likes.
        """
        likes = self.logic.get_all_likes()
        if likes:
            for like in likes:
                print(f"Like ID: {like['like_id']}, User: {like['user_first_name']} {like['user_last_name']}, Vacation: {like['vacation_title']}")
        else:
            print("No likes found.")

    def add_like(self, user_id, vacation_id):
        print(f"Attempting to add like for user_id={user_id}, vacation_id={vacation_id}")
        result = self.logic.add_like(user_id, vacation_id)
        print(f"Add like result: {result}")  # This will show you the result of the add_like method

    def remove_like(self, user_id, vacation_id):
        if self.logic.remove_like(user_id, vacation_id):
            print("Like removed successfully.")
        else:
            print("Failed to remove like.")

    def manage_likes(self, user_id):
        while True:
            print("\n=== Like Vacations ===")
            print("1. Add a Like")
            print("2. Remove a Like")
            print("0. Back to Main Menu")
            choice = input("Choose an option: ")

            if choice == "1":
                vacation_id = int(input("Enter Vacation ID to like: "))
                print(f"Inserting like for user_id={user_id}, vacation_id={vacation_id}")
                self.add_like(user_id, vacation_id)
            elif choice == "2":
                vacation_id = int(input("Enter Vacation ID to unlike: "))  # Ask for vacation_id
                print(f"Removing like for user_id={user_id}, vacation_id={vacation_id}")
                self.remove_like(user_id, vacation_id)  # Pass both user_id and vacation_id
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

