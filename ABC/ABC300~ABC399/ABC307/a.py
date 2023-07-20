N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(N):
    tmp = A[i*7:(i+1)*7]
    ans.append(sum(tmp))
print(*ans)
