add = lambda x, y: x + y
print(add(1, 2))

# advanced

square = lambda x: x ** 2
print(square(2))

# map
numbers = [1, 2, 3, 4, 5]
# without lambda
numbers_squared = [x ** 2 for x in numbers]
print("numbers_squared", numbers_squared)

squared = list(map(lambda x: x ** 2, numbers))
print("squared", squared)

# filter

# without lambda
even_numbers = [x for x in numbers if x % 2 == 0]
print("even_numbers", even_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("even_numbers", even_numbers)

# sort
numbers.sort(key=lambda x: x % 2 == 0)
print("numbers", numbers)


# map, filter samples

def extracted_function(x):
    return x ** 2

print(list(map(extracted_function, numbers)))

print(list(filter(extracted_function, numbers)))
