# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    # 여기 코드를 쓰세요
    x = 0
    y = 0
    min_distance = distance(coordinates[0], coordinates[1])
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if coordinates[i] != coordinates[j]:
               num = distance(coordinates[i], coordinates[j])
               if num < min_distance:
                   min_distance = num
                   x = coordinates[i]
                   y = coordinates[j]

    return [x, y]


# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))

#Solution

# def closest_pair(coordinates):
#     # 현재까지 본 가장 가까운 두 매장
#     pair = [coordinates[0], coordinates[1]]
#
#     for i in range(len(coordinates) - 1):
#         for j in range(i + 1, len(coordinates)):
#             store1, store2 = coordinates[i], coordinates[j]
#
#             # 더 가까운 두 매장을 찾으면 pair 업데이트
#             if distance(pair[0], pair[1]) > distance(store1, store2):
#                 pair = [store1, store2]
#
#     return pair
#
