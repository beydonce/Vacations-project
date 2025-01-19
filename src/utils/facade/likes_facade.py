from logic.likes_logic import LikesLogic


class LikesFacade:
    def __init__(self):
        self.logic = LikesLogic()

    def display_all_likes(self):
        """
        הצגת כל הלייקים
        """
        likes = self.logic.get_all_likes()
        if likes:
            for like in likes:
                print(f"Like ID: {like['likes_id']}, User: {like['user_first_name']} {like['user_last_name']}, Vacation: {like['vacation_title']}")
        else:
            print("No likes found.")

    def add_like(self):
        """
        הוספת לייק
        """
        user_id = int(input("Enter User ID: "))
        vacation_id = int(input("Enter Vacation ID: "))

        result = self.logic.add_like(user_id, vacation_id)
        print(result["message"])

    def remove_like(self):
        """
        מחיקת לייק
        """
        user_id = int(input("Enter User ID: "))
        vacation_id = int(input("Enter Vacation ID: "))

        result = self.logic.remove_like(user_id, vacation_id)
        print(result["message"])