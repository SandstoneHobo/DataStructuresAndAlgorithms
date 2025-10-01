# Insertion sort uses part of the array for sorted values and another part for unsorted values
# Get a value from the unsorted portion and put it in the right part of the sorted section

my_array = [7, 12, 9, 11, 3]
n = len(my_array)

for i in range(1, n):
    value = my_array[i]
    for j in range(0, i):
        if value < my_array[j]:
            my_array.pop(i)
            my_array.insert(j, value)
            break

print("Sorted list: " + str(my_array))
