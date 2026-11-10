#minu_failinimi = str(input("Sisesta ostunimekirja faili nimi:"))
#toakaslane_failinimi1 = str(input("Sisesta esimese toakaaslase ostukorvi faili nimi:"))
#toakaslane_failinimi2 = str(input("Sisesta teise toakaaslase ostukorvi faili nimi:"))

def loe_nimekiri(faili_nimi):
    with open(faili_nimi, encoding="utf-8") as f:
        for rida in f:
            if rida:
                yield rida.strip().lower().capitalize()

def lisa_hulka(hulk, nimekiri):
    for produkt in nimekiri:
        hulk.add(produkt)



jaagu_nimekiri = loe_nimekiri("jaak_nimekiri.txt")
koidu_ehalendu_nimekiri = loe_nimekiri("koidu-ehalend.txt")

yhis_nimekiri = set()

lisa_hulka(yhis_nimekiri, jaagu_nimekiri)
lisa_hulka(yhis_nimekiri, koidu_ehalendu_nimekiri)

print(yhis_nimekiri)

jaagu_set = set([el for el in loe_nimekiri("jaak_nimekiri.txt")])

koidu_ehalend_set = set([el for el in loe_nimekiri("koidu-ehalend.txt")])

print("ühend", jaagu_set.union(koidu_ehalend_set))
print("ühend", jaagu_set | koidu_ehalend_set)

print("ühisosa", jaagu_set.intersection(koidu_ehalend_set))
print("ühisosa", jaagu_set & koidu_ehalend_set)

print("vahe", jaagu_set.difference(koidu_ehalend_set))
print("vahe", jaagu_set - koidu_ehalend_set)