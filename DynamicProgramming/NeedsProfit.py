def max_profit_memo(price_list, count, cache):
    # Base Case: 0개 혹은 1개면 부분 문제로 나눌 필요가 없기 때문에 가격을 바로 리턴한다
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    # 이미 계산한 값이면 cache에 저장된 값을 리턴한다
    if count in cache:
        return cache[count]

    # profit은 count개를 팔아서 가능한 최대 수익을 저장하는 변수
    # 팔려고 하는 총개수에 대한 가격이 price_list에 없으면 일단 0으로 설정
    # 팔려고 하는 총개수에 대한 가격이 price_list에 있으면 일단 그 가격으로 설정
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 profit에 저장
    for i in range(1, (count // 2) + 1):
        #profit = max(profit, max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache))
        temp = max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache)
        if temp > profit:
            profit = temp

    # 계산된 최대 수익을 cache에 저장
    cache[count] = profit

    return profit
    # n개를 팔아서 가능한 최대 수익을 어떻게 알 수 있을까 ? 주
    # count 가 주어졌을 때 탐색할 수 있는 모든 경우의 수를 구할 수 있냐 없냐갸 문제의 핵심...
    # (count // 2) + 1 => count 가 탐색할 총 수.



    # n 개가 짝수던 홀수던 n / 2 한 몫의 + 1 을 해
    # n개 + 0개
    # n-1개 + 1개
    # n-2개 + 2개
    # ...
    # n // 2개 + n // 2개

    # 6 + 0
    # 5 + 1
    # 4 + 2
    # 3 + 3

    # 5 + 0
    # 4 + 1
    # 3 + 2

    # 10 + 0
    # 9 + 1
    # 8 + 2
    # 7 + 3
    # 6 + 4
    # 5 + 5

    # 9 + 0
    # 8 + 1
    # 7 + 2
    # 6 + 3
    # 5 + 4

    # 8 + 0
    # 7 + 1
    # 6 + 2
    # 5 + 3
    # 4 + 4

    #[5 0] [4 1] [3 2]

def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
