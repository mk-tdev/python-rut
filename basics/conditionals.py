num = 30

print("Mk" * 4)

fav_color = "blue"
fav_movie = "Inception"
fav_food = "pizza"
fav_hobby = "reading"


if fav_color == "bluesky":
    print("My favorite color is blue.")
    if fav_movie == "Inception":
        print("My favorite movie is Inception.")
        if fav_food == "pizza":
            print("My favorite food is pizza.")
            if fav_hobby == "reading":
                print("My favorite hobby is reading.")
else:
    print("In else statement")
print("End of the program.")

unit = input("Enter the unit of measurement (cm, m, km): ")

if unit == "cm":
    value = float(input("Enter the value in centimeters: "))
    converted_value = value / 100
    print(f"{value} cm is equal to {converted_value} m")
elif unit == "m":
    value = float(input("Enter the value in meters: "))
    converted_value = value * 100
    print(f"{value} m is equal to {converted_value} cm")
elif unit == "km":
    value = float(input("Enter the value in kilometers: "))
    converted_value = value * 100000
    print(f"{value} km is equal to {converted_value} cm")
else:
    print("Invalid unit of measurement. Please enter cm, m, or km.")
# The code above is a simple unit converter that converts between centimeters, meters, and kilometers.
# It prompts the user to enter a unit of measurement and a value, then performs the conversion based on the unit provided.