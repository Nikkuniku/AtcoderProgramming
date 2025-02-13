from sys import setrecursionlimit

setrecursionlimit(10**8)
N = int(input())


def rec(k):
    if k == 1:
        return ["###", "#.#", "###"]
    res = []
    for i in range(9):
        if i != 4:
            res.append(rec(k - 1))
        else:
            temp = []
            for _ in range(pow(3, k - 1)):
                temp.append("." * pow(3, k - 1))
            res.append(temp)
    res2 = []
    for j in range(pow(3, k - 1)):
        temp = []
        for i in range(3):
            temp.append(res[i][j])
        res2.append("".join(temp))
    for j in range(pow(3, k - 1)):
        temp = []
        for i in range(3, 6):
            temp.append(res[i][j])
        res2.append("".join(temp))
    for j in range(pow(3, k - 1)):
        temp = []
        for i in range(6, 9):
            temp.append(res[i][j])
        res2.append("".join(temp))
    return res2


if N == 0:
    exit(print("#"))
ans = rec(N)
for c in ans:
    print(*c, sep="")
