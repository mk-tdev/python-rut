more_numbers = [76, 71, 1, 9, 32, 99]

print(more_numbers.sort())

sorted_numbers = sorted(more_numbers, reverse=True)
print(sorted_numbers)
print(more_numbers)

users = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 30},
    {"name": "Doe", "age": 22},
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 35},
]

# Sort the list of dictionaries by age
sorted_users = sorted(users, key=lambda x: x["age"])
print(sorted_users)