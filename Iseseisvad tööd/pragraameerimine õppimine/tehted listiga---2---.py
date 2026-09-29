n = int(input("enter length:"))

userlist = []

i = 0
while i < n:
    string = "enter element #" + str(i + 1) + ": "
    userlist.append(input(string))
    i += 1

print(userlist)
