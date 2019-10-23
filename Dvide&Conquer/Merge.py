def merge(list1, list2):
    temp = [];
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            temp.append(list2[j])
            j += 1
        else:
            temp.append(list1[i])
            i += 1

    if len(list1) == i:
        for num in range (j, len(list2)):
            temp.append(list2[num])
    elif len(list2) == j:
        for num in range(i, len(list1)):
            temp.append(list1[num])

    return temp

# 코드를 작성하세요.

# 테스트
print(merge([1], []))
print(merge([], [1]))
print(merge([2], [1]))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))