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


#odavam hind leidmine kindla aja järgi
võimsus_kw = 1
tunnid = 4
#"ühe tunni sees on 4 korda 15 minuti seega kordame meie vajalik aega 4 ja siis saame kätte vahemik"
Akken = tunnid * 4
hinde_summa = []
for i in range(len(hinnad) - Akken + 1):
    summa = sum(hinnad[i:i+Akken])
    hinde_summa.append((paarid[i][0], summa))
parim = min(hinde_summa, key=lambda p: p[1])
print(f"Odavaim {tunnid} tundi algab: {parim[0]}, hindade summa: {parim[1]:.2f}")

mwh_veerandtunnis = võimsus_kw * 0.25 / 1000
maksumus = parim[1] * mwh_veerandtunnis
print(f"Võimsusega {võimsus_kw} kW maksab see {maksumus:.4f} €")


