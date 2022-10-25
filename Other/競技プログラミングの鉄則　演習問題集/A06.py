n, q = map(int, input().split())
a = list(map(int, input().split()))
csum = [0]
for p in a:
    csum.append(csum[-1]+p)

ans = []
for _ in range(q):
    l, r = map(int, input().split())
    tmp = csum[r]-csum[l-1]
    ans.append(tmp)
print(*ans, sep="\n")
