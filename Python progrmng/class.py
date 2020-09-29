# class student():  
#     name = "amal"
#     age = 22
# s1 = student()
# print(s1.age)
# print(s1.name)
class Student():
    def __init__(self,name,age,place):  #constructor method -compulsry fro object creation
        self.name = name
        self.age = age
        self.place = place
    def display(self):      #user defined functn
        print('name ' + self.name)
        print('age ', self.age)
        print('place '+self.place)
s1 = Student('aysha',22,'clt') #object creatn
s2 = Student('rami', 21,'edpal')
s1.display()                    #callng functn
s2.display()

