import pypyjit
from collections import Counter
import sys
sys.setrecursionlimit(1000000)
pypyjit.set_param('max_unroll_recursion=-1')
readline = sys.stdin.readline
n = int(input())
a = list(map(int, readline().split()))
c = Counter(a)
dp = [[[-1]*301 for _ in range(301)] for _ in range(301)]
dp[0][0][0] = 0


def f(i, j, k):
    if i == 0 and j == 0 and k == 0:
        return 0
    if dp[i][j][k] != -1:
        return dp[i][j][k]

    re = n/(i+j+k)
    if k > 0:
        re += k*f(i, j+1, k-1)/(i+j+k)
    if j > 0:
        re += j*f(i+1, j-1, k)/(i+j+k)
    if i > 0:
        re += i*f(i-1, j, k)/(i+j+k)
    dp[i][j][k] = re
    return re


ans = f(c[1], c[2], c[3])
print(ans)
