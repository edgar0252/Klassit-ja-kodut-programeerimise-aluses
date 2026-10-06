#cortez/tuple = list aga konstantne ehk võhem kaalub

data = (4, 6, 7, 8, 9, True, 5.6, "Hello")
#data[0] = 5  pole võimalik tehe
print(data[1:5])

print(data.count(6))
print(len(data))
print(data)

#prindime eraldi iga tuple element
for el in data:
    print(el)
    
    
#loome tuple from listi
nums = [5, 6, 7, 8, 9, 10, 100, 1000]

new_data = tuple(nums)
print(new_data)
#############################################################


worddd= tuple("hello world")
print(worddd)






datt = 5, 6, 7, True 
print(datt)

dat = (5)
print(dat)

daa = (5,)
print(daa)

da = 5,
print(da)