# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html

import random
from timeit import default_timer as timer


def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp


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