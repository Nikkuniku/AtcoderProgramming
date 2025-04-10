N, M = map(int, input().split())
res = 0
L = 1000_000_000
for i in range(M + 1):
    res += pow(N, i)
    if res > L:
        exit(print("inf"))
print(res)
