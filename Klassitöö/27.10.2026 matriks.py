maatriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

def peadiagonaal(matriks):
    suurus =  len(matriks)
    for i in range(suurus):
        print(matriks[i][i])

def kõrvdiagonaal(matriks):
    suuurus = len(matriks)
    for i in range(suuurus):
        #veerg = suuurus - 1 - i
        #print(matriks[i][veerg])
        #print(matriks[i][-i-1])
        print(matriks[i][suuurus - i - 1])


def print_matriks(matriks):
    for rida in matriks:
        print(rida)



#print_matriks(maatriks)
#peadiagonaal(maatriks)
kõrvdiagonaal(maatriks)