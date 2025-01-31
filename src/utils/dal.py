import mysql.connector


class DAL:
    """
    מחלקת DAL (Data Access Layer) - שכבת גישה לנתונים
    מספקת ממשק מאובטח ומאורגן לביצוע פעולות מול בסיס הנתונים
    """

    def __init__(self, debug=False):
        self.debug = debug
        """
        יצירת התחברות לבסיס הנתונים
        במקרה של שגיאה, מדפיסה הודעת שגיאה ומאפסת את החיבור
        """
        try:
            self.connection = mysql.connector.connect(
                host="localhost",  # שרת מקומי על המחשב שלך
                # אפשרויות נוספות: IP או דומיין של שרת מרוחק
                # למשל: "123.45.67.89" או "db.example.com"

                user="root",  #  MySQL הוא המשתמש בעל ההרשאות הגבוהות ביותר במערכת :

                password="roei2303",  # סיסמת ההתחברות
                # בסביבת ייצור מומלץ לשמור בקובץ הגדרות נפרד או משתנה סביבה

                database="vacations",  # שם מסד הנתונים
                # יש ליצור את מסד הנתונים מראש עם:
                # CREATE DATABASE project2;

                autocommit=True  # כל פעולה תתבצע מיד על בסיס הנתונים
            )

        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")
            self.connection = None

    def _validate_query_params(self, query, params):
        """
        בדיקת תקינות הפרמטרים של השאילתה
        מוודא שהשאילתה היא מחרוזת והפרמטרים הם tuple או None
        """
        if not isinstance(query, str):
            raise ValueError("Query must be a string.")
        if params is not None and not isinstance(params, tuple):
            raise ValueError("Params must be a tuple or None.")

    def _execute_query(self, query, params=None, fetchall=False, fetchone=False, debug=False):
        """
        הרצת שאילתה עם אפשרויות שונות לקבלת התוצאות
        fetchall - מחזיר את כל התוצאות
        fetchone - מחזיר שורה אחת בלבד
        debug - אם True, מדפיס מידע עבור השאילתה
        """
        self._validate_query_params(query, params)
        if self.connection:
            try:
                with self.connection.cursor(dictionary=True) as cursor:
                    if debug:
                        print(f"Executing query: {query}")
                        if params:
                            print(f"With parameters: {params}")
                    cursor.execute(query, params)
                    if fetchall:
                        result = cursor.fetchall()
                        if debug:
                            print(f"Fetched {len(result)} rows")
                        return result
                    elif fetchone:
                        result = cursor.fetchone()
                        if debug:
                            print("Fetched one row")
                        return result
                    else:
                        if debug:
                            print(f"Query affected {cursor.rowcount} rows")
                        return cursor
            except mysql.connector.Error as err:
                if debug:
                    print(f"Error executing query: {err}")
        return None

    def get_table(self, query, params=None):
        """שליפת כל השורות מטבלה"""
        return self._execute_query(query, params, fetchall=True)

    def get_scalar(self, query, params=None):
        """שליפת ערך בודד (שורה אחת)"""
        return self._execute_query(query, params, fetchone=True)

    def insert(self, query, params):
        """הוספת נתונים לטבלה"""
        return self._execute_query(query, params)

    def update(self, query, params):
        """עדכון נתונים בטבלה"""
        return self._execute_query(query, params)

    def delete(self, query, params=None):
        """מחיקת נתונים מטבלה"""
        return self._execute_query(query, params)

    def get_one(self, query, params=None):
        """שליפת רשומה בודדת"""
        return self._execute_query(query, params, fetchone=True)

    def close(self):
        """סגירת החיבור לבסיס הנתונים"""
        if self.connection:
            self.connection.close()

    def __enter__(self):
        """
        מתודה זו מופעלת בתחילת בלוק ה-with
        נקראת כאשר נכנסים לבלוק with DAL() as dal
        מחזירה את האובייקט שיוקצה למשתנה אחרי ה-as
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        מתודה זו מופעלת בסיום בלוק ה-with
        נקראת אוטומטית כשיוצאים מהבלוק, גם במקרה של שגיאה

        הפרמטרים:
        exc_type: סוג השגיאה (אם הייתה)
        exc_val: ערך השגיאה
        exc_tb: מידע על מיקום השגיאה
        """

        if self.connection:
            self.close()  # סגירת החיבור לבסיס הנתונים
            print("Connection Closed!")


# דוגמת שימוש
if __name__ == '__main__':
    with DAL() as dal:
        # dal.insert(
        #     "INSERT INTO users (first_name, last_name, email, password, date_of_birth, role_id) VALUES (%s, %s, %s, %s, %s, %s)",
        #     ('Roei', 'Koriat', 'koriat2069@gmail.com', '123456', '2005-07-25', 1)
        # )
        # print("User inserted successfully!")

        dal.insert(
            "INSERT INTO vacations (title, description, start_date, end_date, price, countries_id, image_url) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (
                'Summer in Paris',  # title
                'A wonderful vacation in Paris with a lot of sightseeing.',  # description
                '2025-06-01',  # start_date
                '2025-06-15',  # end_date
                2500.00,  # price
                1,  # countries_id (Assuming the country id 1 exists in your countries table)
                'https://example.com/images/paris.jpg'  # image_url
            )
        )


        # # דוגמאות ל-get_scalar
        # print("\n=== get_scalar examples ===")
        # count = dal.get_scalar("SELECT COUNT(*) as count FROM users")
        # max_age = dal.get_scalar("SELECT MAX(age) as max_age FROM users")

        # # דוגמאות ל-get_one
        # print("\n=== get_one examples ===")
        # user = dal.get_one("SELECT * FROM users WHERE id = %s", (1,))
        # country = dal.get_one(
        #     "SELECT * FROM countries WHERE name = %s", ('Israel',))

        # # דוגמאות ל-insert
        # print("\n=== insert examples ===")
        # dal.insert(
        #     "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)",
        #     ('Johnny1', 'johnny1@example.com', 35)
        # )
        # dal.insert(
        #     "INSERT INTO countries (name, code) VALUES (%s, %s)",
        #     ('Brazil', 'BR')
        # )

        # # דוגמאות ל-update
        # print("\n=== update examples ===")
        # dal.update(
        #     "UPDATE users SET age = %s WHERE id = %s",
        #     (31, 1)
        # )
        # dal.update(
        #     "UPDATE countries SET population = %s WHERE code = %s",
        #     (67000000, 'FR')
        # )

        # # דוגמאות ל-delete
        # print("\n=== delete examples ===")
        # dal.delete(
        #     "DELETE FROM users WHERE id = %s",
        #     (1,)
        # )
        # dal.delete(
        #     "DELETE FROM countries WHERE code = %s",
        #     ('FR',)
        # )