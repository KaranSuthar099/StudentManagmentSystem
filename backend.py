import mysql.connector as sql
from CTkMessagebox import CTkMessagebox


def insert_student_record(roll, name, class_number, date, gender, phone_number, guardian_name, address):
    # if gender == 0:
    #     gender = "Male"
    # else:
    #     gender = "Female"

    query = "INSERT INTO STUDENT_RECORDS (roll_number, name, class, Date_Of_Birth, Gender, Phone_Number, Guardians_Name, Address)" \
            " VALUES ({}, '{}', {}, '{}', '{}', '{}', '{}', '{}' )".format(str(roll), name,
                                                                                 str(class_number), date, gender,
                                                                                 str(phone_number), guardian_name,
                                                                                 address)
    try:
        cursor.execute(query)
        mydb.commit()
        CTkMessagebox(message="Data is Inserted successfully.",
                      icon="check", option_1="Ok")
        print("data entry success")
    except Exception as e:
        CTkMessagebox(title="Error", message=("Something went wrong!!!\n {}".format(e)), icon="cancel")



def update_student_record(roll, field, updated_value):
    query = "update student_records set {} = \"{}\" where Roll_Number={}".format(field, updated_value, roll)
    #update student_records set name =  where Roll_Number={}
    try:
        cursor.execute(query)
        mydb.commit()
        CTkMessagebox(message="Data is Updated successfully.",
                      icon="check", option_1="Ok")
        print("data update success")
    except Exception as e:
        print(e)
        CTkMessagebox(title="Error", message=("Something went wrong!!!\n {}".format(e)), icon="cancel")

def delete_student_record(roll):
    query = "delete from student_records where roll_number = {}".format(roll)
    try:
        cursor.execute(query)
        mydb.commit()
        CTkMessagebox(message="Data is Deleted successfully.",
                      icon="check", option_1="Ok")
        print("data delete success")
    except Exception as e:
        CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")


def get_all_data():
    mydb.commit()
    cursor.execute('SELECT * FROM STUDENT_RECORDS')
    data = cursor.fetchall()
    return data


mydb = sql.connect(host="localhost", user="root", passwd="root")  # Establishing SQL connection

cursor = mydb.cursor()  # Creating Cursor object

cursor.execute("CREATE DATABASE IF NOT EXISTS STUDENT_MANAGEMENT_SYSTEM")
cursor.execute("USE STUDENT_MANAGEMENT_SYSTEM")
cursor.execute('''
CREATE TABLE IF NOT EXISTS STUDENT_RECORDS (
    Roll_Number INT PRIMARY KEY,
    Name VARCHAR(50),
    Class INT,
    Date_Of_Birth DATE,
    Gender ENUM('Male', 'Female'),
    Phone_Number BIGINT,
    Guardians_Name VARCHAR(50),
    Address VARCHAR(255)
);
''')
