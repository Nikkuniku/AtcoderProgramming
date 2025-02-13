from functools import lru_cache
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")


N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]


@lru_cache(maxsize=None)
def dfs(s, t):
    # 取れるかどうか
    isOK = False
    for i in range(N):
        if s & (1 << i):
            continue
        for j in range(i + 1, N):
            if s & (1 << j):
                continue
            if P[i][0] == P[j][0] or P[i][1] == P[j][1]:
                isOK = True
                break
    if isOK:
        for i in range(N):
            if s & (1 << i):
                continue
            for j in range(i + 1, N):
                if s & (1 << j):
                    continue
                if P[i][0] == P[j][0] or P[i][1] == P[j][1]:
                    if not dfs(s | (1 << i) | (1 << j), t ^ 1):
                        return True
        return False
    else:
        return False


isOK = dfs(0, 0)
if isOK:
    ans = "Takahashi"
else:
    ans = "Aoki"
print(ans)
