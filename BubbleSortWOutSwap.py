
# https://www.geeksforgeeks.org/bubble-sort/

from random import *
from timeit import default_timer as timer
import random


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


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
# bubbleSort()
# end = timer()
# print ("\n    time: \n",(end - start))
