#"1.1 leida еhest suurem tжisarv, mille ruut vЁrdub selle arvu kümnendnumbrite summa (ristsumma) kuubiga"

#n1, n1^2 == RS^3

def ristsumma(arv:int)-> int:
    rs = 0
    for el in (str(arv)):
        print(type(el), el)
        rs = rs + int(el)
    return rs
        
#print(ristsumma(4321))

i = 2

while(True):
    if i**2 == ristsumma(i)**3:
        print(i)
        break
    else:
        i += 1
print(27**2, (2+7)**3)
