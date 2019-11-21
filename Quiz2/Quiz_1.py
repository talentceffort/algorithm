def sublist_max(profits, start, end):
    # O(nlgn) 으로 풀 것. Dvide and Conquer
    if start == end:
        return profits[start]

    pivot = (start + end) // 2

    # 상황별로 최대 수익을 구한다
    max_left = sublist_max(profits, start, pivot)
    max_right = sublist_max(profits, pivot + 1, end)
    max_cross = max_crossing_sum(profits, start, end)

    # 위 세 경우 중 가장 큰 결괏값을 리턴한다
    return max(max_left, max_right, max_cross)

def max_crossing_sum(profit, start, end):
    mid = (start + end) // 2

    left_sum = 0  # 왼쪽 누적 수익
    left_max = profit[mid]

    for i in range(mid, start - 1, -1):
        left_sum += profit[i]
        left_max = max(left_max, left_sum)

    right_sum = 0  # 오른쪽 누적 수익
    right_max = profit[mid + 1]  # 오른쪽 최고 수익; 오른쪽 반 중 가장 왼쪽 값으로 초기화

    for i in range(mid + 1, end + 1):
        right_sum += profit[i]
        right_max = max(right_max, right_sum)

    return left_max + right_max

# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))