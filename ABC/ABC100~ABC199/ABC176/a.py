from math import ceil
N, X, T = map(int, input().split())
ans = T*ceil(N/X)
print(ans)
