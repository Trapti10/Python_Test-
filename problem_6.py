# Write a program that converts and prints user given measurement in inches into
# 1. foot(12 inches)
# 2. yard(36 inches)
# 3. centimetres(2.54 inches)
# 4. meter(39.37 inches)

inches = float(input("Enter the measurement in inches: "))

feet = inches/12
yards = inches/36 
centimeters = inches * 2.54
meters = inches * 39.37

print(f"{inches} inches is equal to:")
print(f"{feet:.2f} feet")
print(f"{yards:.2f} yards")
print(f"{centimeters:.2f} cm")
print(f"{meters:.2f} meters")
