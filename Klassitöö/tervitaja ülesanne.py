def kontrollitav(vanuse_kontroll):
    vanused = {14: "süüdiv",
               16: "KOV",
               18:["RK", "EP", "õlu"],
               21:"kasiino",
               24:"A-kat",
               40:"President"
               }
    for vanus_nimekirjas in vanused.keys():
        if vanuse_kontroll >= vanus_nimekirjas:
            print(vanused[vanus_nimekirjas])
 #   if vanuse_kontroll >= 14:
 #       print("suudi")
 #   if vanuse_kontroll >= 16:
 #       print("void valida")
 #   if vanuse_kontroll >= 18:
 #        print("taisealine")
 #   if vanuse_kontroll >= 21:
 #       print("kasiino")
 #   if vanuse_kontroll >= 24:
 #       print("A-kat")
 #   if vanuse_kontroll >= 40:
 #       print("president")

nimi = input("mis su nimi on nimi?")
sunniaasta = int(input("mis su sunniaasta on?"))
vanus = 2026 - sunniaasta

kontrollitav(vanus)
#print("Tere,", nimi, "sa oled umbes",vanus,"aastat vana")
# print(f"Tere {nimi}! sa oled umbes {vanus} aastat vana")
# print(type(nimi))
# if vanus >= 14:
#     print("suudi")
# if vanus >= 16:
#     print("void valida")
# if vanus >= 18:
#     print("taisealine")
# if vanus >= 21:
#     print("kasun")
# if vanus >= 24:
#     print("A-kat")
# if vanus >= 40:
#     print("president")
# else:
#     print(pensioneer)