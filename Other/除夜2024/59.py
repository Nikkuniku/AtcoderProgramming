N, T, P = map(int, input().split())
L = list(map(int, input().split()))
M = 200
for i in range(M):
    cnt = 0
    for j in range(N):
        cnt += L[j] >= T
    if cnt >= P:
        exit(print(i))
    for j in range(N):
        L[j] += 1
