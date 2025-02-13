def s(j):
    return j * (j + 1) * (2 * j + 1) // 6


M = 10**18
N = 10000000
for i in range(N + 1):
    if s(i) >= M:
        print(i, s(i))
        break
