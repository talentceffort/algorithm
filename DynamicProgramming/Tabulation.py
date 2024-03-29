def fib_tab(n):
    # 코드를 작성하세요.
    fib_table = [0, 1, 1]

    # if n < 3:
    #     #     return fib_table[n]
    #     # else:
    #     #     while len(fib_table) != n + 1:
    #     #         fib_table.append( fib_table[len(fib_table) - 1] + fib_table[len(fib_table) - 2])
    #     #
    #     # return fib_table[n - 1] + fib_table[n - 2]

    #FeedBack
    # n번째 피보나치 수까지 리스트를 하나씩 채워 나간다
    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])

    # 피보나치 n번째 수를 리턴한다
    return fib_table[n]

# 테스트
print(fib_tab(1))
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))