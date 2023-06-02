from swap import swap_numbers
from extras.desc import print_descending

a = int(input("Please enter the first number (0-3): "))
b = int(input("Please enter the second number (0-3): "))

swapped_a, swapped_b = swap_numbers(a, b)
print(f"The two swapped numbers are: {swapped_a} and {swapped_b}")

n = int(input("Please enter a number to print in natural descending order: "))
print("Natural descending order:", end=' ')
print_descending(n)
