
# https://www.geeksforgeeks.org/python-program-for-quicksort/

from random import *
from timeit import default_timer as timer
import random


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


list_hundred_sorted = list(range(1, 100))
list_hundred_random = random.sample(range(1, 100), 99)
list_hundred_semiSort = list(range(1,100))

# randomize every 10th pos of array
for i in list_hundred_semiSort:
    if i % 10 != 0 and i != 0:
        continue
    list_hundred_semiSort[i] = randint(1,100)


list_thousand_sorted = list(range(1, 1000))
list_thousand_random = random.sample(range(1, 1000), 999)
list_thousand_semiSort = list(range(1,1000))

# randomize every 10th pos of array
for i in list_thousand_semiSort:
    if i % 10 != 0 and i != 0:
        continue
    list_thousand_semiSort[i] = randint(1,1000)


list_tenthous_sorted = list(range(1, 10000))
list_tenthous_random = random.sample(range(1, 10000), 9999)
list_tenthous_semiSort = list(range(1,10000))

# randomize every 10th pos of array
for i in list_tenthous_semiSort:
    if i % 10 != 0 and i != 0:
        continue
    list_tenthous_semiSort[i] = randint(1,10000)


# start = timer()
# quickSort()
# end = timer()
# print ("\n    time: \n",(end - start))
