from random import randint
from typing import List
from time import monotonic
def pseudo_random_gen(num_items: int):
    return [randint(0,10) for x in range(num_items)]

def insertion_sort(xs: List[int]):
    for i in range(1, len(xs)):

        key = xs[i]

        j = i-1
        while j >= 0 and key < xs[j]:
            xs[j+1] = xs[j]
            j -= 1
        xs[j+1] = key
def quick_sort(xs: List[int]):
    length = len(xs)
    if length <= 1:
        return xs
    else:
        pivot = xs.pop()
    items_greater = []
    items_lower = []
    for item in xs:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

xs = pseudo_random_gen(10)
print(xs)
# start = monotonic()
# insertion_sort(xs)
# end = monotonic()
# print(xs)
# print("time elapsed %f", end-start)
print(quick_sort(xs))

