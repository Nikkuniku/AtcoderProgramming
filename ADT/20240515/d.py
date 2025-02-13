N = 10
S = [list(input()) for _ in range(N)]


def check(a, b, c, d):
    for i in range(a, b + 1):
        for j in range(c, d + 1):
            if S[i][j] == ".":
                return False
    return True


a = 1 << 60
b = -1
for i in range(N):
    if "#" in S[i]:
        a = min(a, i + 1)
        b = max(b, i + 1)
c, d = 1 << 60, -1
for j in range(N):
    isOK = False
    for i in range(N):
        if S[i][j] == "#":
            isOK = True
    if isOK:
        c = min(c, j + 1)
        d = max(d, j + 1)
print(a, b)
print(c, d)
