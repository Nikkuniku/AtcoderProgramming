from functools import lru_cache
import sys
sys.setrecursionlimit(1000000)

n = int(input())
a = list(map(int, input().split()))
dp = [[False]*(n+2) for _ in range(n+2)]


@lru_cache(maxsize=None)
def rec(i, j):
    if n % 2 == 0:
        if abs(j-i) == 0:
            return 0
        if dp[i][j] != False:
            return dp[i][j]

        re = 0
        if (j-i) % 2 == 0:
            if a[j-1] >= a[i-1]:
                re = rec(i, j-1)+a[j-1]
            else:
                re = rec(i+1, j)+a[j-1]
            dp[i][j] = re
            return dp[i][j]
        else:
            re = min(rec(i, j-1)-a[j-1], rec(i+1, j)-a[i])
            dp[i][j] = re
            return dp[i][j]
    else:
        if abs(j-i) == 1:
            return a[i]

        if dp[i][j] >= 0:
            return dp[i][j]

        if (j-i) % 2 == 0:
            re = min(rec(i, j-1)-a[j-1], rec(i+1, j)-a[i])
            dp[i][j] = re
            return dp[i][j]
        else:
            re = max(rec(i, j-1)+a[j-1], rec(i+1, j)+a[i-1])
            dp[i][j] = re
            return dp[i][j]


ans = rec(0, n)
print(ans)
