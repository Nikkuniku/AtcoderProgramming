A = []
Q = int(input())
ans = []
for _ in range(Q):
    t, k = map(int, input().split())
    if t == 1:
        A.append(k)
    elif t == 2:
        ans.append(A[-k])
print(*ans, sep="\n")
