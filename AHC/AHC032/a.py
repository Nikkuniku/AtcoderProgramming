from random import randint

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
S = [list(map(int, input().split())) for _ in range(M)]
L = randint(0, K)
ans = []
for _ in range(L):
    m = randint(0, M - 1)
    p = randint(0, N - 3)
    q = randint(0, N - 3)
    ans.append((m, p, q))
print(len(ans))
for c in ans:
    print(*c)
