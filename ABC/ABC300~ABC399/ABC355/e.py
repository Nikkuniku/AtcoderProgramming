N, L, R = map(int, input().split())
res = []
if L % 2 != 0:
    print("?", 0, L, flush=True)
    T = int(input())
    res.append(T)
    L += 1
diff = R - L + 1
while diff:
    for i in range(30, -1, -1):
        if pow(2, i) + L - 1 <= R and pow(2, i) <= L:
            j = L // pow(2, i)
            break
    print("?", i, j, flush=True)
    T = int(input())
    res.append(T)
    L += pow(2, i)
    diff -= pow(2, i)
print("!", sum(res) % 100, flush=True)
