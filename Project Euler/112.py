def Increase_Number(N):
    L = len(str(N))
    dp = [[[0] * 10 for _ in range(2)] for _ in range(L + 1)]
    # 初期値
    for x in range(1, int(str(N)[0]) + 1):
        dp[1][x < int(str(N)[0])][x] += 1
    for i in range(1, L):
        p = int(str(N)[i])
        for smaller in range(2):
            lim = 10 if smaller == 1 else p + 1
            for j in range(10):
                for x in range(lim):
                    if j <= x:
                        dp[i + 1][smaller | (x < p)][x] += dp[i][smaller][j]
    return sum([dp[L][0][x] + dp[L][1][x] for x in range(10)])


def Decrease_Number(N):
    L = len(str(N))
    dp = [[[0] * 10 for _ in range(2)] for _ in range(L + 1)]
    # 初期値
    for x in range(1, int(str(N)[0]) + 1):
        dp[1][x < int(str(N)[0])][x] += 1
    for i in range(1, L):
        p = int(str(N)[i])
        for smaller in range(2):
            lim = 10 if smaller == 1 else p + 1
            for j in range(10):
                for x in range(lim):
                    if x <= j:
                        dp[i + 1][smaller | (x < p)][x] += dp[i][smaller][j]
    return sum([dp[L][0][x] + dp[L][1][x] for x in range(10)])


def Horizontal_Numberdigit(N):
    L = len(str(N))
    l = 0
    r = 10
    while r - l > 1:
        mid = (l + r) // 2
        temp = 0
        for _ in range(L):
            temp *= 10
            temp += mid
        if temp <= N:
            l = mid
        else:
            r = mid
    return l


def Bouncy_Numbers(N):
    L = len(str(N))
    res = N
    for digit in range(1, L + 1):
        if digit == 1:
            res -= 9
        elif digit < L:
            D = pow(10, digit) - 1
            res -= Increase_Number(D)
            res -= Decrease_Number(D)
            res += Horizontal_Numberdigit(D)
        else:
            res -= Increase_Number(N)
            res -= Decrease_Number(N)
            res += Horizontal_Numberdigit(N)
    return res


def check_count(N):
    res = 0
    for i in range(10, N + 1):
        p = str(i)
        # 増加数かチェック
        isZouka = True
        for j in range(1, len(p)):
            if not int(p[j - 1]) <= int(p[j]):
                isZouka = False
                break
        isGensyo = True
        for j in range(1, len(p)):
            if not int(p[j - 1]) >= int(p[j]):
                isGensyo = False
                break
        if isZouka or isGensyo:
            continue
        res += 1
    return res


M = 99
L = 5000000
for k in range(1, L):
    cnt = Bouncy_Numbers(k)
    if cnt * 100 >= M * k:
        print(k, cnt, cnt / k)
        break
