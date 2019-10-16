def trapping_rain(buildings):
    # 코드를 작성하세요
    pivot = buildings[0]
    total = 0;

    for num in range (len(buildings) - 1):
        count = 0
        if pivot > buildings[num + 1]:
            for i in range(num, len(buildings) - 1):
                if pivot <= buildings[i + 1]:
                    count += 1
            if count > 0:
                total += pivot - buildings[num + 1]
            else:
                pivot = buildings[num + 1]
        else:
            pivot = buildings[num + 1]

    return total

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trapping_rain([2, 1, 2]))
print(trapping_rain([3, 2, 1, 4]))
print(trapping_rain([3, 3, 3, 3]))
# 0 1 1 2 1

# 처음에 0 이면 패스. 자기보다 작은 수면 다음수로 넘어감.
# 기준인 수에서 자기보다 큰 수가 나올 때 까지 기준 수 - 다음 수 반복.
# 자기와 같거나 높은 수 사이에는 작은 수가 와야함 ex) 2 1 4 이러면 1칸이 채워짐.
# 1 0 4 던 4 0 1 이던 무조건 1칸.

#자기 다음 수가 자기 보다 큰가 작은가? 작으면 넘어감. 크면 계산.

#Solution
# 1. 현재 인덱스의 왼쪽에서 가장 높은 건물의 높이를 구한다
# 2. 현재 인덱스의 오른쪽에서 가장 높은 건물의 높이를 구한다
# 3. 그 중 더 낮은 건물의 높이를 구한다
# 3. 그 높이에서 현재 인덱스에 있는 건물의 높이를 뺀다

# def trapping_rain(buildings):
#     # 총 담기는 빗물의 양을 변수에 저장
#     total_height = 0
#
#     # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
#     # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
#     for i in range(1, len(buildings) - 1):
#         # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
#         max_left = max(buildings[:i])
#         max_right = max(buildings[i:])
#
#         # 현재 인덱스에 빗물이 담길 수 있는 높이
#         upper_bound = min(max_left, max_right)
#
#         # 현재 인덱스에 담기는 빗물의 양을 계산
#         # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
#         total_height += max(0, upper_bound - buildings[i])
#
#     return total_height