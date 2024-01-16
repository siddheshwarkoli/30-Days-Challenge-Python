# Write a Python program to check if a number is a perfect square.
# Input : 9
# Output : True


import math
num = int(input("Enter a number: "))
if math.isqrt(num)**2 == num:
    print(num," is a perfect square.")
else:
    print(num," is not a perfect square.")
