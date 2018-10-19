#http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html

import random
from timeit import default_timer as timer

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





