N = int(input())
P = [0, 0]+list(map(int, input().split()))
ans = [0]*(N+1)
for i in range(2, N+1):
    ans[i] = ans[P[i]]+1
print(ans[-1])
