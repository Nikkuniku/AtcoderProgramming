def count_differents(s, t):
    res = 0
    for i in range(len(s)):
        res += s[i] != t[i]
    return res


from collections import deque, defaultdict

first, last = input().split()
N = int(input())
S = [input() for _ in range(N)] + [last]
dist = defaultdict(lambda: -1)
pre = defaultdict(lambda: -1)
q = deque([first])
dist[first] = 0
while q:
    v = q.popleft()
    for i in range(N + 1):
        k = count_differents(v, S[i])
        if k != 1:
            continue
        if dist[S[i]] != -1:
            continue
        dist[S[i]] = dist[v] + 1
        pre[S[i]] = v
        q.append(S[i])
if dist[last] == -1:
    exit(print(-1))
if dist[last] == 0:
    print(0)
    print(first)
    exit(print(last))
now = last
footprint = []
while now != -1:
    footprint.append(now)
    now = pre[now]
print(len(footprint) - 2)
print(*footprint[::-1], sep="\n")
