"""
Bubble sort checks two values and swaps them if the larger one is on the left, then goes to the next value until the biggest value ends up at the end
This repeats until the smallest value ends up on the left
"""

my_array = [7, 12, 9, 11, 3]

n = len(my_array)
for i in range(n - 1):
    swapped = False
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            swapped = True
    if not swapped:
        break

print(my_array)
