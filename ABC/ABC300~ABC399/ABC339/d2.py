N = int(input())
s = []
for i in range(N):
    s.append(["."] * N)
s[0][0] = "P"
s[N - 1][N - 1] = "P"
for c in s:
    print(*c, sep="")
