H, W = map(int, input().split())
si, sj = map(int, input().split())
si -= 1
sj -= 1
C = [list(input()) for _ in range(H)]
X = input()
for i, v in enumerate(X):
    if v == "L":
        if sj > 0 and C[si][sj - 1] == ".":
            sj -= 1
    elif v == "R":
        if sj < W - 1 and C[si][sj + 1] == ".":
            sj += 1
    elif v == "U":
        if si > 0 and C[si - 1][sj] == ".":
            si -= 1
    elif v == "D":
        if si < H - 1 and C[si + 1][sj] == ".":
            si += 1
print(si + 1, sj + 1)
