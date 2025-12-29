class Car:
  def __init__(self, make, model, year) -> None:
      self.make = make
      self.model = model
      self.year = year

  def display_info(self):
    return f"{self.year} {self.make} {self.model}"
  
  def __str__(self):
    return f"Car(make={self.make}, model={self.model}, year={self.year})"

volvo: Car = Car("Volvo", "XC90", 2020)

print(volvo)

print(volvo.display_info())

def main():
  print("Hello, World!")

if __name__ == "__main__":
  main()