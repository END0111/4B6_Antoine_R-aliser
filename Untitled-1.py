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