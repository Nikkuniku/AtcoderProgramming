def isOK(n, m):
    k = n
    digit = 0
    while k > 0:
        digit += k % 10
        k //= 10
    if digit**m == n:
        return True
    return False


A = []
for n in range(2, 300):
    for m in range(2, 50):
        if isOK(n**m, m):
            A.append(n**m)
A.sort()
print(A[:30])
print(A[29])
