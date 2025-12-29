import time

def perf_time(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"Time taken: {end - start}")
    return result
  return wrapper

@perf_time
def brew_tea(formula=""):
  print("Brewing tea..." + formula)
  time.sleep(1)
  print("Tea is ready!")

@perf_time
def brew_coffee():
  print("Brewing coffee...")
  time.sleep(2)
  print("Coffee is ready!")
  return "Coffee"


brew_tea("Earl Grey")
print(brew_coffee())