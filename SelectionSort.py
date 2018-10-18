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


list = list(range(1, 100))
list2 = random.sample(range(1, 10000), 9999)
# list3 = list(range(1, 1000))
#
# aa = 0
# while aa < len(list3):
#     aa += 1
#     if (list3[aa] % 10) == 0:
#         list3[aa] = 0

start = timer()
selectionSort(list)
end = timer()
print ("    time:",(end - start))

start2 = timer()
selectionSort(list2)
end2 = timer()
print ("    time:",(end2 - start2))

print(list)
print(list2)
# print(list3)

# how to graph outputs of each statement
# how to make an array of 10,000 chars with % 10 positions swapped