N = int(input())
ST = [list(input().split(" ")) for _ in range(N)]
P = [False] * N
for i in range(N):
    for k in range(2):
        cnt = 0
        si = ST[i][k]
        for j in range(N):
            if j == i:
                continue
            if si in ST[j]:
                cnt += 1
        P[i] |= cnt == 0
if all(P):
    ans = "Yes"
else:
    ans = "No"
print(ans)
