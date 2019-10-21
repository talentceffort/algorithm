# soultion
def consecutive_sum(start, end):
    # base case
    print(start, end)

    if end == start:
        return start

    # 부분 문제를 반으로 나눠주기 위해서 문제의 정중앙을 정의한다 (Divide)
    mid = (start + end) // 2

    # 각 부분 문제를 재귀적으로 풀고(Conquer), 부분 문제의 답을 서로 더한다(Combine).
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)

# consecutive_sum(1, 10)
# consecutive_sum(1, 5) + consecutive_sum(6, 10) => 15 + consecutive_sum(6, 8) + consecutive_sum(9, 10) => ...
# consecutive_sum(1, 3) + consecutive_sum(4, 5) => 6 +  consecutive_sum(4, 4) + consecutive_sum(5, 5) => 6 + 4 + 5 = 15
# consecutive_sum(1, 2) + consecutive_sum(3, 3) => 3 + 3 = 6
# consecutive_sum(1, 1) + consecutive_sum(2, 2) => 1 + 2 = 3




# 테스트
print(consecutive_sum(1, 10))
#print(consecutive_sum(1, 100))
#print(consecutive_sum(1, 253))
#print(consecutive_sum(1, 388))

#soultion
def consecutive_sum(start, end):
    # base case
    if end == start:
        return start

    # 부분 문제를 반으로 나눠주기 위해서 문제의 정중앙을 정의한다 (Divide)
    mid = (start + end) // 2

    # 각 부분 문제를 재귀적으로 풀고(Conquer), 부분 문제의 답을 서로 더한다(Combine).
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)