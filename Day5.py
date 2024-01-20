# Write a Python program to check if an integer is the power of another integer.
# Input : 16, 2
# Output : True


number_to_check = int(input("Enter the number to check: "))
base_number = int(input("Enter the base number: "))
if number_to_check == 1:
    print( number_to_check,"is a power of",base_number)
else:
    power = 1
    while power < number_to_check:
        power *= base_number
    if power == number_to_check:
        print(number_to_check,"is a power of",base_number)
    else:
        print(number_to_check,"is not a power of",base_number)
