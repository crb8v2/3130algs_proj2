
# https://www.geeksforgeeks.org/python-program-for-quicksort/

from random import *
from timeit import default_timer as timer
import random


def partition(lst, start, end, pivot):
    lst[pivot], lst[end] = lst[end], lst[pivot]
    store_index = start
    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[i], lst[store_index] = lst[store_index], lst[i]
            store_index += 1
    lst[store_index], lst[end] = lst[end], lst[store_index]
    return store_index


def quick_sort(lst, start, end):
    if start >= end:
        return lst
    pivot = randrange(start, end + 1)
    new_pivot = partition(lst, start, end, pivot)
    quick_sort(lst, start, new_pivot - 1)
    quick_sort(lst, new_pivot + 1, end)


def sort(lst):
    quick_sort(lst, 0, len(lst) - 1)
    return lst

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
# sort()
# end = timer()
# print ("\n    time: \n",(end - start))
