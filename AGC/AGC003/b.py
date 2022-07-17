n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
tmp = a.copy()
ans1 = 0
for i in range(n):
    if i > 0:
        if tmp[i-1] == 1 and tmp[i-1]+tmp[i] >= 2:
            ans1 += 1
            tmp[i-1] -= 1
            tmp[i] -= 1
    p, q = divmod(tmp[i], 2)
    ans1 += p
    tmp[i] = q
print(ans1)
