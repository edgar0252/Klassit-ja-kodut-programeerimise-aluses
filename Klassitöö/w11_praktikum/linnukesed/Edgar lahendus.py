fail_nimi = str(input("Sisesta failinimi:"))

def linnud_sõnastikku(failinimi):
    linnud = {}
    with open(failinimi, encoding="utf-8") as f:
        for rida in f:
            rida = rida.strip()
            if rida:
                nimi, arv = rida.split(",")
                linnud[nimi] = int(arv)
    return linnud
linnud = linnud_sõnastikku(fail_nimi)
arv_var = str(input("Sisesta arv:"))

for nimi, arv in linnud.items():
    if int(arv) > int(arv_var):
        print(f"{nimi} ({arv})")

kokku = sum(linnud.values())
print(f"Juku nägi väljas {kokku} lindu.")