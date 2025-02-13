H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1
S = [list(input()) for _ in range(H)]
T = input()
visit = set()
for t in T:
    if t == "U":
        if 0 <= X - 1 < H:
            if S[X - 1][Y] in [".", "@"]:
                X -= 1
    elif t == "D":
        if 0 <= X + 1 < H:
            if S[X + 1][Y] in [".", "@"]:
                X += 1
    elif t == "L":
        if 0 <= Y - 1 < W:
            if S[X][Y - 1] in [".", "@"]:
                Y -= 1
    elif t == "R":
        if 0 <= Y + 1 < W:
            if S[X][Y + 1] in [".", "@"]:
                Y += 1
    if S[X][Y] == "@":
        visit.add((X, Y))
print(X + 1, Y + 1, len(visit))
