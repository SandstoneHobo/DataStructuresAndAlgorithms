"""
Arrays are a data structure that store multiple elements

What is the difference between a list and array? A list is a dynamically sized array
"""

#arrays are indexed so each element has an index number that says where the element is located in the array
my_array=[7, 12, 9, 4, 11]
print(my_array[0])

#algorithm to find the lowest value in the array
    #create minVal to track the lowest value
    #visit each element in the array
    #if the current element is lower than minVal set minVal to that
    #print the lowest value
minVal = my_array[0]
for value in my_array:
    if value < minVal:
        minVal = value

print(minVal)
