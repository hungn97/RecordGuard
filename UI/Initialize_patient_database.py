import sqlite3

with sqlite3.connect("patient_database.db") as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS patients(
patientid INTEGER PRIMARY KEY,
firstname VARCHAR(20) NOT NULL,
lastname VARCHAR(20) NOT NULL);
''')

cursor.execute("""
INSERT INTO patients(patientid,firstname,lastname)
VALUES("1","Hung","Nguyen")
""")
cursor.execute("""
INSERT INTO patients(patientid,firstname,lastname)
VALUES("2","Bob","Smith")
""")
db.commit()

cursor.execute("SELECT * FROM patients")
print(cursor.fetchall())