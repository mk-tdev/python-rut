from dataclasses import dataclass, field

@dataclass #(frozen=True)
class Person:
  name: str
  age: int
  password: str = field(repr=False)
  is_student: bool = False

  def __post_init__(self):
    if self.age < 0:
      raise ValueError("Age cannot be negative")

person1 = Person(name="Alice", age=30, password="secret123")
person2 = Person(name="Bob", age=22, is_student=True, password="mypassword")
person3 = Person(name="Alice", age=30, password="anothersecret")

print(person1)
print(person2)

print(person1 == person3)  # True, because name and age are the same

person3.age = 31  # This will raise an error because the dataclass is frozen

def main():
  print("Hello, World!")

if __name__ == "__main__":
  main()