# Write a Python program to check if a given positive integer is a power of three.
# Input : 9
# Output : True


n = int(input("Enter a positive integer: "))
temp=n
if temp <= 0:
    print(n," is not a positive integer.")
else:
    while temp % 3 == 0:
        temp /= 3
    if temp == 1:
        print(n," is a power of three.")
    else:
        print(n," is not a power of three.")
