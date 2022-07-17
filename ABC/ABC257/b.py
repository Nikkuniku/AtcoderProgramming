n, k, q = map(int, input().split())
a = list(map(int, input().split()))
L = list(map(int, input().split()))
for i in range(q):
    p = L[i]-1
    if a[p] == n:
        continue
    if a[p]+1 in a:
        continue
    else:
        a[p] += 1
print(*a)
