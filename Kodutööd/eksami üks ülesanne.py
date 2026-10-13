def ristsumma(arv: int) -> int:
    rs = 0
    for el in (str(arv)):
        print(type(el), el)
        rs = rs + int(el)
    return rs


i = 1

while(True):
    i += 1
    if i**2 == ristsumma(i)**3:
        print(i)
        break