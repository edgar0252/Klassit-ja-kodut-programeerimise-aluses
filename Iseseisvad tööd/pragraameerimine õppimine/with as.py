try:
    with open("text.txt", "r", encoding="utf-8") as file:
        file.read()
except FileNotFoundError:
    print("fila netu debil")
