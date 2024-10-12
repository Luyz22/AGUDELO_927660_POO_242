#Clase Abstracta
class Person:
    def __init__(self,dni,name,lastname,age):
        self.dni =dni 
        self.name=name
        self.lastname=lastname 
        self.age=age
class Student(Person):
    def __init__(self,dni,name,lastname,age,code):
        super().__init__(dni,name,lastname,age)
        self.code=code
        self.__subjects= []

    def __str__(self):
        return f"Nombre: {self.name}, codigo: {self.code}, asignaturas: {self.__subjects}"
    
    def addsubjects(self,subjects):
        self.__subjects.append(subjects)


class Professor(Person):
    def __init__(self,dni,name,lastname,age,devices,desktop):
        super().__init__(dni,name,lastname,age)
        self.devices=devices
        self.desktop=desktop
    def __str__(self):
        return f"Nombre: {self.name}, dispositivos: {self.devices}, puesto de trabajo: {self.desktop}"

student1 = Student (1234,"Luis","Chaparro",24,927660)
professor1 = Professor(1234,"David","Chavez",34,"Laptop",7)
student1.addsubjects("Matematicas")
print(student1)
print(professor1)





