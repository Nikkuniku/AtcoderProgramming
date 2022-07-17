n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = max(a)

idx = set()
for i in range(n):
    if a[i] == m:
        idx.add(i+1)

ans = 'No'
for j in range(k):
    if b[j] in idx:
        ans = 'Yes'
        break
print(ans)
