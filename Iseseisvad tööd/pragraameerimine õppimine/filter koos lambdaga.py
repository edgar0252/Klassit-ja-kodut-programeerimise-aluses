items = [1, 2, 3, 4, 5, 6]
tingimus = lambda x: x % 2 == 0
vastus = []
for el in items:
    if tingimus(el) == True:
        vastus.append(el)
print(vastus)