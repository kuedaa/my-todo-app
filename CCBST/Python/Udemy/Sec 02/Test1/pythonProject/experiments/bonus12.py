from experiments.convert import convert
from experiments.parse import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result} meters")

if result < 1 :
    print("Kid is too small.")
else:
    print ("Kid can use the slide")