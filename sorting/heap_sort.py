def heapify(array, heap_size, root_index):
    largest = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index + 2
    if left_child < heap_size and array[right_child] > array[largest]:
        largest = left_child
    if right_child < heap_size and array[right_child] > array[largest]:
        largest = right_child
    if largest != root_index:
        array[root_index], array[largest] = array[largest], array[root_index]
        heapify(array, heap_size, largest)


def heap_sort(array):
    length = len(array)
    for i in range(length, -1, -1):
        heapify(array, length, i)
    for i in range(length-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, length, 0)


if __name__ == "__main__":
    lst = [4, 51, -1, 0, -3, 4, 1]
    heap_sort(lst)
    print(lst)
