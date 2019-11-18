def select_stops(water_stops, capacity):
    # 약수터 최대한 적게 들릴것
    # 마지막 산 정상 약수터에 들려야함.
    pivot = 0
    max = water_stops[0]
    result = []
    N = capacity
    for i in range(0, len(water_stops) - 1):
        if capacity >= water_stops[i]:
            pivot += 1
            if max <= water_stops[i] and water_stops[i + 1] > capacity:
                max = water_stops[i]
                capacity = N
                capacity += water_stops[i]
                result.append(water_stops[i])

    result.append(water_stops[len(water_stops) - 1])
    return result

# Feedback
# 약수터 위치 리스트
# stop_list = []
#
# 마지막 들른 약수터 위치
# prev_stop = 0
# for i in range(len(water_stops)):
#         # i 지점까지 갈 수 없으면, i - 1 지점 약수터를 들른다
#         if water_stops[i] - prev_stop > capacity:
#             stop_list.append(water_stops[i - 1])
#             prev_stop = water_stops[i - 1]
#
#     # 마지막 약수터는 무조건 간다
#     stop_list.append(water_stops[-1])
#
#     return stop_list


# 약수터 위치: [1km, 4km, 5km, 7km, 11km, 12km, 13km, 16km, 18km, 20km, 22km, 24km, 26km]
# 물통 용량: 4L
# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

#list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
#print(select_stops(list2, 6))