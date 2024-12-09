# def heapify(arr, n, i):
#     largest = i
#     left = 2 * i + 1
#     right = 2 * i + 2
#
#     if left < n and arr[left] > arr[largest]:
#         largest = left
#
#     if right < n and arr[right] > arr[largest]:
#         largest = right
#
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)
#
# def build_heap(arr):
#     n = len(arr)
#
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)
#
# # Пример использования
# arr = [12, 11, 13, 5, 6, 7]
# build_heap(arr)
# print(arr)
#
# import heapq
#
# def array_to_heap_heapq(arr):
#   heapq.heapify(arr)
#   return arr
#
# my_array = [12, 11, 13, 5, 6, 7]
# heap = array_to_heap_heapq(my_array)
# print(heap)
#
#
# def add_to_heap(heap, item):
#     heap.append(item)
#     i = len(heap) - 1
#     while i > 0:
#         parent = (i - 1) // 2
#         if heap[i] < heap[parent]:
#             heap[i], heap[parent] = heap[parent], heap[i]
#             i = parent
#         else:
#             break
#     return heap
#
# my_heap = [3, 1, 4, 1, 5, 9, 2, 6]
# new_item = 0
# my_heap = add_to_heap(my_heap, new_item)
# print(my_heap)



# import heapq
#
# def remove_max(heap):
#
#     if not heap:
#         return None
#
#     max_val = -heapq.heappop(heap)
#     return max_val
#
# my_heap = [-3, -1, -4, -1, -5, -9, -2, -6]
# heapq.heapify(my_heap)
#
#
# max_element = remove_max(my_heap)
# print(max_element)
# print(my_heap)


import heapq

def heapsort(arr):
    n = len(arr)
    heapq.heapify(arr)
    sorted_arr = []
    for _ in range(n):
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr

my_array = [10, 5, 3, 15, 20, 12, 8]
sorted_array = heapsort(my_array)
print(sorted_array)