###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

celsius = int(input("Temperature in celsius ")) #inputs temperature in celsius
fahrenheit = celsius*1.8+32 #converts celsius to fahrenheit
kelvin = celsius+273.15 #converts celsius to kelvin
print(f"Temperature in Celsius - {celsius}°C, Temperature in Fahrenheit - {round(fahrenheit)}°F, Temperature in Kelvin - {kelvin}K.") #prints the results



