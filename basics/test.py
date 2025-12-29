
teamA = ["John", "Jane", "Jack", "Jill"]
teamB = ["Tom", "Tina", "Tim", "Tina"]

# allPlayers = teamA + teamB

allPlayers = teamA + teamB

allPlayers.append("Kim")

allPlayers.remove("Tina")


allPlayers.sort()

friends = allPlayers.copy()


# Dictionary

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(person)
print(person["name"])
print(person.get("age"))

person["age"] = 31
print(person)

print(person.keys())
print(person.values())

for key in person.keys():
  print(key)

print(person.items())

for key, value in person.items():
  print(key, value)