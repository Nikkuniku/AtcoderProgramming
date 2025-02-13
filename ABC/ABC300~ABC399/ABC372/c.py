N, Q = map(int, input().split())
S = list(input())
T = [0] * N
for i in range(N - 2):
    if S[i] == "A" and S[i + 1] == "B" and S[i + 2] == "C":
        T[i] = 1
ans = []
M = sum(T)
for _ in range(Q):
    query = input().split()
    x = int(query[0]) - 1
    c = query[1]
    S[x] = c
    for i in range(max(0, x - 2), x + 1):
        tmp = []
        for k in range(3):
            if i + k > N - 1:
                continue
            tmp.append(S[i + k])
        if len(tmp) == 3 and "".join(tmp) == "ABC":
            if T[i] == 0:
                T[i] = 1
                M += 1
        else:
            if T[i] == 1:
                T[i] = 0
                M -= 1
    ans.append(M)
print(*ans, sep="\n")
