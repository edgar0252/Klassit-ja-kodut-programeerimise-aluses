args = [9,8,7,1,2,3,4,5,6,7,8]
kalevipoeg = "soomlased kirjutasid maha meie eepose"





def threesmalest(args):
    sordi_aretus = sorted(args)
    return sordi_aretus[0:3]
    #return sordi_aretus[0:3]
print(threesmalest(args))
print(len(args))
print(min(args))
print(max(args))
print(threesmalest(args)[0:3])

print(len(kalevipoeg))
print(max(kalevipoeg))
print(min(kalevipoeg))



koodid = [ord(m) for m in kalevipoeg]
print(min(koodid))



