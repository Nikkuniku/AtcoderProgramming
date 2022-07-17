a, b, c, d, e, f = map(int, input().split())

noudo = -1
water = 0
sugar = 0
for k in range(31):
    for m in range(16):
        p = a*k + b*m
        if 100*p > f:
            continue
        v = min(p*e, f - 100*p)
        goods = [c, d]
        dp = [[False]*(v+1) for _ in range(3)]
        dp[0][0] = True

        for i in range(2):
            for j in range(v+1):
                dp[i+1][j] |= dp[i][j]
                if j-goods[i] >= 0:
                    dp[i+1][j] |= dp[i+1][j-goods[i]]
        tmp = 0
        for i in range(v+1):
            if dp[2][i]:
                tmp = i
        if (100*p + tmp) <= 0:
            continue

        if tmp/(100*p + tmp) >= noudo:
            noudo = tmp/(100*p + tmp)
            water = 100*p
            sugar = tmp

print(water+sugar, sugar)
