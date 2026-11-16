#try:
 #  x = int(input("sisesta numbri"))
 #   x += 5
 #   print(x)
#except ValueError:
#    print("tõ loh, vvedi chislo")


#x = 0
#while x == 0:
 #   try:
 #       x = int(input("sisesta numbri: "))
 #       x += 5
 #       print(x)
 #   except ValueError:
 #       print("tõ loh, vvedi chislo")

try:
    x = 5 / 1
except ZeroDivisionError:
    print("delenie na nol")
except ValueError:
    print("ne shifra")
else:
    print("to hui")
finally:
    print("nakonetsto")