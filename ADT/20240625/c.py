Q = int(input())
A = []
ans = []
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        A.append(x)
    else:
        ans.append(A[-x])
print(*ans, sep="\n")
