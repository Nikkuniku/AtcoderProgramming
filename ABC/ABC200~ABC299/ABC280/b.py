N = int(input())
A = list(map(int, input().split()))
ans = [A[0]]
for i in range(1, N):
    ans.append(A[i]-A[i-1])
print(*ans)
