#tärn = "*"
#for i in range(6):
#    print(tärn*(i+1))
#
#for i in range(1,7):
#    print(tärn*i)
#
def tärnide_trepp(tärn):
    for i in range(1, 7):
        print(tärn * i)

#tärnide_trepp("*")

def tärnide_trepp_2(tärn):
    for i in range(1, 7):
        print(" " * (6 - i) + tärn * i)

#tärnide_trepp_2("*")

def tärnide_trepp_3(tärn):
    for i in range(1, 7):
        print(" " * (6 - i) + (tärn + " ") * i)
#tärnide_trepp_3("*")


def tärnide_trepp_4(tärn):
    for i in range(1, 7):
        print(" " * (6 - i) + tärn * (2 * i - 1))
###tärnide_trepp_4("*")

###natuke vale###
def opilase_variant(height):
    for i in range(height):
        spaces = " " * (height - i)
        stars = " * " * (i + 1)
        print(spaces, stars)
#opilase_variant(7)

###parem###

def opilase_variant2(height, sumbol):
    for i in range(height):
        spaces = " " * (height - i)
        print(spaces, sumbol * (i * 2 - 1))
#opilase_variant2(7, "#")

def opilase_varian_r(kordus, sumbol):
    for i in range(kordus):
        print((kordus - i) * " " + (i * 2 - 1) * sumbol + (kordus - i) * " " + "I")
#opilase_varian_r(5, "l")


def minu_pro_raskeee(kõrgus, sümbol):
    for i in range(kõrgus):
        print(i * " " + (((kõrgus - i - 1) * 2)+ 1) * sümbol + (i*""))
#minu_pro_raskeee(4,"p")





def super_duper_puper_scuper(kõrgus, sümbol):
    for i in range(kõrgus):
        print(((kõrgus - i) * " " + (i * 2 + 1) * sümbol + ((kõrgus - i)+1) * " " + "I " + " " * i ) + (((kõrgus - i - 1) * 2)+ 1) * sümbol )

super_duper_puper_scuper(4,"p")