from itertools import product
n, a, b, c = map(int, input().split())
L = [int(input()) for _ in range(n)]
B = [a, b, c]
ans = 1000_000_000_000_000
p = product([0, 1, 2, 3], repeat=n)
bamboo = [[], [], [], []]
for d in p:
    for j in range(4):
        bamboo[j] = []
    tmp = 0
    for i in range(n):
        bamboo[d[i]].append(L[i])
    if (not bamboo[0]) or (not bamboo[1]) or (not bamboo[2]):
        continue
    for k in range(3):
        tmp += 10*(len(bamboo[k])-1)+abs(B[k]-sum(bamboo[k]))

    ans = min(ans, tmp)
print(ans)
