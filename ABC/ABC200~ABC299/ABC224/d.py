from collections import defaultdict, deque
M = int(input())
edge = [[] for _ in range(9)]
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    edge[u].append(v)
    edge[v].append(u)
d = defaultdict(lambda: -1)
koma = [0]*9
P = list(map(int, input().split()))
for i, v in enumerate(P):
    koma[v-1] = i+1


def hash():
    res = 0
    for i, v in enumerate(koma):
        res += pow(10, i)*v
    return res


def akimasu(h):
    res = -1
    for i in range(9):
        if h % 10 == 0:
            res = i
            break
        else:
            h //= 10
    return res


def move_hash(h, aki_idx, adj_idx, val):
    res = h
    res -= pow(10, adj_idx)*val
    res += pow(10, aki_idx)*val
    return res


def adj_val(h, adj_idx):
    res = -1
    h //= pow(10, adj_idx)
    res = h % 10
    return res


s = hash()
d[s] = 0
q = deque()
q.append(s)
while q:
    v = q.popleft()

    aki_idx = akimasu(v)
    for e in edge[aki_idx]:
        w = adj_val(v, e)
        h_dash = move_hash(v, aki_idx, e, w)
        if d[h_dash] == -1:
            d[h_dash] = d[v]+1
            q.append(h_dash)

print(d[87654321])
