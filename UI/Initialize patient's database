from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title('RecordGuard')
root.geometry("500x500")


def main():
    # Databases

    # Create a database or connect to one
    conn = sqlite3.connect('patient_data.db')

    # Create cursor
    c = conn.cursor()

    # saerch_btn = Button(root, text="Search patient database")
    # Searching through the database
    # Create table

    ########### TEST TO CREATE TABLE FOR PATIENTS DATA ##############
    # c.execute("""CREATE TABLE patients (
    #         first_name text,
    #         last_name text,
    #         address text,
    #         city text,
    #         state text,
    #         zipcode integer,
    #         phone integer,
    #         password text,
    #         confirm text
    #         )""")

    def delete():
        clean()
        # Create a database or connect to one
        conn = sqlite3.connect('patient_data.db')
        # Create cursor
        c = conn.cursor()

        def erase():
            # Create a database or connect to one
            conn = sqlite3.connect('patient_data.db')
            # Create cursor
            c = conn.cursor()
            c.execute("DELETE from patients WHERE oid = " + delete.get())
            delete.delete(0,END)
            #Commit Changes
            conn.commit()
            #Close Connection 
            conn.close()
        def back():
            # Create a database or connect to one
            conn = sqlite3.connect('patient_data.db')
            # Create cursor
            c = conn.cursor()
            delete.destroy()
            delete_label.destroy()
            erase_btn.destroy()
            back_btn.destroy()
            main()
            #Commit Changes
            conn.commit()
            #Close Connection 
            conn.close()

        # f_name = Entry(root,width = 30)
        # f_name.grid(row=0, column = 1, padx = 20, pady = (10,0))
        # l_name = Entry(root,width = 30)
        # l_name.grid(row=1, column = 1)
        # f_name_label = Label(root, text = "First Name")
        # f_name_label.grid(row = 0, column = 0, pady = (10,0))
        # l_name_label = Label(root, text = "Last Name")
        # l_name_label.grid(row = 1, column = 0)
        delete = Entry(root,width = 30)
        delete.grid(row=2, column = 1, padx = 20, pady = (10,0))
        delete_label = Label(root, text = "Patient's ID")
        delete_label.grid(row = 2, column = 0, pady = (10,0))

        erase_btn = Button(root, text="Erase data", command = erase)
        erase_btn.grid(row=3,column=0,columnspan=2,pady=10,padx=10,ipadx = 200)
        back_btn = Button(root, text="Return", command = back)
        back_btn.grid(row=4,column=0,columnspan=2,pady=10,padx=10,ipadx = 200)

        #Commit Changes
        conn.commit()
        #Close Connection 
        conn.close()

    def signup():
        clean()
        # Create a database or connect to one
        conn = sqlite3.connect('patient_data.db')
        # Create cursor
        c = conn.cursor()

        #Create Submit Function for database
        def submit():
            # Create a database or connect to one
            conn = sqlite3.connect('patient_data.db')
            # Create cursor
            c = conn.cursor()

            #Insert Into the Table
            c.execute("INSERT INTO patients VALUES (:f_name, :l_name, :address, :city, :state, :zipcode, :phone, :password, :confirm)",
                    {
                        'f_name': f_name.get(),
                        'l_name': l_name.get(),
                        'address': address.get(),
                        'city': city.get(),
                        'state': state.get(),
                        'zipcode': zipcode.get(),
                        'phone': phone.get(),
                        'password':password.get(),
                        'confirm':reenterpw.get()
                    } 
            )

            #Clear the Text Boxes
            f_name.delete(0,END)
            l_name.delete(0,END)
            address.delete(0,END)
            city.delete(0,END)
            state.delete(0,END)
            zipcode.delete(0,END)
            phone.delete(0,END)
            password.delete(0,END)
            reenterpw.delete(0,END)

            #Commit Changes
            conn.commit()
            #Close Connection 
            conn.close()

        def back():
            # Create a database or connect to one
            conn = sqlite3.connect('patient_data.db')
            # Create cursor
            c = conn.cursor()

            f_name.destroy()
            l_name.destroy()
            address.destroy()
            city.destroy()
            state.destroy()
            zipcode.destroy()
            phone.destroy()
            password.destroy()
            reenterpw.destroy()
            submit_btn.destroy()
            query_btn.destroy()
            return_btn.destroy()
            f_name_label.destroy()
            l_name_label.destroy()
            address_label.destroy()
            city_label.destroy()
            state_label.destroy()
            zipcode_label.destroy()
            phone_label.destroy()
            password_label.destroy()
            reenterpw_label.destroy()
            
            main()

            #Commit Changes
            conn.commit()
            #Close Connection 
            conn.close()

        #Create Text Boxes
        f_name = Entry(root,width = 35)
        f_name.grid(row=0, column = 1, padx = 20, pady = (10,0))
        l_name = Entry(root,width = 35)
        l_name.grid(row=1, column = 1)
        address = Entry(root,width = 35)
        address.grid(row=2, column = 1)
        city = Entry(root,width = 35)
        city.grid(row=3, column = 1)
        state = Entry(root,width = 35)
        state.grid(row=4, column = 1)
        zipcode = Entry(root,width = 35)
        zipcode.grid(row=5, column = 1)
        phone = Entry(root,width = 35)
        phone.grid(row=6, column = 1)
        password = Entry(root,show="*", width=35)
        password.grid(row=7,column = 1)
        reenterpw = Entry(root,show="*", width=35)
        reenterpw.grid(row=8, column = 1)

        f_name_label = Label(root, text = "First Name")
        f_name_label.grid(row = 0, column = 0, pady = (10,0))
        l_name_label = Label(root, text = "Last Name")
        l_name_label.grid(row = 1, column = 0)
        address_label = Label(root, text = "Address")
        address_label.grid(row = 2, column = 0)
        city_label = Label(root, text = "City")
        city_label.grid(row = 3, column = 0)
        state_label = Label(root, text = "State")
        state_label.grid(row = 4, column = 0)
        zipcode_label = Label(root, text = "Zipcode")
        zipcode_label.grid(row = 5, column = 0)
        phone_label = Label(root, text = "Phone Number")
        phone_label.grid(row= 6, column = 0)
        password_label = Label(root, text = "Password")
        password_label.grid(row=7, column = 0)
        reenterpw_label = Label(root, text = "Confirm password")
        reenterpw_label.grid(row=8,column = 0)

        #Buttons
        submit_btn = Button(root, text="Add Record to Database", command = submit)
        submit_btn.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx = 160)

        return_btn = Button(root, text="Return", command = back)
        return_btn.grid(row=11, column=0,columnspan=2,pady=10,padx=10,ipadx = 210)

        #Commit Changes
        conn.commit()

        #Close Connection 
        conn.close()

    # Create edit function to update a record
    def edit():
        def change():
            def update():
                # Create a database or connect to one
                conn = sqlite3.connect('patient_data.db')
                # Create cursor
                c = conn.cursor()

                c.execute("""UPDATE patients SET
                        first_name = :first,
                        last_name = :last,
                        address = :address,
                        city = :city,
                        state = :state,
                        zipcode = :zipcode,
                        phone = :phone,
                        password = :password
                        reenterpw = :confirm
                        
                        WHERE oid = :oid""",
                        { 'first': f_name_editor.get(),
                          'last': l_name_editor.get(),
                          'address': address_editor.get(),
                          'city': city_editor.get(),
                          'state': state_editor.get(),
                          'zipcode': zipcode_editor.get(),
                          'phone': phone_editor.get(),
                          'password': password_editor.get(),
                          'reenterpw': reenterpw_editor.get()
                        })

                #Commit Changes
                conn.commit()
                #Close Connection 
                conn.close()

                #Clear the Text Boxes
                f_name_editor.delete(0,END)
                l_name_editor.delete(0,END)
                address_editor.delete(0,END)
                city_editor.delete(0,END)
                state_editor.delete(0,END)
                zipcode_editor.delete(0,END)
                phone_editor.delete(0,END)
                password_editor.delete(0,END)
                reenterpw_editor.delete(0,END)
            
            # Create a database or connect to one
            conn = sqlite3.connect('patient_data.db')
            # Create cursor
            c = conn.cursor()

            record_id = id_editor.get()
            c.execute("SELECT * FROM patients WHERE oid = " + record_id)
            records = c.fetchall()
            #Create Text Boxes
            f_name_editor = Entry(root,width = 35)
            f_name_editor.grid(row=0, column = 1, padx = 20, pady = (10,0))
            l_name_editor = Entry(root,width = 35)
            l_name_editor.grid(row=1, column = 1)
            address_editor = Entry(root,width = 35)
            address_editor.grid(row=2, column = 1)
            city_editor = Entry(root,width = 35)
            city_editor.grid(row=3, column = 1)
            state_editor = Entry(root,width = 35)
            state_editor.grid(row=4, column = 1)
            zipcode_editor = Entry(root,width = 35)
            zipcode_editor.grid(row=5, column = 1)
            phone_editor = Entry(root,width = 35)
            phone_editor.grid(row=6, column = 1)
            password_editor = Entry(root,show="*", width=35)
            password_editor.grid(row=7,column = 1)
            reenterpw_editor = Entry(root,show="*", width=35)
            reenterpw_editor.grid(row=8, column = 1)

            f_name_editor_label = Label(root, text = "First Name")
            f_name_editor_label.grid(row = 0, column = 0, pady = (10,0))
            l_name_editor_label = Label(root, text = "Last Name")
            l_name_editor_label.grid(row = 1, column = 0)
            address_editor_label = Label(root, text = "Address")
            address_editor_label.grid(row = 2, column = 0)
            city_editor_label = Label(root, text = "City")
            city_editor_label.grid(row = 3, column = 0)
            state_editor_label = Label(root, text = "State")
            state_editor_label.grid(row = 4, column = 0)
            zipcode_editor_label = Label(root, text = "Zipcode")
            zipcode_editor_label.grid(row = 5, column = 0)
            phone_editor_label = Label(root, text = "Phone Number")
            phone_editor_label.grid(row= 6, column = 0)
            password_editor_label = Label(root, text = "Password")
            password_editor_label.grid(row=7, column = 0)
            reenterpw_editor_label = Label(root, text = "Confirm password")
            reenterpw_editor_label.grid(row=8,column = 0)

            for record in records:
                f_name_editor.insert(0, record[0])
                l_name_editor.insert(0, record[1])
                address_editor.insert(0, record[2])
                city_editor.insert(0, record[3])
                state_editor.insert(0, record[4])
                zipcode_editor.insert(0, record[5])
                phone_editor.insert(0, record[6])
                password_editor.insert(0, record[7])
                reenterpw_editor.insert(0, record[8])

            save_btn = Button(root, text="Save changes", command = update)
            save_btn.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx = 180)
            #Commit Changes
            conn.commit()
            #Close Connection 
            conn.close()

        def back():
            # Create a database or connect to one
            conn = sqlite3.connect('patient_data.db')
            # Create cursor
            c = conn.cursor()

            change_btn.destroy()
            id_editor.destroy()
            id_editor_label.destroy()
            return_btn.destroy()

            main()

            #Commit Changes
            conn.commit()
            #Close Connection 
            conn.close()

        clean()
        # Create a database or connect to one
        conn = sqlite3.connect('patient_data.db')
        # Create cursor
        c = conn.cursor()

        id_editor = Entry(root,width = 35)
        id_editor.grid(row=0, column = 1, padx = 20, pady = (10,0))
        id_editor_label = Label(root, text = "First Name")
        id_editor_label.grid(row = 0, column = 0, pady = (10,0))

        change_btn = Button(root, text="Change", command = change)
        change_btn.grid(row=1,column=0,columnspan=2,pady=10,padx=10,ipadx = 180)

        return_btn = Button(root, text="Return", command = back)
        return_btn.grid(row=11, column=0,columnspan=2,pady=10,padx=10,ipadx = 210)

        #Commit Changes
        conn.commit()
        #Close Connection 
        conn.close()

    # Create query function
    def query():
        clean()
        # Create a database or connect to one
        conn = sqlite3.connect('patient_data.db')
        # Create cursor
        c = conn.cursor()

        def auth():
            def back():
                # Create a database or connect to one
                conn = sqlite3.connect('patient_data.db')
                # Create cursor
                c = conn.cursor()

                authenticate_btn.destroy()
                return_btn.destroy()
                query_label.destroy()

                main()

                #Commit Changes
                conn.commit()
                #Close Connection 
                conn.close()
            # Create a database or connect to one
            conn = sqlite3.connect('patient_data.db')
            # Create cursor
            c = conn.cursor()

            c.execute("SELECT *, oid FROM patients")
            records = c.fetchall()
            ########### TEST TO SEE DATA ##############
            print_records = ''
            for record in records:
                print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[9])+"\n"
            query_label = Label(root, text=print_records)
            query_label.grid(row=3,column=0,columnspan=2)

            return_btn = Button(root, text="Return", command = back)
            return_btn.grid(row=2, column=0,columnspan=2,pady=10,padx=10,ipadx = 210)

            #Commit Changes
            conn.commit()
            #Close Connection 
            conn.close()  

        def back():
            # Create a database or connect to one
            conn = sqlite3.connect('patient_data.db')
            # Create cursor
            c = conn.cursor()

            authenticate_btn.destroy()
            return_btn.destroy()

            main()

            #Commit Changes
            conn.commit()
            #Close Connection 
            conn.close() 

        authenticate_btn = Button(root, text="Authenticate Me", command = auth)
        authenticate_btn.grid(row=1,column=0,columnspan=2,pady=10,padx=10,ipadx = 180)
        return_btn = Button(root, text="Return", command = back)
        return_btn.grid(row=2, column=0,columnspan=2,pady=10,padx=10,ipadx = 210)
        
        #Commit Changes
        conn.commit()
        #Close Connection 
        conn.close()    

    def clean():
        signup_btn.destroy()
        delete_btn.destroy()
        query_btn.destroy()
        update_btn.destroy()
        logout_btn.destroy()
    
    def finish():
        quit()

    signup_btn = Button(root, text="Register a Patient", command = signup)
    signup_btn.grid(row=1,column=0,columnspan=2,pady=10,padx=10,ipadx = 180)
    delete_btn = Button(root, text="Delete a Patient", command = delete)
    delete_btn.grid(row=2,column=0,columnspan=2,pady=10,padx=10,ipadx = 180)
    query_btn = Button(root, text="Show Records", command = query)
    query_btn.grid(row=3, column=0,columnspan=2,pady=10,padx=10,ipadx = 180)
    update_btn = Button(root, text="Edit a Patient's Info", command = edit)
    update_btn.grid(row=4,column=0,columnspan=2,pady=10,padx=10,ipadx = 180)
    logout_btn = Button(root, text="Log Out", command = finish)
    logout_btn.grid(row=5,column=0,columnspan=2,pady=10,padx=10,ipadx = 180)

main()
root.mainloop()
