from collections import deque
n, m = map(int, input().split())
q = deque()
q.append((0, 0))
ans = [[-1]*n for _ in range(n)]
ans[0][0] = 0
# 平方数を求める
squares = set()
for i in range(m+1):
    if i**2 > m:
        break
    squares.add(i**2)
edge = []
# 平方数の和となる組を求める
for i in range(m+1):
    if m-i**2 in squares:
        edge.append((i, int((m-i**2)**(1/2))))


def move(a, b):
    return [(a, b), (-a, b), (a, -b), (-a, -b)]


while q:
    v = q.popleft()
    vi, vj = v

    for v, w in edge:
        for p in move(v, w):
            if 0 <= vi+p[0] < n and 0 <= vj+p[1] < n:
                if ans[vi+p[0]][vj+p[1]] == -1:
                    ans[vi+p[0]][vj+p[1]] = ans[vi][vj]+1
                    q.append((vi+p[0], vj+p[1]))

for c in ans:
    print(*c)
