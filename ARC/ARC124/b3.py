n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()
candidate = []
for i in range(n):
    candidate.append(a[0] ^ b[i])
ans = []
for x in candidate:
    c = []
    for i in range(n):
        c.append(x ^ a[i])

    c.sort()
    if b == c:
        ans.append(x)
ans=list(set(ans))
ans.sort()
print(len(ans))
print(*ans, sep="\n")
