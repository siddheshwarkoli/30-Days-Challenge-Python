# Write a Python program to check if a given positive integer is a power of four.
# Input : 4
# Output : True


num = int(input("Enter a positive integer: "))
temp=num
if temp <= 0:
    print(num," is not a positive integer.")
else:
    while temp % 4 == 0:
        temp /= 4

    if temp == 1:
        print(num," is a power of four.")
    else:
        print(num," is not a power of four.")
