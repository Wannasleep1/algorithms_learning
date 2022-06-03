def binary_search(sorted_array, key_value):
    low = 0
    high = len(sorted_array) - 1
    while low <= high:
        mid = (low + high) // 2
        if key_value < sorted_array[mid]:
            high = mid - 1
        elif key_value > sorted_array[mid]:
            low = mid + 1
        else:
            return mid
    return None


if __name__ == "__main__":
    array = [1, 3, 4, 6, 8, 13, 45]
    print(binary_search(array, 0))
    print(binary_search(array, 3))
    print(binary_search(array, 45))
