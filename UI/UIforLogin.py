import sqlite3

def login():
    while True:
        doctorid = input("Please enter your badgeID: ")
        doctorpw = input("Please enter your password: ")
        patientid = input("Please enter patient's ID: ")
        with sqlite3.connect("doctor_database.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE userid = ? AND userpw = ? AND patientid = ?")
        cursor.execute(find_user,[(doctorid),(doctorpw),(patientid)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("Welcome")
                return True
            #return("exit")
            break

        else:
            print("Username and password not recognized")
            again = input("Do you want to try again?(y/n): ")
            if again.lower() == "n":
                print("Goodbye")
                #return("exit")
                break
login()
