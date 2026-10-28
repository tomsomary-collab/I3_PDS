def celsius_to_fahrenheit(c,round_to=1):
    far = c * 9/5 + 32
    return far
print(celsius_to_fahrenheit(2),"°F")
def fahrenheit_to_celsius(f,rount_to=1):
    cel = (f-32) * 5/9
    return cel
print(fahrenheit_to_celsius(68),"°C")

print("\n  °C  |   °F")
print("------+-------")
for c in range(0, 101, 20):
    print(f"{c:5} | {celsius_to_fahrenheit(c):6}")

print("98.6 °F =", fahrenheit_to_celsius(98.6), "°C")
print("Round trip 37 °C:", fahrenheit_to_celsius(celsius_to_fahrenheit(37)))
