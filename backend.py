import mysql.connector as sql
import CTkMessagebox

def insert_student_record(roll, name, class_number, date, gender, phone_number, guardian_name, address, subjects):
    if gender == 0:
        gender = "Male"
    else:
        gender = "Female"
    global subjects_str

    subjects_str = ""
    for i in subjects:
        i = i.get()
        subjects_str += str(i) + ","

    query = "INSERT INTO STUDENT_RECORDS (roll_number, name, class, Date_Of_Birth, Gender, Phone_Number, Guardians_Name, Address, Subjects)" \
            " VALUES ({}, '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}' )".format(str(roll), name,
                                                                                 str(class_number), date, gender,
                                                                                 str(phone_number), guardian_name,
                                                                                 address, subjects_str)
    try:
        cursor.execute(query)
        mydb.commit()
        print("data entry success")
    except Exception as e:
        print("ERROR!!! ", e)


def update_student_record(roll, field, updated_value):
    query = "update student_records set {} = {} where Roll_Number={}".format(field, updated_value, roll)
    try:
        cursor.execute(query)
        mydb.commit()
        print("data update success")
    except Exception as e:
        print("ERROR!!! ", e)


def delete_student_record(roll):
    query = "delete from student_records where roll_number = {}".format(roll)
    try:
        cursor.execute(query)
        mydb.commit()
        print("data delete success")
    except Exception as e:
        print("ERROR!!! ", e)
        CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")


def fill_treeview(tree):
    # Clear existing data
    for item in tree.get_children():
        tree.delete(item)

    cursor.execute('SELECT * FROM STUDENT_RECORDS')
    data = cursor.fetchall()
    for i, row in enumerate(data):
        tree.insert('', i, values=row)

def get_all_data():
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
    Address VARCHAR(255), 
    Subjects VARCHAR(255)
);
''')

cursor.execute("""CREATE TABLE IF NOT EXISTS Subjects (roll_number int , subject_one varchar(20) ,
                        subject_two varchar(20), subject_three varchar(20), 
                        subject_four varchar(20), subject_five varchar(20)) """)
