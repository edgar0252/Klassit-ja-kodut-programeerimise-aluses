class Koer:
    def __init__(self, name):     # käivitub, kui kirjutad Koer("Rex")
        self.name = name          # koer jätab nime meelde
        self.trikid = []          # igal koeral oma list

    def opi(self, trikk):         # meetod = funktsioon klassi sees
        self.trikid.append(trikk)


#rex = Koer("Rex")
#rex.opi("istu")
#print(rex.name)        # Rex
#print(rex.trikid)


class student:
    def __init__(self, name):
        self.name = name
        self.hinne = []

    def add_eksam(self, hinne):
        self.hinne.append(float(hinne))

    def get_mean(self):
        return sum(self.hinne) / len(self.hinne)


class School:
    def __init__(self, name):
        self.name = name
        self.opilased = []

    def add_student(self, student):
        self.opilased.append(student)

    def get_mean(self):
        keskmised = []
        for s in self.opilased:
            keskmised.append(s.get_mean())
        return sum(keskmised) / len(keskmised)

    def get_best_student(self):
        return max(self.opilased, key=lambda s: s.get_mean())
hkis = School("hkis")
for nimi, hinded in (("alice", (1, 2, 3)),
                     ("bob", (2, 3, 4)),
                     ("catherine", (3, 4, 5)),
                     ("daniel", (4, 5, 6))):
    s = student(nimi)
    for h in hinded:
        s.add_eksam(h)
    hkis.add_student(s)

#print(hkis.get_mean())                  # 3.5
#print(hkis.get_best_student().name)









import requests

vastus = requests.get("https://example.com")   # küsi lehte
print(vastus.text)