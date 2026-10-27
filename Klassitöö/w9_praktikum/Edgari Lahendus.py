with open("hinnad.csv") as f:
    sisu = f.readlines()

paarid = []
for rida in sisu[1:]:
    aeg, hind = rida.strip().split(";")
    paarid.append((aeg, float(hind)))

hinnad = []
for aeg, hind in paarid:
    hinnad.append(hind)
keskmine_hind = round(sum(hinnad) / len(hinnad), 2)

with open("odav.txt", "w") as odav, open("kallis.txt", "w") as kallis:
    for aeg,hind in paarid:
        if hind < keskmine_hind:
            odav.write(f"{aeg};{hind}\n")
        else:
            kallis.write(f"{aeg};{hind}\n")

odavaim = min(paarid, key=lambda p: p[1])
kalleim = max(paarid, key=lambda p: p[1])

print(f"Kõige odavam: {odavaim[0]} – {odavaim[1]} €/MWh")
print(f"Kõige kallim: {kalleim[0]} – {kalleim[1]} €/MWh")



