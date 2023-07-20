N = int(input())
ans = N
S = set()
for i in range(2, 10**5+1):
    k = 2
    while 1:
        t = pow(i, k)
        if t <= N:
            S.add(t)
        else:
            break
        k += 1

ans -= len(S)
print(ans)
