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
        """
        Add a like for a user and vacation.
        """
        result = self.logic.add_like(user_id, vacation_id)
        if result['success']:
            print("Like added successfully!")
        else:
            print(result['message'])  # Provide feedback if the like already exists
    

    def remove_like(self, user_id, vacation_id):
        if self.logic.remove_like(user_id, vacation_id):
            print("Like removed successfully.")
        else:
            print("Failed to remove like.")


    def display_user_liked_vacations(self, user_id):
        """
        Display all vacations liked by the user.
        """
        liked_vacations = self.logic.get_liked_vacations_by_user(user_id)
        if liked_vacations:
            print("\n" + "=" * 50)
            print(f"{'ID':<5} {'Title':<20} {'Description':<20} {'Price':<10}")
            print("-" * 50)
            for vacation in liked_vacations:
                print(f"{vacation['idvacations']:<5} {vacation['title']:<20} {vacation['description']:<20} {vacation['price']:<10}")
            print("=" * 50)
        else:
            print("\nYou haven't liked any vacations yet.")
        input("\nPress Enter to return to the menu...")

    def manage_likes(self, user_id):
        while True:
            print("\n=== Manage Likes ===")
            print("1. Like a Vacation ❤️")
            print("2. Remove a Like 💔")
            print("3. View All Liked Vacations 💖")
            print("0. Back to Main Menu 🔙")
            
            choice = input("Choose an option: ")

            if choice == "1":
                vacation_id = int(input("Enter the vacation ID to like: "))
                self.add_like(user_id, vacation_id)
            elif choice == "2":
                vacation_id = int(input("Enter the vacation ID to remove like: "))
                self.remove_like(user_id, vacation_id)
            elif choice == "3":
                self.display_user_liked_vacations(user_id)
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")


