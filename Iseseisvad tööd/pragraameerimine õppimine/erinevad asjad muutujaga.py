word = "itpeoger"
worrd = "Purjetamine, regatt, paad"
print(word[1])#prindime sümbol mis on sisestatud indeksi peal	
print(len(word))#loeme kui palju sümboli on muutuja sees
print(word.count("p"))#arvutame kui palju korda muutujas kasutatakse sümboli

print(word.upper())#teisendab väikekiri kõrg kirjaks
print(word.capitalize())#teeb esimene täht suureks ja teised teeb väiksemaks
print(word.find("p"))#otsime sõnas täpne täht, funktsioon tagastab tähe nubri indeksi
print(worrd.split(", "))#loob listi sünadest, Kasutab "," selleks et saada aru kus on sõnad eraldi



hobby = worrd.split(", ")
print(hobby[1])

#Teeme listsi kõik eraldi sõnad suure esimese tähega

for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()
print(hobby)

########

for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()

result = ", ".join(hobby)
print(result)















