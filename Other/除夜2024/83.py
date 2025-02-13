N = 5
A = list(map(int, input().split()))
S = "ABCDE"
res = []
for i in range(1, 1 << N):
    Name = []
    score = 0
    for j in range(N):
        if i & (1 << j):
            Name.append(S[j])
            score += A[j]
    res.append((score, "".join(Name)))
res.sort(key=lambda x: x[1])
res.sort(key=lambda x: x[0], reverse=True)
for c in res:
    print(c[1])
