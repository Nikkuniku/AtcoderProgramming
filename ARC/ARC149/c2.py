def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def solve(N):
    from sortedcontainers import SortedSet

    A = [[-1] * N for _ in range(N)]
    if N % 2 == 0:
        # 偶数
        c = N * N
        for i in range(N // 2):
            for j in range(N):
                A[i][j] = c
                c -= 2
        Odds = SortedSet([i for i in range(1, N * N + 1, 2)])
        for i in range(N // 2, N):
            for j in range(N):
                if A[i - 1][j] % 2 == 0:
                    c = N * N - 1 - A[i - 1][j]
                else:
                    c = Odds[0]
                A[i][j] = c
                Odds.discard(c)
    else:
        primes = make_divisors(N * N // 2)
        for a in primes:
            b = (N * N // 2) // a
            if a < N and b < N:
                break
        A[a - 1][b - 1] = 2 * N
        A[a][b - 1] = N * N
        A[a - 1][b] = N
        Evens = SortedSet([i for i in range(2, N * N + 1, 2)])
        Odds = SortedSet([i for i in range(1, N * N + 1, 2)])
        Evens.discard(2 * N)
        Odds.discard(N)
        Odds.discard(N * N)
        for i in range(a):
            for j in range(b):
                if A[i][j] != -1:
                    continue
                c = Evens[~0]
                A[i][j] = c
                Evens.discard(c)
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(N):
            for j in range(N):
                if A[i][j] != -1:
                    continue
                isExistEvenVal = False
                for dx, dy in dxy:
                    ni = i + dx
                    nj = j + dy
                    if not (0 <= ni < N and 0 <= nj < N):
                        continue
                    if A[ni][nj] == -1:
                        continue
                    if A[ni][nj] % 2 == 0:
                        c = N * N - A[ni][nj]
                        isExistEvenVal = True
                        break
                if not isExistEvenVal:
                    c = Odds[0]
                A[i][j] = c
                Odds.discard(c)
    return A


N = int(input())
P = solve(N)
for p in P:
    print(*p)
