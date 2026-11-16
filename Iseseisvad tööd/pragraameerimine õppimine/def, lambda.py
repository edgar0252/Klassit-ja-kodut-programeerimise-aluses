def bulka_func():
    pass#miite middage funktsioon ei tee ehk mitte midagi ei tagasta



def bulka_func2():
    print("hi", end="")
    print("!")
#bulka_func2()

def bulka_func3(word):
    print(word, end="")
    print("!")

#bulka_func3("Hihihihiih")

def summa(a, b):
    #res = a + b
    #print("result:", res)
    #return res
    return a + b

#res = summa (5, 7)
#print(res)

#summa(5, 7)
#summa("H", "i")


nums_1 = [6, 5, 3, 8 ,9, 12]

#min = nums_1[0]
#for el in nums_1:
    #if el < min:
        #min = el

#print(min)



nums_2 = [6, 6.4, 5.004, 3.1, 8.90, 9.15, 12.4]

def minnimal(lis):
    return min(lis)

def minnnimal(lis):
    min_num = lis[0]
    for el in lis:
        if el < min_num:
            min_num = el
    print(min_num)

print(minnimal(nums_2))
minnnimal(nums_1)



func = lambda x, y: x * y
res = func(5, 2)
print(res)




