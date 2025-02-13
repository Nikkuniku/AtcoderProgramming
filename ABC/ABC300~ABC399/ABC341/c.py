H, W, N = map(int, input().split())
T = list(input())
M = len(T)
S = [list(input()) for _ in range(H)]


def check(i, j):
    si, sj = i, j
    if S[si][sj] == "#":
        return False
    for k in range(M):
        if T[k] == "L":
            sj -= 1
        elif T[k] == "R":
            sj += 1
        elif T[k] == "U":
            si -= 1
        elif T[k] == "D":
            si += 1
        if S[si][sj] == "#":
            return False
    return True


ans = 0
for i in range(1, H - 1):
    for j in range(1, W - 1):
        ans += check(i, j)
print(ans)
