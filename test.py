l = ["Ahoj", "Jak", "Se", "Máš"]

try:
    l.remove("?")
except ValueError:
    pass

print("Ahoj")


move = [1, 0]

if move == 1 or move == [1, 0]:
    print(True)