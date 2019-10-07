# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    # 코드를 작성하세요.

    length = len(str(n))
    n = str(n)

    if length == 1:
        return int(n[0])
    else:
        return int(n[length - 1]) + sum_digits(n[:length - 1])

#Solution
#def sum_digits(n):
    # base case
    #if n < 10:
    #    return n

    # recursive case
    #return n % 10 + sum_digits(n // 10)


# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))