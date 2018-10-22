
# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html

from random import *
from timeit import default_timer as timer
import random


def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

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
# insertionSort()
# end = timer()
#
# print ("\n    time: \n",(end - start))

