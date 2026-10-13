hinnad = {"09:00": 3.23, "02:00": -0.22, "18:15": 5.28, "13:00": 1.50}

samm1 = hinnad.items()
print("Samm 1:", list(samm1))

samm3 = sorted(samm1, key=lambda paar: paar[1])
print("Samm 3:", samm3)

samm4 = dict(samm3)
print("Samm 4:", samm4)