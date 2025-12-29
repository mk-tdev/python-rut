from joblib import Parallel, delayed
from time import time

nums = [1, 2, 3, 4, 5]

squared = []
for num in nums:
  square = num ** 2
  squared.append(square)

print(squared)

# List Comprehension
comp_squared = [num*10 for num in nums]
print(comp_squared)

phones = ["iPhone 12", "iPhone 13", "iPhone 14", "Google Pixel 6", "Samsung Galaxy S21"]
comp_phones = [phone.title() for phone in phones if "iPhone" not in phone]
print(comp_phones)

print([n*3 for n in range(1, 10)])
print(list(range(1, 10)))

# Parallel Processing
time_1 = time()
Parallel(n_jobs=1)(delayed(lambda x: x**2)(i) for i in range(1000000))
time_2 = time()
print(time_2 - time_1)