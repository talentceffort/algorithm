def binary_search(element, some_list):
    # 코드를 작성하세요.
    start = 0
    end = len(some_list) - 1

    while start <= end:

        mid = (start + end) // 2

        if some_list[mid] > element:
            end = mid - 1
        elif some_list[mid] < element:
            start = mid + 1
        else:
            return mid


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))