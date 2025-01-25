temprature = int(input("Enter the temprature to convert: "))
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9*temprature) - 32
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5*temprature) + 32
unit = input("Is this temprature in Celcius or Fahrenheit? (C/F): ")
def convert_to_celsius(fahrenheit):
     temp_in_C = FAHRENHEIT_TO_CELSIUS_FACTOR 
     print(f"{temprature}°F is {temp_in_C}°C")
def convert_to_fahrenheit(celsius):
    temp_in_F = CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f"{temprature}°C is {temp_in_F}°F ")

if unit.lower() == "c" and type(temprature) is int:
     convert_to_fahrenheit(temprature)
elif unit.lower() == "f" and type(temprature) is int:
     convert_to_celsius(temprature)
else: 
     print("invalid temperature. Please enter a numeric value.")