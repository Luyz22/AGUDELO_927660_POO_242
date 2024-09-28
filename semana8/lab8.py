from faker import Faker
fake = Faker()
class Person:
    def __init__(self, dni, name, lastname):
        self.dni=dni
        self.name=name
        self.lastname=lastname
    def __str__(self):
        return f"Person dni={self.dni},name={self.name},lastname={self.lastname})"
Person1 =Person(dni="123",name="Antony",lastname="Velasco")
print(Person1)
#numero de personas que vamos a crear
def generate_people(count):
    people=[]
    for _ in range(count):
        dni=fake.ssn()
        name=fake.first_name
        lastname = fake.last_name()

        person=Person(dni,name,lastname)
        people.append(person)

    return people
#mostrar el contenido de la lista de personas
def get_people(people):
    for person in people:
        print(person)
number=int(input("Ingrese el numero de personas a agregar:\n"))
people=generate_people(number)
get_people(people)

