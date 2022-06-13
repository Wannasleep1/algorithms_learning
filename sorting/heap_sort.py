from heapq import heappop, heappush, heapify


def heap_sort(lst):
    heap = []
    for ele in lst:
        heappush(heap, ele)

    sort = []

    while heap:
        sort.append(heappop(heap))

    return sort


if __name__ == "__main__":
    some_lst = [4, 51, -1, 0, -3, 4, 1]
    heapify(some_lst)
    print(heap_sort(some_lst))
