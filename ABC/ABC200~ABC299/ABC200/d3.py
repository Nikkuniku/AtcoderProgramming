def check(a, L):
    tmp = 0
    P = len(L)
    ARR = L[0:]
    for i in range(P):
        tmp += a[ARR[i]-1]
    return tmp % 200


def solve(a):
    from collections import defaultdict, Counter
    # n = int(input())
    # a = list(map(int, input().split()))
    amod = [a[i] % 200 for i in range(n)]
    C = Counter(amod)
    Existflg = False
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

        print('Yes')
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

            b -= set(ans1)
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
                q = max(200-(d[i-1]-j), 200-(d[i-1]-j)) % 200
                if dp[i-1][j] > 0:
                    i -= 1
                elif dp[i-1][q] > 0:
                    ans2.append(d[i-1])
                    i -= 1
                    j = q

            if ans1 and ans2:
                break

        X = [pos[p] for p in ans1]
        Y = [pos[p] for p in ans2]
        X.sort()
        Y.sort()
        if X and Y:
            print('Yes')
            print(len(X), *X)
            print(len(Y), *Y)
            # print(check(a, X))
            # print(check(a, Y))
        else:
            print('No')


n = int(input())
a = list(map(int, input().split()))
solve(a)
