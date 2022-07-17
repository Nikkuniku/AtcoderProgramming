from itertools import combinations_with_replacement, permutations, product
n, m, d = map(int, input().split())

p = [i for i in range(1, n+1)]

c = product(p, repeat=m)

ans = []
for p in c:
    tmp = 0
    for i in range(m-1):
        if abs(p[i]-p[i+1]) == d:
            tmp += 1
    ans.append(tmp)

print(ans)
print(ans.count(1))
print(ans.count(2))
print(ans.count(3))

print(pow(10**9, 10**9))
