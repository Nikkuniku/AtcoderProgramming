# M, D, K = 2277, 11, 361
N, M, D, K = map(int, input().split())


def check(A, P):
    pass
    if (D*A + (D*(D-1)*p)//2) != M:
        return False
    if A+(D-1)*P > K:
        return False
    return True


ans = []
for a in range(K+1):
    for p in range(K+1):
        if check(a, p):
            ans.append((a, p))
ans.sort(key=lambda x: x[1])
print(ans)
can = []
for a, p in ans:
    tmp = []
    for d in range(D):
        tmp.append(a+d*p)
    can.append(tmp)
print(*can, sep="\n")
print(sum([57, 87, 117, 147, 177, 207, 237, 267, 297, 327, 357]))
