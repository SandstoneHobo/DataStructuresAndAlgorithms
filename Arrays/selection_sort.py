"""
Selection Sort finds the lowest value in the array and moves it to the front, then repeats until the array is sorted
"""

my_array = [7, 12, 9, 11, 3]
n = len(my_array)

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

print("Selection sort with shifting: " + str(my_array))

#Selection sort can be improved by swapping values instead of removing and insterting values, which saves time complexity for not shifting the rest of the values
my_array = [7, 12, 9, 11, 3]

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print("Selection sort without shifting: " + str(my_array))
