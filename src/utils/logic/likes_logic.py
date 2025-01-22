from dal import DAL


class LikesLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_likes(self):
        """
        Retrieve all likes.
        """
        query = """
        SELECT l.like_id, l.vacation_id, l.user_id, 
               v.title AS vacation_title, u.first_name AS user_first_name, u.last_name AS user_last_name
        FROM likes l
        JOIN vacations v ON l.vacation_id = v.idvacations
        JOIN users u ON l.user_id = u.id
        """
        return self.dal.get_table(query)

    def add_like(self, user_id, vacation_id):
        check_query = """
        SELECT * FROM likes
        WHERE vacation_id = %s AND user_id = %s
        """
        existing_like = self.dal.get_one(check_query, (vacation_id, user_id))
        
        if existing_like:
            return {"success": False, "message": "Like already exists."}

        insert_query = """
        INSERT INTO likes (vacation_id, user_id)
        VALUES (%s, %s)
        """
        
        try:
            self.dal.insert(insert_query, (vacation_id, user_id))
            print(f"Like added for vacation_id={vacation_id} and user_id={user_id}")
            return {"success": True, "message": "Like added successfully."}
        except Exception as e:
            print(f"Error while adding like: {e}")
            return {"success": False, "message": "Error while adding like."}


    def remove_like(self, user_id, vacation_id):
        try:
            query = "DELETE FROM likes WHERE user_id = %s AND vacation_id = %s"
            self.dal.delete(query, (user_id, vacation_id))  # Use DAL to execute the query
            return True
        except Exception as e:
            print(f"Error while deleting like: {e}")
            return False
