import csv

def loe_tooted(failinimi):
    tooted = []
#loeme faili sisse
    with open(failinimi,encoding="utf-8") as f:
        lugeja = csv.DictReader(f, delimiter=";")

        for rida in lugeja:
            # teisendan teksti arvud tavaarvudeks, s.t. "250" teen 250
            rida["hind_km_ta"] = float(rida["hind_km_ta"])
            rida["laoseis"] = int(rida["laoseis"])
            rida["km_maar"] = int(rida["km_maar"])
            tooted.append(rida) #salvestan teisendatud väärtused uue listi sõnastiku formaadis ehk saan loend millega on mugav töötada
    return tooted

#loon uus funktsiooni mis arvutab hind käibemaksuga
def hind_km_ga(hind, maar):
    if hind < 0:
        raise ValueError("hind ei saa olla negatiivne")
    return round(hind * (1 + maar / 100), 2)

def uus_maar(maar):
    if maar == 22:
        return 24
    elif maar in (0, 9, 13, 24):
        return maar
    else:
        raise ValueError(f"Määr {maar}% pole Eestis kehtiv")

def lao_vaartus(tooted, km_ga=False):
    #selle funktsiooni sees arvutame hind vana käibemaksuga
    summa = 0
    for toode in tooted:
        hind = toode["hind_km_ta"]
        if km_ga:
            hind = hind_km_ga(hind, toode["km_maar"])
        summa += hind * toode["laoseis"]
    return summa

def uued_tooted(tooted):
    tulemus = []
    for toode in tooted:
        uus = dict(toode)                           # koopia, et algne ei muutuks
        uus["km_maar"] = uus_maar(uus["km_maar"])
        tulemus.append(uus)
    return tulemus

def main():
    tooted = loe_tooted("tooted.csv")
    print(f"Tooteid kokku: {len(tooted)}")
    maarad = {}
    for toode in tooted:
        m = toode["km_maar"]
        if m in maarad:
            maarad[m] += 1
        else:
            maarad[m] = 1
    for maar, mitu in maarad.items():
        print(f"Määraga {maar}%: {mitu} toodet")
    otsas = []
    for toode in tooted:
        if toode["laoseis"] == 0:
            otsas.append(toode["nimetus"])
    print(f"Laost otsas: {len(otsas)} toodet")
    for nimi in otsas:
        print(f"  - {nimi}")
    kalleim = max(tooted, key=lambda t: t["hind_km_ta"])
    odavaim = min(tooted, key=lambda t: t["hind_km_ta"])
    print(f"Kõige kallim: {kalleim['nimetus']} ({kalleim['inventari_nr']}), "
          f"{kalleim['hind_km_ta']} € km-ta, "
          f"{hind_km_ga(kalleim['hind_km_ta'], kalleim['km_maar'])} € km-ga")
    print(f"Kõige odavam: {odavaim['nimetus']} ({odavaim['inventari_nr']}), "
          f"{odavaim['hind_km_ta']} € km-ta, "
          f"{hind_km_ga(odavaim['hind_km_ta'], odavaim['km_maar'])} € km-ga")
    print(f"Lao väärtus km-ta: {lao_vaartus(tooted):.2f} €")
    vana = lao_vaartus(tooted, km_ga=True)
    uus = lao_vaartus(uued_tooted(tooted), km_ga=True)
    print(f"Lao väärtus km-ga (vana määr): {vana:.2f} €")
    print(f"Lao väärtus km-ga (uus määr):  {uus:.2f} €")
    print(f"Vahe: {uus - vana:.2f} €")
    salvesta_hinnakiri(tooted, "tooted_2025_07.csv")
    print("Uus hinnakiri salvestatud: tooted_2025_07.csv")


def salvesta_hinnakiri(tooted, failinimi):
    veerud = ["inventari_nr", "nimetus", "hind_km_ta", "laoseis", "km_maar", "hind_km_ga"]
    with open(failinimi, "w", encoding="utf-8", newline="") as f:
        kirjutaja = csv.DictWriter(f, fieldnames=veerud, delimiter=";")
        kirjutaja.writeheader()
        for toode in uued_tooted(tooted):
            toode["hind_km_ga"] = hind_km_ga(toode["hind_km_ta"], toode["km_maar"])
            kirjutaja.writerow(toode)


main()

