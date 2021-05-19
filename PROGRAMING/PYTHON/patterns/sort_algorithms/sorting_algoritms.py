#-------------------------MORE ABOUT ALGORITHMS---------------------------------
#https://realpython.com/sorting-algorithms-python/#the-significance-of-time-complexity
#-------------------------------------------------------------------------------

# Without Optimization: Function always runs O(n^2) time
# With Optimization: O(n*n). Worst case occurs when array is reverse sorted., Best case O(n) when sorted
# best: Ω(n)	avg: θ(n^2)	 worst: O(n^2)
def bubble_sort(our_list):
    n = len(our_list)
    for x in range(n-1):
        swaped = False        # For optimisation
        for y in range(n-x-1):
            if our_list[y] > our_list[y+1]:
                our_list[y], our_list[y+1] = our_list[y+1], our_list[y]
                swaped = True # For optimisation
        if not swaped: break  # For optimisation
    return our_list

# Sorts elemets by putting smalles number to the left, then taking different
# element and putting to left side if it is smaller if not leaves in palce and
# check other element. O(n^2) time complexity,
# Time Complexity max: O(n*2) , when reveresed sorted
# Time Complexity min: O(n) , when sorted
# best: Ω(n)	avg: θ(n^2)	 worst: O(n^2)
def insert_sort(our_list):
    n = len(our_list)
    for x in range(1, n):
        val = our_list[x]
        y = x-1
        # print(y,x, val, our_list, 'outer loop')
        while y >= 0 and val < our_list[y]:
            # print(y, val, our_list, 'inner loop: before change')
            our_list[y+1] = our_list[y]
            y -= 1
            # print(y, val, our_list, 'inner loop: after change')
        our_list[y+1] = val
    return our_list

# best: Ω(n^2)	avg: θ(n^2)	worst: O(n^2)
def select_sort(our_list):
    n = len(our_list)
    for x in range(n):
        min_index = x
        for y in range(x+1, n):
            if our_list[y] < our_list[min_index]:
                min_index = y
        our_list[x], our_list[min_index] = our_list[min_index], our_list[x]
    return our_list

## QuickSort with partition
# best: Ω(n log(n))	avg: θ(n log(n))	worst: O(n^2)
def partition(arr, low, high):
    i = (low -1)
    pivot = arr[high]

    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)

## MergeSort
# Best: Ω(n log(n))	avg: θ(n log(n))	worst: O(n log(n))
def merge(array, left_i, right_i, middle):
    left_arr_copy = array[left_i: middle+1]
    right_arr_copy = array[middle+1: right_i+1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_i
    while left_copy_index < len(left_arr_copy) and right_copy_index < len(right_arr_copy):
        if left_arr_copy[left_copy_index] <= right_arr_copy[right_copy_index]:
            array[sorted_index] = left_arr_copy[left_copy_index]
            left_copy_index += 1
        else:
            array[sorted_index] = right_arr_copy[right_copy_index]
            right_copy_index += 1
        sorted_index += 1

    while left_copy_index < len(left_arr_copy):
        array[sorted_index] = left_arr_copy[left_copy_index]
        left_copy_index += 1
        sorted_index += 1
    while right_copy_index < len(right_arr_copy):
        array[sorted_index] = right_arr_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1

def merge_sort(array, left_i, right_i):
    # main function
    if left_i >= right_i:
        return
    middle = (left_i + right_i) // 2
    merge_sort(array, left_i, middle)
    merge_sort(array, middle+1, right_i)
    merge(array, left_i, right_i, middle)

## HeapSort: Needs to implement
# best: Ω(n log(n))	avg: θ(n log(n))	worst: O(n log(n))

## BucketSort: Needs to implement
# best: Ω(n+k)	avg: θ(n+k)	worst: O(n^2)

## RadixSort: Needs to implement
# best: Ω(nk)	avg: θ(nk)	worst: O(nk)

if __name__=='__main__':
    from random import randint
    ll = [randint(1,100) for _ in range(randint(5,11))]
    print(ll)
    ll = insert_sort(ll)
    print(ll)
