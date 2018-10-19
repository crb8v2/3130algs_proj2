
# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html

import random
from timeit import default_timer as timer


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

list_thousand_sorted = list(range(1, 1000))
list_thousand_random = random.sample(range(1, 1000), 999)

list_tenthous_sorted = list(range(1, 10000))
list_tenthous_random = random.sample(range(1, 1000), 9999)


start = timer()
# insertionSort(list_hundred_sorted)
# insertionSort(list_hundred_random)
# insertionSort(list_thousand_random)
# insertionSort(list_thousand_random)
# insertionSort(list_tenthous_random)
# insertionSort(list_tenthous_random)
end = timer()

print ("    time:",(end - start))

