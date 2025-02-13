N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
ans = []
Q = int(input())
for _ in range(Q):
    t, d = map(int, input().split())
    t -= 1
    if d % P[t][0] == P[t][1]:
        ans.append(d)
    else:
        if d % P[t][0] < P[t][1]:
            tmp = d + (P[t][1] - d % P[t][0])
        else:
            tmp = ((d // P[t][0]) + 1) * P[t][0] + P[t][1]
        ans.append(tmp)
print(*ans, sep="\n")
