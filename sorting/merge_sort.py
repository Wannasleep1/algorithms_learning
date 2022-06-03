def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    while left_list_index < left_list_length and right_list_index < right_list_length:
        if left_list[left_list_index] <= right_list[right_list_index]:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
        else:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

    sorted_list += left_list[left_list_index:] + right_list[right_list_index:]
    return sorted_list


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_list = merge_sort(array[:mid])
    right_list = merge_sort(array[mid:])
    return merge(left_list, right_list)


if __name__ == "__main__":
    lst = [4, 51, -1, 0, -3, 4, 1]
    print(merge_sort(lst))
