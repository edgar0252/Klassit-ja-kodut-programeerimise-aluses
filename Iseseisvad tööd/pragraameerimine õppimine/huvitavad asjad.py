esn = int(input("kirjuta suvaline nummer"))
tsn = int(input("kirjuta teine suvaline nummer"))
print("praegu ma teen mata tegevused nende numbritega")
print(f"liitmine {esn} + {tsn} = {esn + tsn}")
print(f"lahutamine {esn} - {tsn} = {esn - tsn}")
print(f"korutamine {esn} * {tsn} = {esn * tsn}")
print(f"jagamine {esn} / {tsn} = {esn / tsn}")

if esn > tsn:
    print(True)
else:
    print(False)
    
if esn < tsn:
    print(True)
print(False)

