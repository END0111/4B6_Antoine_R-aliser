Tuple0 = ("bobine", "condensateur", 20, True, "LED")
Tuple1 = ("bobine", "condensateur", 10, False, "LED")
Tuples = [Tuple0, Tuple1]
for composant1, composant2, ammount, isInStock, composant3 in Tuples:
    print(composant1)
    print(composant2)
    print(ammount)
    print(isInStock)
    print(composant3)

# Tuple is used to isolate different variables in a list
# can be used in databases 
# need a () to be registered