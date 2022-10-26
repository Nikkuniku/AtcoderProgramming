x, y, z, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ab = []
for ai in a:
    for bi in b:
        ab.append(ai+bi)
ab = sorted(ab)[::-1][:K]
ans = []
for ci in c:
    for abi in ab:
        ans.append(ci+abi)
ans = sorted(ans)[::-1][:K]
print(*ans, sep="\n")
