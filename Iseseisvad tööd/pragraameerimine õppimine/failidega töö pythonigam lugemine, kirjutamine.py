#file = open("text.txt", "w")

#file.write("ja hotchu pitsu.......\n")
#file.write("ja hotchu pitsu.......")


#file.close()

#fuil = open("texas.txt", "a")

#fuil.write("ja hotchu pitsu.......\n")
#fuil.write("ja hotchu pitsu.......\n")


#fuil.close()

#data = input("sisesta teksti:")

#fiksik = open("fiksik.txt","w")
#fiksik.write(data)
#fiksik.close()

#nubl = open("text.txt","r")
#text = nubl.read()
#for lin in nubl:
 #   print(lin)
#nubl.close()

with open("text.txt", "r") as f:
    text = f.read()

for line in text.splitlines():
    print(line)