#student = {
#    "name" : "luis"
#    "age" : 24
#}
#print(student["name"])

#class Persona
#__name: string
#__lastname: string
#__id: string
#__age: int
#__role: string
# 1:student
# 2:collaborator
# 3:security

def class_person(name,lastname,id,age,role)
    return {
        "name": name,
        "lastname":lastname,
        "id": id,
        "role": role
    }
def show_object(object_):
    print(object_)
def add_person():
    name=input("Digite el nombre:\n")
    lastname=input("Digite el apellido:\n")
    id=int(input("Digite el id:\n"))
    age=int(input("Digite la edad:\n"))
    role=int(input("Digite el rol"))

add_person()