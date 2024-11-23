class Person:
    def __init__ (self, name,lastname,age,dni):
        self.name=name
        self.lastname=lastname
        self.age=age
        self.dni=dni

"""
CRUD

CREATE
READ
UPDATE
DELETE
UUID

"""



class PersonCRUD:
    def __init__(self):
        self.persons=[]

    """
    Description: Es una funcion de busqueda por dni
    

    params:
    dni: es un atributo de la clase Person (string | number)

    return:
    Un objeto de tipo persona
    |
    v
    """
    def find_by_dni(self,dni):
        for person in self.persons:
            if person.dni == dni:
                return person

        return None

    def create(self,person):
        if self.find_by_dni(person.dni):
            raise ValueError("Person already exists")
        self.persons.append(person)
        #optional
        return person

    def read(self,dni):
        person = self.find_by_dni(dni)
        if not person:
            raise ValueError("Person not found")

        return person

    def update(self,dni,name,lastname,age):
        person = self.find_by_dni
        if not person:
            raise ValueError("Person not found")

        if name is not None:
            person.name = name
        if lastname is not None:
            person.lastname = lastname
        if age is not None:
            person.age = age
        #Optional
        return person

    # def _update(self,dni,**kwargs):
    #     person = self.find_by_dni(dni)

    #     if not person:
    #         raise ValueError("Person not found")        
    #     for key, value in kwargs.items():
    #         if hasattr(person, key): 
    #             setattr(person,key,value)
    #     #Optional
    #     return person

    def delete(self,dni):
        person =self.find_by_dni(dni)
        if not person:
            raise ValueError("Person not found")
        self.persons.remove(person)
        return f"Person delete"