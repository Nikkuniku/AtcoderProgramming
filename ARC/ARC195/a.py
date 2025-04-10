N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def calc_indexies(P, Q):
    n = len(P)
    m = len(Q)
    i = 0
    res = []
    for j in range(n):
        if Q[i] == P[j]:
            res.append(j)
            i += 1
        if i >= m:
            break
    return res


revA, revB = A[::-1], B[::-1]
X = calc_indexies(A, B)
Y = calc_indexies(revA, revB)[::-1]
for i in range(len(Y)):
    Y[i] = N - 1 - Y[i]
ans = "No"
if len(X) == len(Y) == M and X != Y:
    ans = "Yes"
print(ans)
