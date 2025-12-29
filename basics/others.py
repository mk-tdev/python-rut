# Reduce
from functools import reduce
reduced = reduce(lambda x, y: x + y, nums)
print(reduced)  # Output: 15
# List Comprehension
squared = [x ** 2 for x in nums]
print(squared)  # Output: [1, 4, 9, 16, 25]
# Dictionary Comprehension
squared_dict = {x: x ** 2 for x in nums}
print(squared_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Set Comprehension
squared_set = {x ** 2 for x in nums}
print(squared_set)  # Output: {1, 4, 9, 16, 25}
# Generator Expression
squared_gen = (x ** 2 for x in nums)
print(list(squared_gen))  # Output: [1, 4, 9, 16, 25]
# List Comprehension with Condition
even_squared = [x ** 2 for x in nums if x % 2 == 0]
print(even_squared)  # Output: [4, 16]
# Dictionary Comprehension with Condition
even_squared_dict = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_squared_dict)  # Output: {2: 4, 4: 16}
# Set Comprehension with Condition
even_squared_set = {x ** 2 for x in nums if x % 2 == 0}
print(even_squared_set)  # Output: {16, 4}
# Generator Expression with Condition
even_squared_gen = (x ** 2 for x in nums if x % 2 == 0)
print(list(even_squared_gen))  # Output: [4, 16]
# Nested Comprehensions
nested_list = [[x * y for y in range(1, 4)] for x in range(1, 4)]
print(nested_list)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
# Nested Dictionary Comprehensions
nested_dict = {x: {y: x * y for y in range(1, 4)} for x in range(1, 4)}
print(nested_dict)  # Output: {1: {1: 1, 2: 2, 3: 3}, 2: {1: 2, 2: 4, 3: 6}, 3: {1: 3, 2: 6, 3: 9}}
# Nested Set Comprehensions
nested_set = {x * y for x in range(1, 4) for y in range(1, 4)}
print(nested_set)  # Output: {1, 2, 3, 4, 6, 8, 9}
# Nested Generator Expressions
nested_gen = (x * y for x in range(1, 4) for y in range(1, 4))
print(list(nested_gen))  # Output: [1, 2, 3, 4, 6, 8, 9]
# List Comprehension with Multiple Iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [(x, y) for x in list1 for y in list2]
print(combined)  # Output: [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
# Dictionary Comprehension with Multiple Iterables
combined_dict = {(x, y): x + y for x in list1 for y in list2}
print(combined_dict)  # Output: {(1, 4): 5, (1, 5): 6, (1, 6): 7, (2, 4): 6, (2, 5): 7, (2, 6): 8, (3, 4): 7, (3, 5): 8, (3, 6): 9}
# Set Comprehension with Multiple Iterables
combined_set = {x * y for x in list1 for y in list2}
print(combined_set)  # Output: {4, 5, 6, 8, 9, 10, 12, 15, 18}
# Generator Expression with Multiple Iterables
combined_gen = ((x, y) for x in list1 for y in list2)
print(list(combined_gen))  # Output: [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
# List Comprehension with Nested Loops
nested_combined = [(x, y) for x in list1 for y in list2 if x + y > 7]
print(nested_combined)  # Output: [(2, 6), (3, 5), (3, 6)]
# Dictionary Comprehension with Nested Loops
nested_combined_dict = {(x, y): x + y for x in list1 for y in list2 if x + y > 7}
print(nested_combined_dict)  # Output: {(2, 6): 8, (3, 5): 8, (3, 6): 9}
# Set Comprehension with Nested Loops
nested_combined_set = {x * y for x in list1 for y in list2 if x + y > 7}
print(nested_combined_set)  # Output: {12, 15, 18}
# Generator Expression with Nested Loops
nested_combined_gen = ((x, y) for x in list1 for y in list2 if x + y > 7)
print(list(nested_combined_gen))  # Output: [(2, 6), (3, 5), (3, 6)]
# List Comprehension with String Manipulation
string_list = ["hello", "world"]
capitalized = [s.capitalize() for s in string_list]
print(capitalized)  # Output: ['Hello', 'World']
# Dictionary Comprehension with String Manipulation
string_dict = {"name": "john", "age": 30}
capitalized_dict = {k: v.capitalize() if isinstance(v, str) else v for k, v in string_dict.items()}
print(capitalized_dict)  # Output: {'name': 'John', 'age': 30}
# Set Comprehension with String Manipulation
string_set = {"apple", "banana", "cherry"}
capitalized_set = {s.capitalize() for s in string_set}
print(capitalized_set)  # Output: {'Apple', 'Banana', 'Cherry'}
# Generator Expression with String Manipulation
string_gen = (s.capitalize() for s in string_list)
print(list(string_gen))  # Output: ['Hello', 'World']
# List Comprehension with Tuple Unpacking
tuple_list = [(1, 2), (3, 4), (5, 6)]
unpacked = [(x, y) for x, y in tuple_list]
print(unpacked)  # Output: [(1, 2), (3, 4), (5, 6)]
# Dictionary Comprehension with Tuple Unpacking
tuple_dict = {1: (2, 3), 4: (5, 6)}
unpacked_dict = {k: (x, y) for k, (x, y) in tuple_dict.items()}
print(unpacked_dict)  # Output: {1: (2, 3), 4: (5, 6)}
# Set Comprehension with Tuple Unpacking
tuple_set = {(1, 2), (3, 4), (5, 6)}
unpacked_set = {(x, y) for x, y in tuple_set}
print(unpacked_set)  # Output: {(1, 2), (3, 4), (5, 6)}
# Generator Expression with Tuple Unpacking
tuple_gen = ((x, y) for x, y in tuple_list)
print(list(tuple_gen))  # Output: [(1, 2), (3, 4), (5, 6)]
# List Comprehension with Conditional Logic
conditional_list = [x if x % 2 == 0 else x * 2 for x in nums]
print(conditional_list)  # Output: [2, 2, 6, 4, 10]
# Dictionary Comprehension with Conditional Logic
conditional_dict = {x: (x if x % 2 == 0 else x * 2) for x in nums}
print(conditional_dict)  # Output: {1: 2, 2: 2, 3: 6, 4: 4, 5: 10}
# Set Comprehension with Conditional Logic
conditional_set = {x if x % 2 == 0 else x * 2 for x in nums}
print(conditional_set)  # Output: {2, 4, 6, 10}
# Generator Expression with Conditional Logic
conditional_gen = (x if x % 2 == 0 else x * 2 for x in nums)
print(list(conditional_gen))  # Output: [2, 2, 6, 4, 10]
# List Comprehension with String Formatting
formatted_list = [f"Number: {x}" for x in nums]
print(formatted_list)  # Output: ['Number: 1', 'Number: 2', 'Number: 3', 'Number: 4', 'Number: 5']
# Dictionary Comprehension with String Formatting
formatted_dict = {x: f"Number: {x}" for x in nums}
print(formatted_dict)  # Output: {1: 'Number: 1', 2: 'Number: 2', 3: 'Number: 3', 4: 'Number: 4', 5: 'Number: 5'}
# Set Comprehension with String Formatting
formatted_set = {f"Number: {x}" for x in nums}
print(formatted_set)  # Output: {'Number: 1', 'Number: 2', 'Number: 3', 'Number: 4', 'Number: 5'}
# Generator Expression with String Formatting
formatted_gen = (f"Number: {x}" for x in nums)
print(list(formatted_gen))  # Output: ['Number: 1', 'Number: 2', 'Number: 3', 'Number: 4', 'Number: 5']
# List Comprehension with String Manipulation and Conditional Logic
string_list = ["hello", "world", "python"]
conditional_string_list = [s.upper() if len(s) > 4 else s for s in string_list]
print(conditional_string_list)  # Output: ['hello', 'WORLD', 'PYTHON']
# Dictionary Comprehension with String Manipulation and Conditional Logic
conditional_string_dict = {s: s.upper() if len(s) > 4 else s for s in string_list}
print(conditional_string_dict)  # Output: {'hello': 'hello', 'world': 'WORLD', 'python': 'PYTHON'}
# Set Comprehension with String Manipulation and Conditional Logic
conditional_string_set = {s.upper() if len(s) > 4 else s for s in string_list}
print(conditional_string_set)  # Output: {'hello', 'WORLD', 'PYTHON'}
# Generator Expression with String Manipulation and Conditional Logic
conditional_string_gen = (s.upper() if len(s) > 4 else s for s in string_list)
print(list(conditional_string_gen))  # Output: ['hello', 'WORLD', 'PYTHON']
# List Comprehension with Nested Loops and Conditional Logic
nested_conditional_list = [(x, y) for x in list1 for y in list2 if x + y > 7]
print(nested_conditional_list)  # Output: [(2, 6), (3, 5), (3, 6)]
# Dictionary Comprehension with Nested Loops and Conditional Logic
nested_conditional_dict = {(x, y): x + y for x in list1 for y in list2 if x + y > 7}
print(nested_conditional_dict)  # Output: {(2, 6): 8, (3, 5): 8, (3, 6): 9}
# Set Comprehension with Nested Loops and Conditional Logic
nested_conditional_set = {x * y for x in list1 for y in list2 if x + y > 7}
print(nested_conditional_set)  # Output: {12, 15, 18}
# Generator Expression with Nested Loops and Conditional Logic
nested_conditional_gen = ((x, y) for x in list1 for y in list2 if x + y > 7)
print(list(nested_conditional_gen))  # Output: [(2, 6), (3, 5), (3, 6)]
# List Comprehension with String Manipulation and Nested Loops
string_nested_list = [[f"{x}-{y}" for y in list2] for x in list1]
print(string_nested_list)  # Output: [['1-4', '1-5', '1-6'], ['2-4', '2-5', '2-6'], ['3-4', '3-5', '3-6']]
# Dictionary Comprehension with String Manipulation and Nested Loops
string_nested_dict = {x: [f"{x}-{y}" for y in list2] for x in list1}
print(string_nested_dict)  # Output: {1: ['1-4', '1-5', '1-6'], 2: ['2-4', '2-5', '2-6'], 3: ['3-4', '3-5', '3-6']}
# Set Comprehension with String Manipulation and Nested Loops
string_nested_set = {f"{x}-{y}" for x in list1 for y in list2}
print(string_nested_set)  # Output: {'1-4', '1-5', '1-6', '2-4', '2-5', '2-6', '3-4', '3-5', '3-6'}
# Generator Expression with String Manipulation and Nested Loops
string_nested_gen = (f"{x}-{y}" for x in list1 for y in list2)
print(list(string_nested_gen))  # Output: ['1-4', '1-5', '1-6', '2-4', '2-5', '2-6', '3-4', '3-5', '3-6']
# List Comprehension with String Manipulation and Nested Loops and Conditional Logic
string_nested_conditional_list = [[f"{x}-{y}" for y in list2 if x + y > 7] for x in list1]
print(string_nested_conditional_list)  # Output: [['2-6'], ['3-5', '3-6']]
# Dictionary Comprehension with String Manipulation and Nested Loops and Conditional Logic
string_nested_conditional_dict = {x: [f"{x}-{y}" for y in list2 if x + y > 7] for x in list1}
print(string_nested_conditional_dict)  # Output: {1: [], 2: ['2-6'], 3: ['3-5', '3-6']}
# Set Comprehension with String Manipulation and Nested Loops and Conditional Logic
string_nested_conditional_set = {f"{x}-{y}" for x in list1 for y in list2 if x + y > 7}
print(string_nested_conditional_set)  # Output: {'2-6', '3-5', '3-6'}
# Generator Expression with String Manipulation and Nested Loops and Conditional Logic
string_nested_conditional_gen = (f"{x}-{y}" for x in list1 for y in list2 if x + y > 7)
print(list(string_nested_conditional_gen))  # Output: ['2-6', '3-5', '3-6']
