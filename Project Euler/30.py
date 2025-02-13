from itertools import product

P = list(product(range(10), repeat=6))


def isOK(A):
    res = 0
    N = 5
    for i in range(6):
        res += pow(A[i], N)
    res = str(res).zfill(6)
    isOK = True
    for i in range(6):
        if int(res[i]) != A[i]:
            isOK = False
    return isOK


ans = set()
for p in P:
    if isOK(p):
        ans.add(p)
temp = 0
for p in ans:
    b = 0
    for i in range(6):
        b += p[i] * pow(10, 5 - i)
    temp += b
    print(b)
print(ans)
print(temp)

print(isOK((0, 9, 1, 8, 1, 9)))
