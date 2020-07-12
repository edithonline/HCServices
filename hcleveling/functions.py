import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

base_stats = {
    "level": 1,
    "xp": 0,
    "money": 0
}


def add_profile(param_id):
    user_id = str(param_id)
    sql = f"INSERT INTO global_leveling(user_id, level, xp) VALUES({user_id},1,12)"
    cursor.execute(sql)
    conn.commit()
    cursor.close()


def set_xp(param_id, param_xp):
    user_id = str(param_id)
    user_xp = str(param_xp)
    sql = ("UPDATE global_leveling SET xp = " + user_xp + " WHERE user_id = " + user_id)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
