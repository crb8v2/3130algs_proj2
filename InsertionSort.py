
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

list = list(range(1, 100))
list2 = random.sample(range(1, 100), 99)

start = timer()
end = timer()
print ("    time:",(end - start))

print(list)
print(list2)