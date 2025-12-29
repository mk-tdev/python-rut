def tea_order(customer_name, tea_type, *args, **kwargs):
  print(f"{customer_name} ordered {tea_type}")

  if args:
    print("With:", args)
    for arg in args:
      print(arg)

  if kwargs:
    print("With:", kwargs)
    for key, value in kwargs.items():
      print(f"{key}: {value}")


tea_order("John", "Earl Grey")
tea_order("John", "Earl Grey", "Milk", sugar="Sugar Minus")

johnExtras = ["Milk", "Sugar"]
tea_order("John", "Earl Grey", *johnExtras)

maryExtras = {"milk": "Milk", "sugar": "Sugar Plus"}
tea_order("Mary", "Earl Grey", **maryExtras)

