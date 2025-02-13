N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
ans = [0] * N
cnt = 0
pre = A[0]
for i in range(N):
    if pre != A[i]:
        cnt += 1
    ans[cnt] += 1
    pre = A[i]
print(*ans, sep="\n")
