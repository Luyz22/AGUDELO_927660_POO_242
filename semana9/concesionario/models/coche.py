class Car:
    def __init__(self, brand: str, model: str, age: int, price: float):
        self.brand=brand
        self.__model=model
        self.__age=age
        self.__price=price
#Metodos        
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def get__age(self):
        return self.__age
    def get__price(self):
        return self.__price

    

    def set_brand(self,brand):
        self.__brand=brand
    def set_model(self,model):
        self.__lastname=lastname
    def set__age(self,age):
        self.__age=age
    def set__price(self,price):
        return self.__price

    def __repr__(self):
        return f"name={self.get_name()}, lastname={self.get_lastname()}, age={self.__age}"
