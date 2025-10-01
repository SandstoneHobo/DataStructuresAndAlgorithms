#Counting sort is an algorithm that sorts an array by counting the number of times a value occurs 
#counting sort only works on an array of non negative integers

my_array = [2, 3, 0, 2, 3, 2]
maxVal = my_array[0]

for value in my_array:
    if value > maxVal:
        maxVal = value

count_array = [0] * (maxVal+1)

while len(my_array) != 0:
    value = my_array.pop(0)
    count_array[value] += 1

for i in range(len(count_array)):
    for j in range(count_array[i]):
        my_array.append(i)
print("Sorted array: " + str(my_array))
