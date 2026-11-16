count = {True: 0}
country = {4: 3}
cortez = {(5, 6): 3}
#print(country[4])
#print(count[True])
#print(cortez[(5, 6)])


real_country = {'code': 'est', 'name': 'Estonia', 'population': 1100}
#real_country = dict(code='EST', name='Estonia')
#print(real_country['name']

#for key in real_country:
    #print(key)

#for key, value in real_country.items():
    #print(key, " - ", value)

#print(real_country.get('code'))

#real_country.clear() #kustutab terve listi
#print(real_country)

#real_country.pop('name') #kustutab valitud element

#real_country.popitem() #kustutab viimane element

#print(real_country.keys())

#print(real_country.values())

#print(real_country.items())

#real_country['code'] = 'none'  #muudame väärtus

#print(real_country)



persone = {
    'user_1':{
        'first_name': 'Jon',
        'last_name': 'marlou',
        'age': '45',
        'address': ['hui teab', 'kus ta elab'],
        'hinned': {'matha': 5, 'physic': 4}
    }


    }
print(persone['user_1']['address'][1])