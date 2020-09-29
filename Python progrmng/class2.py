 ### inheritance ####
class Employee():             
    def __init__(self,emp_id,name,salary,place):
        self.id = emp_id
        self.name = name
        self.salary = salary
        self.place = place
    def display(self):
        print('id ', self.id)
        print('name '+ self.name)
        print('salary', self.salary)
        print('place '+ self.place)
class Manager(Employee):                    #inherited class
    def __init__(self,mid,mname,msalary,mplace,mproject):       #init method of manager class
        Employee.__init__(self,emp_id=mid,name=mname,salary=msalary,place=mplace)
        self.project = mproject
    def m_display(self):            #functn for manager
        self.display()              #display of emply
        print('project:' + self.project)  

print('------Employee----')
e1 =Employee(12,'Rami',1234,'vlncy')
e1.display()
print('-----Manager----')
m1 = Manager(12,'Savad',123,'me12','erp projct')
m1.m_display()


# e1 = Employee(21,'rami',10000,'clt')
# e2 = Employee(23,'AMAL',12000,'Wynd')
# e1.display()