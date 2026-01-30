import random
def swap(index1, index2, list: list):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

def bubble_pass(items: list) -> tuple[int, int]:
    comparisons = 0
    swaps = 0
    for i in range(0, len(items) - 1):
        current = items[i]
        next = items[i + 1]
        comparisons += 1
        if current > next:
            swaps += 1
            items[i + 1] = current
            items[i] = next
    return swaps, comparisons

def bubbleSort(items: list):
    swaps = 0
    comparisons = 0
    new_swaps = True
    while new_swaps:
        start_swaps = swaps
        bubble_return = bubble_pass(items) # tuple return of functon
        swaps += bubble_return[0] # first item in tuple
        comparisons += bubble_return[1] # second item in tuple
        end_swaps = swaps
        if end_swaps == start_swaps: # no new swaps
            # if no items are swapped, the list should be ordered
            new_swaps = False
    return items, swaps, comparisons
def swap_index(list: list, item):
    comparisons = 0
    for i in list:
        if item < i:
            return i, comparisons

def pushing_swap(list: list, low_index, high_index):
    comparisons = 0
    swaps = 0
    if low_index > high_index:
        # guarantees proper ordering
        # xor swap algorithm
        low_index = high_index ^ low_index
        high_index = low_index ^ high_index
        low_index = high_index ^ low_index

    for i in range(high_index, low_index , -1):
        current_item = list[i]
        next_index = i - 1
        next_item = list[next_index]
        comparisons += 1
        # print("pushing", list, current_item )
        if current_item < next_item:
            swaps += 1
            swap(i, next_index, list)
        else:
            break
    return  swaps, comparisons
def insertionSort(items : list):
    swaps = 0
    comparisons = 0
    indices = range(0, len(items)) # 0 is checked in the one case
    for i in indices:
        # print(items, i)
        temp = pushing_swap(items, 0, i) # contains tuple
        swaps += temp[0] # accesses first item
        comparisons += temp[1] # second
    # swap(0, len(items) - 1, items)
    # print("final: ", items)
    return items, swaps, comparisons

def find_min(list: list):
    min = list[0]
    min_index = 0
    indices = range(1, len(list)) # excludes 0, the default minimum value is 0
    for i in indices:
        if list[i] < min:
            min = list[i]
            min_index = i
    # print("slice to find min in: ", list)
    # print("min_index = ", min_index, "value = ", min)
    return min_index

def selectionSort(items: list):
    swaps = 0
    comparisons = 0
    indices = range(0, len(items) - 1) # all indices in items, except the last one, which is left automatically
    # the sort selects the lowest value, and puts it at the end of the sorted list, starting at index 0
    # the last item is the least minimum, or the maximum value (or equal to the maximum varue)
    # so it is already sorted
    for i in indices:
        # print("current index: ", i, " current list: ", items)
        next_index = find_min(items[i:len(items)]) # minimum value further in the list than the current index
        comparisons += len( items[i : len(items)] ) - 1 # every two values are compared in order, overlapping
        # however, the first and last index have no overlap, which allows for one less, since the fences
        # do not need to be compared to two values, just one
        next_index += i # next index is relative to i, so to use in the full list
        # the next index has to be normalized to the full list
        # print("current index: ", i, " current list: ", items)
        swaps += 1 # every time a value is swapped the swaps counter must increase
        swap(i, next_index, items)
    return items, swaps, comparisons

y = [9,8,7,6,5,4,3,2,1]
print(bubbleSort(y.copy()))
print(insertionSort(y.copy()))
print(selectionSort(y.copy()))
print()
x = [x for x in range(50)]
random.shuffle(x)
print(bubbleSort(x.copy()))
print(insertionSort(x.copy()))
print(selectionSort(x.copy()))
