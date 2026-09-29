nums = [5, 2, 7]

#nums[3] = 100

nums.append(100) #peale viimast arvu listis lisab seda mids on sulusees
nums.insert(1, True) # paigaldab vajalikku indeksi peale seda väärtust mida oleme kirjutanud

b = [5, 6, 8]
nums.extend(b) # liidab esialgse listili uuead andmed teises listis
nums.sort()
#nums.reverse()

nums.pop(-2) #kustusab elementi määratud indeksis
nums.remove(6) #kidla numbri/väärtuse listis kustutamine mis iganes indeksis
#nums.clear() kustutab listi sise väärtused maha
 

#print(nums.count(5))
print(len(nums))
print(nums)


