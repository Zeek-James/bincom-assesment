# Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.

import random

# Generate a random 4-digit number of 0s and 1s
number_str = ""
for i in range(4):
    digit = random.randint(0, 1)
    number_str += str(digit)

# Convert the number from base 2 to base 10
number_base10 = int(number_str, 2)

# Print the result
print(f"The random 4-digit number in base 10 is {number_base10}")