L, R = map(int, input().split())
ans = []
l = L
K = 62
while 1:
    for i in range(K):
        if l % pow(2, i) != 0:
            break
        j = l // pow(2, i)
        if pow(2, i) * (j + 1) > R:
            break
    i -= 1
    j = l // pow(2, i)
    a = pow(2, i) * j
    b = pow(2, i) * (j + 1)
    ans.append((a, b))
    l = b
    if b == R:
        break
print(len(ans))
for c in ans:
    print(*c)
