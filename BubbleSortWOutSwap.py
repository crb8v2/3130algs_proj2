
import random
from timeit import default_timer as timer


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