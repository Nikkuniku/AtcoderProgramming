N = int(input())
A = list(map(int, input().split()))
ans = -1
tmp = 0
for k in range(2, max(A)+1):
    cnt = 0
    for i in range(N):
        if A[i] % k == 0:
            cnt += 1
    if cnt > tmp:
        ans = k
        tmp = cnt
print(ans)
