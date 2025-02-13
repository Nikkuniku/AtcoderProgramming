N, D = map(int, input().split())
S = list(input())
for _ in range(D):
    for i in range(N - 1, -1, -1):
        if S[i] == "@":
            S[i] = "."
            break
print(*S, sep="")
