#Quick sort picks a pivot element putting lower values on the left and higher values on the right, then runs recursively on the sub arrays to the left and right

my_array = [11, 9, 12, 7, 3]

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quick_sort(array, low=0, high=None):
    if high is None:
        high = len(array)-1
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index-1)
        quick_sort(array, pivot_index+1, high)

quick_sort(my_array)
print("Sorted array: " + str(my_array))
