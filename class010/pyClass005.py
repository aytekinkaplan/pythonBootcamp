print("American States and their capitals")
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida"]
capitals = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford", "Dover",
            "Tallahassee"]

for i in range(len(states)):
    print(i + 1, f"{states[i]}`s capital is", capitals[i], sep=" ")

for i, state in enumerate(states):
    print(i + 1, state, sep=". ")

print("Famous Car Brands")
cars = ["Ford", "BMW", "Fiat", "VW", "Audi"]
for i, car in enumerate(cars):
    print(i + 1, car, sep=". ")
