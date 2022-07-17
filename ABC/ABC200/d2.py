from collections import deque, defaultdict, Counter
n = int(input())
a = list(map(int, input().split()))
amod = [a[i] % 200 for i in range(n)]
C = Counter(amod)
Existflg = False


def check(L):
    tmp = 0
    P = L[0]
    ARR = L[0:]
    for i in range(P):
        tmp += a[ARR[i]-1]
    return tmp % 200


for k, v in C.items():
    if v > 1:
        Existflg = True
        break

if Existflg:
    b = []
    c = []
    for i in range(n):
        if not b:
            if a[i] % 200 == k:
                b.append(i+1)
        else:
            if a[i] % 200 == k:
                c.append(i+1)
                break

    print('YES')
    print(len(b), *b)
    print(len(c), *c)
else:
    pos = defaultdict(int)
    for k, v in enumerate(a):
        pos[v] = k+1

    for k in range(200):
        b = set(a)
        d = list(b)
        m = len(d)
        ans1 = []
        ans2 = []
        dp = [[0]*200 for _ in range(m+1)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(200):
                dp[i+1][j] += dp[i][j]
                dp[i+1][(j+d[i]) % 200] += dp[i][j]
        i, j = m, k
        if dp[m][k] <= 1:
            continue
        while i > 0 and j > 0:
            q = max(-(d[i-1]-j), 200-(d[i-1]-j)) % 200
            if dp[i-1][j] > 0:
                i -= 1
            elif dp[i-1][q] > 0:
                ans1.append(d[i-1])
                i -= 1
                j = q

        for p in ans1:
            b.discard(p)

        d = list(b)
        m = len(d)
        dp = [[0]*200 for _ in range(m+1)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(200):
                dp[i+1][j] += dp[i][j]
                dp[i+1][(j+d[i]) % 200] += dp[i][j]
        i, j = m, k
        if dp[m][k] <= 0:
            continue
        while i > 0 and j > 0:
            q = max(-(d[i-1]-j), 200-(d[i-1]-j)) % 200
            if dp[i-1][j] > 0:
                i -= 1
            elif dp[i-1][q] > 0:
                ans2.append(d[i-1])
                i -= 1
                j = q

        if ans1 and ans2:
            break

    X = []
    Y = []
    for p in ans1:
        X.append(pos[p])
    for p in ans2:
        Y.append(pos[p])
    X.sort()
    Y.sort()
    if X and Y:
        print('Yes')
        print(len(X), *X)
        print(len(Y), *Y)
        print(check(X))
        print(check(Y))
    else:
        print('No')
