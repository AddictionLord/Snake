l = ["Ahoj", "Čau", "Nazdar"]

for pozdrav in l:
    if l == "Čau":
        l = "Changed"

print(l)

for index, pozdrav in enumerate(l, start=1):
    if pozdrav == "Čau":
        l[index - 1] = "Changed"

print(l)