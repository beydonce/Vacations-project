from dal import DAL


class LikesLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_likes(self):
        """
        שליפת כל הלייקים
        """
        query = """
        SELECT l.likes_id, l.vacations_idvacations, l.users_idusers, 
               v.title AS vacation_title, u.first_name AS user_first_name, u.last_name AS user_last_name
        FROM likes l
        JOIN vacations v ON l.vacations_idvacations = v.idvacations
        JOIN users u ON l.users_idusers = u.idusers
        """
        return self.dal.get_table(query)

    def add_like(self, user_id, vacation_id):
        """
        הוספת לייק
        """
        # בדיקה אם כבר קיים לייק כזה
        check_query = """
        SELECT * FROM likes
        WHERE vacations_idvacations = %s AND users_idusers = %s
        """
        existing_like = self.dal.get_one(check_query, (vacation_id, user_id))

        if existing_like:
            return {"success": False, "message": "Like already exists."}

        # הוספת לייק
        insert_query = """
        INSERT INTO likes (vacations_idvacations, users_idusers)
        VALUES (%s, %s)
        """
        self.dal.insert(insert_query, (vacation_id, user_id))

        # עדכון מונה הלייקים בחופשה
        update_vacation_query = """
        UPDATE vacations
        SET likes = likes + 1
        WHERE idvacations = %s
        """
        self.dal.update(update_vacation_query, (vacation_id,))

        return {"success": True, "message": "Like added successfully."}

    def remove_like(self, user_id, vacation_id):
        """
        מחיקת לייק
        """
        # בדיקה אם הלייק קיים
        check_query = """
        SELECT * FROM likes
        WHERE vacations_idvacations = %s AND users_idusers = %s
        """
        existing_like = self.dal.get_one(check_query, (vacation_id, user_id))

        if not existing_like:
            return {"success": False, "message": "Like does not exist."}

        # מחיקת הלייק
        delete_query = """
        DELETE FROM likes
        WHERE vacations_idvacations = %s AND users_idusers = %s
        """
        self.dal.delete(delete_query, (vacation_id, user_id))

        # עדכון מונה הלייקים בחופשה
        update_vacation_query = """
        UPDATE vacations
        SET likes = likes - 1
        WHERE idvacations = %s
        """
        self.dal.update(update_vacation_query, (vacation_id,))

        return {"success": True, "message": "Like removed successfully."}
