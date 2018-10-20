
#http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html

from random import *
from timeit import default_timer as timer
import random

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)


# list_hundred_sorted = list(range(1, 100))
# list_hundred_random = random.sample(range(1, 100), 99)
# list_hundred_semiSort = list(range(1,100))
#
# # randomize every 10th pos of array
# for i in list_hundred_semiSort:
#     if i % 10 != 0 and i != 0:
#         continue
#     list_hundred_semiSort[i] = randint(1,100)
#
#
# list_thousand_sorted = list(range(1, 1000))
# list_thousand_random = random.sample(range(1, 1000), 999)
# list_thousand_semiSort = list(range(1,1000))
#
# # randomize every 10th pos of array
# for i in list_thousand_semiSort:
#     if i % 10 != 0 and i != 0:
#         continue
#     list_thousand_semiSort[i] = randint(1,1000)
#
#
# list_tenthous_sorted = list(range(1, 10000))
# list_tenthous_random = random.sample(range(1, 10000), 9999)
# list_tenthous_semiSort = list(range(1,10000))
#
# # randomize every 10th pos of array
# for i in list_tenthous_semiSort:
#     if i % 10 != 0 and i != 0:
#         continue
#     list_tenthous_semiSort[i] = randint(1,10000)
# #
# print(list_tenthous_semiSort)
#
# start = timer()
# mergeSort()
# end = timer()
#
# print ("\n    time: \n",(end - start))





