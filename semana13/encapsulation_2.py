class Person: 
    def __init__(self,name,age):
        self.__name =name
        self.__age=age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age=age


person1 = Person("marcela", 16)
print(person1.age)
person1.age=17
print(person1.age)
