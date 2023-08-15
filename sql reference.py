import mysql.connector as sql

mydb = sql.connect(host="localhost", user="root", passwd="root")
cur = mydb.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS MENU")
cur.execute("USE MENU")
cur.execute("CREATE TABLE IF NOT EXISTS MenuProgramme(roll INT PRIMARY KEY,"
            " name VARCHAR(10),"
            " age INT,"
            " marks INT, "
            "address VARCHAR(20))")


def add_record():
    rno = input("Enter roll: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")
    add = input("Enter address: ")

    cur.execute("INSERT INTO MenuProgramme VALUES (%s, %s, %s, %s, %s)", (rno, name, age, marks, add))
    mydb.commit()
    print("Data inserted")


def delete_record():
    rno = input("Enter roll: ")
    cur.execute("DELETE FROM MenuProgramme WHERE roll = %s", (rno,))
    mydb.commit()
    print("Record Deleted")


def display_record():
    try:
        cur.execute("SELECT * FROM MenuProgramme")
        result = cur.fetchall()
        for i in result:
            print(i)
    except:
        print("Error fetching data")


def update_record():
    try:
        roll = input("Enter the roll no whose details are to be updated: ")

        print("1: to Update Name ")
        print("2: to Update Age ")
        print("3: to Update Marks ")
        print("4: to Update Address ")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            name = input("Enter new Name: ")
            cur.execute("UPDATE MenuProgramme SET name = %s WHERE roll = %s", (name, roll))
        elif choice == 2:
            age = input("Enter new Age: ")
            cur.execute("UPDATE MenuProgramme SET age = %s WHERE roll = %s", (age, roll))
        elif choice == 3:
            marks = input("Enter new Marks: ")
            cur.execute("UPDATE MenuProgramme SET marks = %s WHERE roll = %s", (marks, roll))
        elif choice == 4:
            address = input("Enter new Address: ")
            cur.execute("UPDATE MenuProgramme SET"
                        " address = %s WHERE roll = %s", (address, roll))
        else:
            print("Invalid choice")
            return

        mydb.commit()
        print("Record updated")
    except:
        print("Error updating data")


def menu():
    c = "y"
    while c == "y":
        print("1: Add Record ")
        print("2: Delete Record ")
        print("3: Update Record ")
        print("4: Display Record ")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            add_record()
        elif choice == 2:
            delete_record()
        elif choice == 3:
            update_record()
        elif choice == 4:
            display_record()
        else:
            print("Invalid choice")

        c = input("Do you want to continue? (y/n): ")


menu()
