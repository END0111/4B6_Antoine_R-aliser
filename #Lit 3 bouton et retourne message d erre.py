#Lit 3 bouton et retourne message d erreur si..
def readButtons():
    return (True, False, True, "You lose")

(isBoutonPressed1, isBoutonPressed2, isBoutonPressed3, YouLose) = readButtons()
if YouLose == "OK":
    print("isBoutonPressed1")
    print("isBoutonPressed2")
    print("isBoutonPressed3")
else:
    print("There is an" + " L + SKILL_ISSUE")


#nomEtAgePersonnes = [("Esteban", True, 19), ("Jerry", True, 13)]
#for nom, alive, age in nomEtAgePersonnes:
#    print(nom)
#    print(alive)
#   print(age)

class Person:
    def __init__(self, name, age, alive):
        self.name = name
        self.age = age
        self.alive = alive

p1 = Person("Esteban", 19, True)
p2 = Person("Jerry", 13, True)

people = [p1, p2]
for person in people:
    print(person.name)
    print(person.age)
    print(person.alive)

p1 = ("nom": "Esteban", "age": 19)
p2 = ("nom": "Jerry", "age": 13)
people = [p1, p2]
for person in people:
    print(person["nom"])
    print(person["age"])

