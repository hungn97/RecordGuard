import sqlite3

with sqlite3.connect("doctor_database.db") as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
userid INTEGER PRIMARY KEY,
userpw VARCHAR(20) NOT NULL,
patientid VARCHAR(20) NOT NULL);
''')

cursor.execute("""
INSERT INTO user(userid,userpw,patientid)
VALUES("30096073","password","1")
""")
cursor.execute("""
INSERT INTO user(userid,userpw,patientid)
VALUES("30426205","password","2")
""")
db.commit()

cursor.execute("SELECT * FROM user")
print(cursor.fetchall())
