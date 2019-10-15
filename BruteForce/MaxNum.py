def max_product(left_cards, right_cards):

    max_num = 0

    for i in left_cards:
        for j in right_cards:
            if i * j > max_num:
                max_num = i * j

    return max_num

# 코드를 작성하세요.

# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))

#가장 큰 곱 구하기.