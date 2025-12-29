def greet_proper(fn):
  def wrapper():
    print("Hello, how are you?")
    fn()
    print("Goodbye!")
  return wrapper

@greet_proper
def greet():
  print("Hello, code with mk!")

# this is not needed because of the @greet_proper decorator
# greet = greet_proper(greet)
greet()
