def ristsumma(arv: int) -> int:
    rs = 0
    for el in (str(arv)):
        print(type(el), el)
        rs = rs + int(el)
    return rs


print(ristsumma(987))