P = list(map(int, input().split()))
ans = []
N = len(P)
S = "ABCDE"
for i in range(1, 1 << 5):
    user = []
    point = 0
    for j in range(N):
        if i & (1 << j):
            user.append(S[wj])
            point += P[j]
    ans.append(("".join(user), point))
ans.sort(key=lambda x: x[0])
ans.sort(key=lambda x: x[1], reverse=True)
for name, score in ans:
    print(name)
