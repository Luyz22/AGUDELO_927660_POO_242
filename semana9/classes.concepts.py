# class Person:
#     def __init__ (self,name, lastname, age, isMarriedWith,nationality="Colombia"):
#         self.name=name
#         self.lastname=lastname
#         self.age=age
#         self.isMarriedWith=isMarriedWith
#         self.nationality=nationality
#  #   def __str__(self):
#   #      return f"{self.name}"

#     def __repr__(self):
#         return f"Person(name={self.name}, lastname={self.lastname}, age={self.age}, isMarriedWith={self.isMarriedWith} nationality={self.nationality})"

# person_1=Person(name="james",lastname="Rodriguez",age="33",isMarriedWith="Daniela Ospina")
# print(person_1.name)
# print(person_1)
# class Person:
#     def __init__ (self,name, lastname, age):
#         self.name=name
#         self.lastname=lastname
#         self.age=age
#         self.isMarriedWith=isMarriedWith
#         self.nationality=nationality
#  #   def __str__(self):
#   #      return f"{self.name}"

#     def __repr__(self):
#         return f"Person(name={self.name}, lastname={self.lastname}, age={self.age},
#         spouse={self.isMarriedWith} ,nationality={self.nationality})"

# person_1=Person(name="james",lastname="Rodriguez",age="33",isMarriedWith="Daniela Ospina")
# print(person_1.name)
# print(person_1)


class Person:
    def __init__(self,name: str, lastname: str, age: int):
        self.__name=name
        self.__lastname=lastname
        self.age=age

    def get_name(self):
        return self.__name
    def get_lastname(self):
        return self.__lastname
    def get__age(self,age):
        return self.__age

    

    def set_name(self,name):
        self.__name=name
    def set_lastname(self,lastname):
        self.__lastname=lastname
    def set__age(self,age):
        self.__age=age

        

    def __repr__(self):
        return f"name={self.get_name()}, lastname={self.get_lastname()}, age={self.__age}"
person_1 =Person(name="James", lastname="Rodriguez", age=33)
person_2 =Person(name="Daniela", lastname="Ortiz", age=32)
person_3= Person(name="Luis", lastname="Chaparro", age=28)

person_1.set__age(20)

print(person_1)

def get_discount():
    pass