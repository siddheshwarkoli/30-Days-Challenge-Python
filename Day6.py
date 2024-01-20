# Write a Python program to check if a number is a power of a given base


number = int(input("Enter a number: "))
base = int(input("Enter a base: "))

if number <= 0 or base <= 1:
    print("Enter positive integers greater than 1 for both number and base.")
else:
    exponent = 0
    while base ** exponent < number:
        exponent += 1

    if base ** exponent == number:
        print(number," is a power of",base)
    else:
        print(number,"is not a power of",base)
