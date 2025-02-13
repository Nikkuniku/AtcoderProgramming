def maxlen(A):
    from collections import defaultdict

    r = 0
    N = len(A)
    temp = 0
    res = 0
    d = defaultdict(int)
    for left in range(N):
        while r < N and d[A[r]] == 0:
            d[A[r]] += 1
            r += 1
        res = max(res, r - left)
        if r == left:
            r += 1
        else:
            d[A[left]] -= 1
    return res


N = int(input())
A = list(map(int, input().split()))
# 偶数
E = []
temp = []
for i in range(N):
    if i % 2 == 0 and i < N - 1:
        if A[i] == A[i + 1]:
            temp.append(A[i])
        else:
            E.append(temp)
            temp = []
if temp:
    E.append(temp)
# 奇数
O = []
temp = []
for i in range(N):
    if i % 2 == 1 and i < N - 1:
        if A[i] == A[i + 1]:
            temp.append(A[i])
        else:
            O.append(temp)
            temp = []
if temp:
    O.append(temp)
ans = 0
for L in E:
    ans = max(ans, maxlen(L) * 2)
for L in O:
    ans = max(ans, maxlen(L) * 2)
print(ans)
