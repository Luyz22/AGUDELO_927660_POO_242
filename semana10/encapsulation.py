class Person:
    def __init__(self,dni,name,age):
        self.__dni =dni 
        self.__name=name 
        self.age=age
    def __str__(self):
        return f"Person(name={self.__name}, age={self.age})"
person1=Person(1234,"Luis",20)
person1.name="Lucho"
#print(person1)

class ProductInventory:
    def __init__(self,product,__stock):
        self.product = product
        self.__stock=0

    def add_stock(self, quantity):
        self.stock.__stock += quantity
    def remove_stock(self,quantity):
        if quantity <=self.__stock:
            self.__stock -= quantity
    def show_stock(self):
        return f"Para el producto {self.product} hay un stock de {self.__stock}"

    def __str__(self):
        pass
inventory = ProductInventory("Coca-Cola")
inventory.add__stock(100)


inventory = ProductInventory("Coca-Cola")