# 거듭 제곱 빠르게 계산하

def power(x, y):
    # 코드를 작성하세요.
    # x ^ y

    # if y == 0:
    #     return 1
    # else:
    #     return power(x, y - 1) * x

    if y == 0:
     return 1

    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)
    else:
         return x * power(x, y // 2) * power(x, y // 2)

    # print(power(3, 5))
    # print(power(5, 6))
    # print(power(7, 9))

# Feedback
# 문제를 최대한 똑같은 크기의 문제 두 개로 나눠준다 (짝수, 홀수 경우 따로)
# O(lg y) 로 풀기. log 는 문제를 분할한다.
# def power(x, y):
#     if y == 0:
#         return 1
#
#     # 문제를 최대한 똑같은 크기의 문제 두 개로 나눠준다 (짝수, 홀수 경우 따로)
#     if y % 2 == 0:
#         return power(x, y // 2) * power(x, y // 2)
#     else:
#         return x * power(x, y // 2) * power(x, y // 2)


# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))