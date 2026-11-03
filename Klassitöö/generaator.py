
def loenda_alla(n):
    print("algus")
    while n > 0:
        yield n
        n -= 1
    print("Lõpp")

for arv in loenda_alla(5):
    print(arv)