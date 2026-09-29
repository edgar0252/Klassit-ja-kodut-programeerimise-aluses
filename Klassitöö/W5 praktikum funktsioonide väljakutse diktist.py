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

def taisarvuline_jagamine(a,b):
    return a // b

x = int(input("sisesta esimest nubri: "))
y = int(input("sisesta teine nubri: "))
tehe = input("tehte tüüb: ")


operaatorid = {
    "+" : summa,
    "-" : lahutamine,
    "*" : korrutamine,
    "/" : jagamine,
    "//" : taisarvuline_jagamine
    }

print(operaatorid[tehe](x,y))