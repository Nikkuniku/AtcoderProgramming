from collections import defaultdict, deque

N = int(input())
S = input() + ".."
T = input()
dp = defaultdict(lambda: -1)
dp[S] = 0
q = deque([S])
while q:
    v = q.popleft()
    blank = -1
    for i in range(N + 1):
        if v[i] == "." and v[i + 1] == ".":
            blank = i
            break
    if blank == -1:
        continue
    for i in range(N + 1):
        if v[i] == ".":
            continue
        next = list(v)
        next[i], next[i + 1], next[blank], next[blank + 1] = (
            next[blank],
            next[blank + 1],
            next[i],
            next[i + 1],
        )
        next = "".join(next)
        if dp[next] != -1:
            continue
        dp[next] = dp[v] + 1
        q.append(next)
ans = dp[T + ".."]
print(ans)
