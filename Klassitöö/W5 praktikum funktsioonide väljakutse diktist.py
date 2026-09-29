def summa (a,b):
    #print(a+b)
    return a + b

def lahutamine (a, b):
    #print(a - b)
    return a - b

def korrutamine (a, b):
    #print(a * b)
    return a * b

def jagamine (a, b):
    #print(a / b)
    return a / b

x = int(input("sisesta esimest nubri: "))
y = int(input("sisesta teine nubri: "))
tehe = input("tehte tüüb: ")


operaatorid = {
    "+" : summa(x,y),
    "-" : lahutamine(x,y),
    "*" : korrutamine(x,y),
    "/" : jagamine(x,y)}

print(operaatorid[tehe])