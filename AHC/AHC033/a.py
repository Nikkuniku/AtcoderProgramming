N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
Moves = [[] for _ in range(N)]


def BFS(sx, sj, P):
    gx = P // 5
    res = ["P"]
    for _ in range(N - 1):
        res.append("R")
    if sx - gx >= 0:
        for _ in range(abs(sx - gx)):
            res.append("U")
        res.append("Q")
        for _ in range(abs(sx - gx)):
            res.append("D")
    else:
        for _ in range(abs(sx - gx)):
            res.append("D")
        res.append("Q")
        for _ in range(abs(sx - gx)):
            res.append("U")
    for _ in range(N - 1):
        res.append("L")
    return res


Now = [0] * 5
Clane = [0, 1, 2, 3, 4]
for _ in range(5):
    for i in range(N):
        c = Clane[i]
        movement = BFS(i, 0, A[i][Now[i]])
        for s in movement:
            Moves[c].append(s)
        for k in range(N):
            if k == c:
                continue
            Moves[k] += "." * len(movement)
        Now[i] += 1

for c in Moves:
    print(*c, sep="")
