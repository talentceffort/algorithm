def min_fee(pages_to_print):
    # 코드를 작성하세요.
    sort = []
    pre = 0
    total = 0

    for i in sorted(pages_to_print):
        sort.append(i)

    for i in range(0, len(sort)):
       temp = sort[i] + pre
       pre = temp
       total += temp
    return total

    # 인풋으로 받은 리스트를 정렬시켜 준다
    #sorted_list = sorted(pages_to_print)

    # 총 벌금을 담을 변수
    #total_fee = 0

    # 정렬된 리스트에서 총 벌금 계산
    #for i in range(len(sorted_list)):
    #   total_fee += sorted_list[i] * (len(sorted_list) - i)

    #return total_fee

    # 1
    # 1 + 4
    # 1 + 4 + 6
    # 1 + 4 + 6 + 11


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
