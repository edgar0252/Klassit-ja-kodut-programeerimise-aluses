"kontrollida, kas antud kahe naturaalarvu kümnendnumbrite hulga on ühisosata."
"näiteks"
"arvude 9124 ja 35876 kümnendnumbrite hulgad on ühisosata;"
"arvude 91624 ja 358761 kümnendnumbrite hulka ühisosa on {1,6}."


def yhis_kassa(n_1, n_2):
    str_2 = str(n_2)
    yhised_elemendid = []
    for el_1 in str(n_1):
        if el_1 in str_2:
            yhised_elemendid.append(el_1)




    return set(yhised_elemendid)

print(yhis_kassa(9124, 35876))
print(yhis_kassa(9124, 358213476))
print(yhis_kassa(9124, 35898762348545676))
