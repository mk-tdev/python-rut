# Python Lambda Function
# In Python, a lambda is an anonymous, 
# small, and inline function defined using the lambda keyword

# Syntax:
# lambda arguments: expression

square = lambda x: x ** 2
add = lambda a, b: a + b

numbers = [1, 2, 3, 4]
squared = list(
  map(lambda x: x ** 2, numbers)
)

numbers_2 = [1, 2, 3, 4, 5, 6]
even_numbers = list(
  filter(lambda x: x % 2 == 0, numbers_2)
)

def main():
  print(even_numbers)

# map & filter
# sorting


if __name__ == "__main__":
  main()