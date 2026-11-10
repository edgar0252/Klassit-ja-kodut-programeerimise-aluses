failinimi = str(input("Sisesta faili nimi:"))
otsitav_zanr = str(input("Sisesta žanr:"))
ajavahemik = str(input("Sisesta ajavahemik:"))

plaadid = []

with open(failinimi, encoding="utf-8") as f:
    sisu = f.readlines()
for rida in sisu:
    rida = rida.strip()
    osad = rida.split(", ")
    esitaja, album = osad[0].split(" - ")
    zanr = osad[1]
    aasta = int(osad[2])
    plaadid.append([esitaja, album, zanr, aasta])
#print(plaadid)

def otsi_zanri_järgi(otsitav_zanr):
    if otsitav_zanr == "":
        return plaadid
    vajalikku_zanr = []
    for plaat in plaadid:
        if plaat[2].lower() == otsitav_zanr.lower():
            vajalikku_zanr.append(plaat)
    return vajalikku_zanr

def otsi_ajavahemikku_jargi(ajavahemik):
    if ajavahemik == "":
        return otsi_zanri_järgi(otsitav_zanr)
    vajalikku_ajaga = []
    for aeg in otsi_zanri_järgi(otsitav_zanr):
        if aeg[3] == int(ajavahemik):
            vajalikku_ajaga.append(aeg)
    return vajalikku_ajaga

#tulemus = otsi_zanri_järgi(otsitav_zanr)
tulemus_ajaga = otsi_ajavahemikku_jargi(ajavahemik)

for plaat in tulemus_ajaga:
    print(f"{plaat[0]}-{plaat[1]}")

