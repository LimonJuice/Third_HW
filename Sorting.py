import random

a = random.sample(range(100), 10)  # generating a random list


# MergeSort


def mergeSort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i = i + 1
            else:
                lst[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            lst[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            lst[k] = right[j]
            j = j + 1
            k = k + 1

    return (lst)


# QuickSort

def quickSort(lst):
    if len(lst) > 1:
        pivot = lst[0]
        left, right = [], []
        for i in range(1, len(lst)):
            if (lst[i] < pivot):
                left.append(lst[i])

            else:
                right.append(lst[i])
        return quickSort(left) + [pivot] + quickSort(right)

    else:
        return list
