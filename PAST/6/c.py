N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
P, Q = map(int, input().split())
B = set(list(map(int, input().split())))
ans = 0
for i in range(N):
    a = A[i]
    temp = 0
    for j in range(1, a[0] + 1):
        if a[j] in B:
            temp += 1
    ans += temp >= Q
print(ans)
