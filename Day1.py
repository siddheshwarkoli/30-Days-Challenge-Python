# 1. Write a Python program to check if a given positive integer is a power of two.
# Input : 4
# Output : True


num = int(input("Enter a positive integer: "))
if num > 0 and (num & (num - 1)) == 0:
    print(num," is a power of 2.")
else:
    print(num, " is not a power of 2.")




# -------------------------------Simple Explanation :---------------------------------------------------


#     In Above code we have to find the given number is power of two or not for that we used and operator
#     The "&" operator compares the corresponding bits of A and B
#     If both bits are 1, the result bit will be 1 otherwise it will be 0.
#     In above case we "&" compare with given number with previous number
#     if the output shows 0 then it is power of two if not the value is false