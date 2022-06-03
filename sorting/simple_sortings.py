# Selection sort
def selection_sort(array):
    length = len(array)
    for i in range(length):
        lowest_value_index = i
        for j in range(i + 1, length):
            if array[j] < array[lowest_value_index]:
                lowest_value_index = j
        array[i], array[lowest_value_index] = array[lowest_value_index], array[i]


# Insertion sort
def insertion_sort(array):
    length = len(array)
    for i in range(1, length):
        item_to_insert = array[i]
        j = i - 1
        while j >= 0 and array[j] > item_to_insert:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = item_to_insert


# Bubble sort
def bubble_sort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True


if __name__ == "__main__":
    lst_1 = [4, 51, -1, 0, -3, 4, 1]
    selection_sort(lst_1)
    lst_2 = [4, 51, -1, 0, -3, 4, 1]
    insertion_sort(lst_2)
    lst_3 = [4, 51, -1, 0, -3, 4, 1]
    bubble_sort(lst_3)
    print(lst_1)
    print(lst_2)
    print(lst_3)
