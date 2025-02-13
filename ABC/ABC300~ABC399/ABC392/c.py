N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = [(Q[i], i + 1) for i in range(N)]
R.sort()
ans = []
for i, t in R:
    w = t
    ans.append(Q[P[w - 1] - 1])
print(*ans)
