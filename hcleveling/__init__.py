from services.hcleveling import functions
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


class Leveling:
    @staticmethod
    def exists(param_id):
        user_id = str(param_id)
        cursor.execute("SELECT level FROM global_leveling WHERE user_id=" + user_id)
        data = cursor.fetchone()
        if data is None:
            return False
        else:
            return True

    @staticmethod
    def add_profile(param_id):
        if Leveling.exists(param_id):
            pass
        else:
            functions.add_profile(param_id)
            print("Profile Added")

    @staticmethod
    def set_xp(param_id, param_xp):
        if Leveling.exists(param_id):
            functions.set_xp(param_id, param_xp)
            pass
        else:
            functions.add_profile(param_id)
            Leveling.set_xp(param_id, param_xp)
