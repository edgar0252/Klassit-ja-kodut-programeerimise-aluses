import unicodedata
def puhasta(tekst):
    puhastatud = ""
    tekst = unicodedata.normalize("NFD", tekst)
    for täht in tekst:
        if täht.isalpha() and unicodedata.combining(täht) == 0:
            puhastatud += täht
    return puhastatud


def is_anagram(left, right):
    if sorted(puhasta(left.lower())) == sorted(puhasta(right.lower())):
        return True
    return False

print(is_anagram("crâné", "crane"))