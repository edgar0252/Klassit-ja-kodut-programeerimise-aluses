#data = set("hello")

data = {5, 7, 6, 5, 5, 4}

data.add(32)
data.update([32, True, "32", 2, 3])
data.remove(5)
data.pop()
data.clear()
#print(data)

nums = [5, 7, 5, 4, 3, 3, 6, 5, 98, 1000]
new_nums = set(nums)
#print(new_nums)

new_data = frozenset([5, 7, 5, 4, 3, 3, 6, 5, 98, 1000])
print(new_data)