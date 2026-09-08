# write  a program using function to convert celcius to fahrenheit.
# The formula to convert Celsius (°C) to Fahrenheit (°F) is °F = (°C × 9/5) + 32

def f_to_c(f):
  return 5*(f-32)/9


f = int(input("enter temperature in F: "))
print(f_to_c(f))
