import sqlite3
from OOP3 import patient 

conn = sqlite3.connect('patient.db') 

c = conn.cursor()

# c.execute("""CREATE TABLE patient(
#             name text, 
#             age integer,
#             sex text,
#             doctor_name text,
#             disease text, 
#             bloud_group text
#             )""" )

def insert_pat(pat):
    with conn:
       c.execute("INSERT INTO patient VALUES(:name, :age, :sex, :doctor_name, :disease, :bloud_group)",{'name': pat.name, 'age': pat.age, 'sex': pat.sex, 'doctor_name': pat.doctor_name, 'disease': pat.disease, 'bloud_group':pat.bloud_group}) 

def get_pats_by_name(name):
    c.execute("SELECT * FROM patient WHERE name =:name", {'name': name})
    return c.fetchall()

def get_pats_by_age(age):
    c.execute("SELECT * FROM patient WHERE age =:age", {'age': age})
    return c.fetchall()   

def get_pats_by_sex(sex):
    c.execute("SELECT * FROM patient WHERE sex =:sex", {'sex': sex})
    return c.fetchall()

def get_pats_by_doctor_name(doctor_name):
    c.execute("SELECT * FROM patient WHERE doctor_name=:doctor_name", {'doctor_name': doctor_name})
    return c.fetchall()

def get_pats_by_disease(disease):
    c.execute("SELECT * FROM patient WHERE disease=:disease", {'disease': disease})
    return c.fetchall()

def get_pats_by_bloud_group(bloud_group):
    c.execute("SELECT * FROM patient WHERE bloud_group=:bloud_group", {'bloud_group':bloud_group})
    return c.fetchall()


pat_1= patient('Ram', 19, 'male', 'krishna', 'corona', 'A+')
pat_2= patient('Ravan', 19, 'male', 'Ram', 'jondis', 'A+')
pat_3= patient('Ram', 18, 'male', 'krishna', 'corona', 'A+')
pat_4= patient('Radha', 20, 'female', 'krishna', 'corona', 'B+')

insert_pat(pat_2) 
insert_pat(pat_3)

patients=get_pats_by_disease('corona')
print(patients)


patients=get_pats_by_doctor_name('Ram')
print(patients)


conn.close()
