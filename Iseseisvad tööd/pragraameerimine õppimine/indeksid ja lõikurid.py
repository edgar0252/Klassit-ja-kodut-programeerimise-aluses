word = "purjetamine"

print(word[0:4])#prindi elemendid alustades 0, lüpetame 4 peal
print(word[4:4])# 0 elemendi on prinditud
print(word[4:6])# 4 - 6 on prinditud
print(word[0:])#kõik elemendit on prinditud
print(word[0:-1])# prindime kõik elemendid aga viimane võtame ära
print(word[1:-1:2])# prindime elemendit alustades 1 indeksi, ei prindime viimane element, prindime iga teine element


lis = [6, 4, "sipsik", True, 6.5] #difineerisime muutuja mis sees on list
print(lis[2]) #prindime 2 element listis
print(lis[2:]) #prindime kõik elemendid peale 2 indeksi
print(lis[2:-1])
print(lis[2:5:2])
print(lis[::-1]) # põõrame listi
print(lis[::2])