from bisect import bisect_right

N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))
R = []
L = []
for i, v in enumerate(S):
    if v == "0":
        L.append(X[i])
    else:
        R.append(X[i])
L.sort()
R.sort()
ans = 0
for x in R:
    b = bisect_right(L, x + 2 * T)
    a = bisect_right(L, x)
    ans += b - a
print(ans)
