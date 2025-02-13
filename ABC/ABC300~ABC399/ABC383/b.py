from itertools import combinations

H, W, D = map(int, input().split())
S = [list(input()) for _ in range(H)]
A = []
for i in range(H):
    for j in range(W):
        A.append((i, j))
C = list(combinations(A, 2))


def check(humids):
    res = 0
    for a, b in humids:
        if S[a][b] == "#":
            return 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            isOK = False
            for a, b in humids:
                if abs(i - a) + abs(j - b) <= D:
                    isOK = True
            if isOK:
                res += 1
    return res


ans = 0
for c in C:
    temp = check(c)
    ans = max(ans, temp)
print(ans)
