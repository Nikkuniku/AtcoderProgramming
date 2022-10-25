from itertools import product
h1, w1 = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(h1)]
h2, w2 = map(int, input().split())
b = [tuple(map(int, input().split())) for _ in range(h2)]


def check(p):
    if not p:
        return False
    if len(p) != h2 or len(p[0]) != w2:
        return False

    for i in range(h2):
        for j in range(w2):
            if p[i][j] != b[i][j]:
                return False

    return True


for i in product([0, 1], repeat=h1):
    for j in product([0, 1], repeat=w1):
        tmp = []
        for k, v in enumerate(i):
            if v == 0:
                continue
            t = []
            for m, w in enumerate(j):
                if w == 0:
                    continue
                t.append(a[k][m])
            tmp.append(t)
        if check(tmp):
            print('Yes')
            exit()
print('No')
