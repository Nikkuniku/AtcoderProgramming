N, T, P = map(int, input().split())
L = list(map(int, input().split()))
ans = 0
while 1:
    cnt = 0
    for i in range(N):
        cnt += L[i] >= T
    if cnt >= P:
        exit(print(ans))
    for i in range(N):
        L[i] += 1
    ans += 1
