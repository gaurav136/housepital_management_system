
class patient:
    def __init__(self, name, age, sex, doctor_name, disease, bloud_group):

        self.name = name 
        self.age = age
        self.sex = sex 
        self.doctor_name = doctor_name 
        self.disease = disease 
        self.bloud_group = bloud_group




#     def biodata(self):
#         return f" Name = {self.name} \n Age = {self.age} \n Sex = {self.sex} \n doctor_name = {self.doctor_name} \n Disease = {self.disease} \n bloud_group = {self.bloud_group}" 


# list_of_patients =[]


# while len(list_of_patients) < 2:
#     list_of_patients.append(patient(input("Name of pationt : "), input("Age : "), input("Sex : "), input("Doc : "), input("Disease :"), input("Blood_group : ")))


# for i in range(0,len(list_of_patients)):
#     print(list_of_patients[i].biodata())

    #  def __repr__(self) : 
    #      return "patient('{}','{}','{}','{}','{}','{}')".format(self.name,self.age,self.sex,self.doctor_name,self.disease,self.bloud_group)

