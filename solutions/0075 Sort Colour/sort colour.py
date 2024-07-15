import random


def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]

    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if right < left:
            break
        arr[left], arr[right] = arr[right], arr[left]

    # when the loop terminates the rest of the array is partitioned
    arr[low], arr[right] = arr[right], arr[low]
    return right


def quicksort(arr, low, high):
    if low > high:
        return

    pivot_index = partition(arr, low, high)
    quicksort(arr, low, pivot_index - 1)
    quicksort(arr, pivot_index + 1, high)


def sort_colours(nums):
    quicksort(nums, 0, len(nums) - 1)
    return nums
