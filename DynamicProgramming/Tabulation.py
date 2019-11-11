def fib_tab(n):
    # 코드를 작성하세요.
    fib_table = [0, 1, 1]

    if n < 3:
        return fib_table[n]
    else:
        while len(fib_table) != n + 1:
            fib_table.append( fib_table[len(fib_table) - 1] + fib_table[len(fib_table) - 2])

    return fib_table[n - 1] + fib_table[n - 2]

# 테스트
print(fib_tab(1))
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))