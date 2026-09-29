def summa (a,b):
    return a + b

def lahutamine (a, b):
    return a - b

def korrutamine (a, b):
    return a * b

def jagamine (a, b):
    return a / b

a = int(input("sisesta esimest nubri: "))
b = int(input("sisesta teine nubri: "))
tehe = input("tehte tüüb: ")

if tehe == "+":
    print(summa(a, b))
if tehe == "-":
    print(lahutamine(a,b))
if tehe == "*":
    print(lahutamine(a,b))
if tehe == "/":
    print(lahutamine(a,b))
else:
    print("vale tehe")