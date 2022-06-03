import random


def partition_(array, start, end, idx_pivot):
    if not (start <= idx_pivot <= end):
        raise ValueError('Index pivot must be between start and end')

    array[start], array[idx_pivot] = array[idx_pivot], array[start]
    pivot = array[start]
    i = start + 1
    j = start + 1

    while j <= end:
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1

    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1


def quick_sort(array, start=0, end=None):

    if end is None:
        end = len(array) - 1

    if end - start < 1:
        return

    idx_pivot = random.randint(start, end)
    i = partition_(array, start, end, idx_pivot)
    quick_sort(array, start, i - 1)
    quick_sort(array, i + 1, end)


if __name__ == "__main__":
    lst = [4, 51, -1, 0, -3, 4, 1]
    print(quick_sort(lst))
